from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column


from .base import BaseModel


class Course(BaseModel):
    __tablename__ = 'course'

    title: Mapped[str] = mapped_column(String, nullable=False)
    image: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[str] = mapped_column(String, nullable=False)
    duration: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[int] = mapped_column(Integer, nullable=False)

    def __str__(self):
        return f"{self.title}\n{self.price}\n{self.duration}"
