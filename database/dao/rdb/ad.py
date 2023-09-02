from pydantic import parse_obj_as
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from dto import Ad as AdDTO
from models import Ad
from .base import BaseDAO


class AdDAO(BaseDAO[Ad]):
    def __init__(self, session: AsyncSession):
        super().__init__(Ad, session)

    async def create_ad(
        self,
        chat_name: str,
        chat_id: int,
        url: str | None
    ) -> AdDTO:
        result = await self.session.execute(
            insert(Ad).values(
                chat_name=chat_name,
                chat_id=chat_id,
                url=url
            ).returning(Ad)
        )
        await self.session.commit()
        return AdDTO.from_orm(result.scalar())

    async def get_ads(self) -> list[AdDTO]:
        result = await self.session.execute(
            select(Ad)
        )
        return parse_obj_as(list[AdDTO], result.scalar().all())

    async def get_ad_by_id(self, ad_id: int) -> AdDTO:
        result = await self.session.execute(
            select(Ad).filter(Ad.id == ad_id)
        )
        ad = result.scalar()
        if ad is not None:
            return AdDTO.from_orm(ad)

    async def update_ad(
        self,
        ad_id: int,
        chat_name: str,
        chat_id: int,
        url: str | None
    ) -> AdDTO:
        result = await self.session.execute(
            update(Ad).values(
                chat_name=chat_name,
                chat_id=chat_id,
                url=url
            ).filter(Ad.id == ad_id).returning(Ad)
        )
        await self.session.commit()
        return AdDTO.from_orm(result.scalar())

    async def delete_ad(self, ad_id: int) -> AdDTO:
        result = await self.session.execute(
            delete(Ad).filter(Ad.id == ad_id).returning(Ad)
        )
        await self.session.commit()
        return AdDTO.from_orm(result.scalar())
