from pydantic import parse_obj_as
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from base import BaseDAO
from models import Application
from dto import Application as ApplicationDTO


class ApplicationDAO(BaseDAO[Application]):
    def __init__(self, session: AsyncSession):
        super().__init__(Application, session)

    async def create_application(
        self,
        full_name: str,
        phone_number: str,
        goals: str,
        username: str | None
    ) -> ApplicationDTO:
        result = await self.session.execute(
            insert(Application).values(
                full_name=full_name,
                phone_number=phone_number,
                goals=goals,
                username=username
            ).returning(Application)
        )
        await self.session.commit()
        return ApplicationDTO.from_orm(result.scalar())

    async def get_applications(self) -> list[ApplicationDTO]:
        result = await self.session.execute(
            select(Application)
        )
        return parse_obj_as(list[ApplicationDTO], result.scalar().all())

    async def get_application_by_id(self, application_id: int) -> ApplicationDTO:
        result = await self.session.execute(
            select(Application).filter(Application.id == application_id)
        )
        application = result.scalar()
        if application is not None:
            return ApplicationDTO.from_orm(application)

    async def update_application(
        self,
        application_id: int,
        full_name: str,
        phone_number: str,
        goals: str,
        username: str | None
    ) -> ApplicationDTO:
        result = await self.session.execute(
            update(Application).values(
                full_name=full_name,
                phone_number=phone_number,
                goals=goals,
                username=username
            ).filter(Application.id == application_id).returning(Application)
        )
        await self.session.commit()
        return ApplicationDTO.from_orm(result.scalar())

    async def delete_application(self, application_id: int) -> ApplicationDTO:
        result = await self.session.execute(
            delete(Application).filter(Application.id ==
                                       application_id).returning(Application)
        )
        await self.session.commit()
        return ApplicationDTO.from_orm(result.scalar())
