from pydantic import parse_obj_as
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from .base import BaseDAO
from dto import User as UserDTO


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def create_user(
        self,
        full_name: str,
        phone_number: str,
        username: str | None,
        telegram_id: int
    ) -> UserDTO:
        result = await self.session.execute(
            insert(User).values(
                full_name=full_name,
                phone_number=phone_number,
                username=username,
                telegram_id=telegram_id
            ).returning(User)
        )
        await self.session.commit()
        return UserDTO.from_orm(result.scalar())

    async def get_user_by_telegram_id(self, telegram_id: int) -> UserDTO:
        result = await self.session.execute(
            select(User).filter(User.telegram_id == telegram_id)
        )
        user = result.scalar()
        if user is not None:
            return UserDTO.from_orm(user)

    async def update_user(
        self,
        telegram_id: int,
        full_name: str,
        phone_number: str,
        username: str | None
    ) -> UserDTO:
        result = await self.session.execute(
            update(User).values(
                full_name=full_name,
                phone_number=phone_number,
                username=username
            ).filter(User.telegram_id == telegram_id).returning(User)
        )
        await self.session.commit()
        return UserDTO.from_orm(result.scalar())

    async def delete_user_by_telegram_id(self, telegram_id: int) -> UserDTO:
        result = await self.session.execute(
            delete(User).filter(User.telegram_id ==
                                telegram_id).returning(User)
        )
        await self.session.commit()
        return UserDTO.from_orm(result.scalar())
