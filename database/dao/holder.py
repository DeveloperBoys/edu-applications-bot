from sqlalchemy.ext.asyncio import AsyncSession

from rdb import BaseDAO, UserDAO, ApplicationDAO, AdDAO, CourseDAO


class HolderDao:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.base = BaseDAO
        self.user = UserDAO(self.session)
        self.application = ApplicationDAO(self.session)
        self.ad = AdDAO(self.session)
        self.course = CourseDAO(self.session)
