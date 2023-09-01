from sqlalchemy.ext.asyncio import AsyncSession

from rdb import BaseDAO


class HolderDao:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.base = BaseDAO
        # self.user = UserDAO(self.session)
        # self.todo = TodoDAO(self.session)