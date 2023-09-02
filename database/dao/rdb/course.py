from pydantic import parse_obj_as
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from models import Course
from dto import Course as CourseDTO


class CourseDAO(BaseDAO[Course]):
    def __init__(self, session: AsyncSession):
        super().__init__(Course, session)

    async def create_course(
        self,
        title: str,
        image: str,
        price: str,
        duration: str | None,
        description: int
    ) -> CourseDTO:
        result = await self.session.execute(
            insert(Course).values(
                title=title,
                image=image,
                price=price,
                duration=duration,
                description=description
            ).returning(Course)
        )
        await self.session.commit()
        return CourseDTO.from_orm(result.scalar())

    async def get_courses(self) -> list[CourseDTO]:
        result = await self.session.execute(
            select(Course)
        )
        return parse_obj_as(list[CourseDTO], result.scalar().all())

    async def get_course_by_id(self, course_id: int) -> CourseDTO:
        result = await self.session.execute(
            select(Course).filter(Course.id == course_id)
        )
        course = result.scalar()
        if course is not None:
            return CourseDTO.from_orm(course)

    async def update_course(
        self,
        course_id: int,
        title: str,
        image: str,
        price: str,
        duration: str | None,
        description: int
    ) -> CourseDTO:
        result = await self.session.execute(
            update(Course).values(
                title=title,
                image=image,
                price=price,
                duration=duration,
                description=description
            ).filter(Course.id == course_id).returning(Course)
        )
        await self.session.commit()
        return CourseDTO.from_orm(result.scalar())

    async def delete_course(self, course_id: int) -> CourseDTO:
        result = await self.session.execute(
            delete(Course).filter(Course.id == course_id).returning(Course)
        )
        await self.session.commit()
        return CourseDTO.from_orm(result.scalar())
