from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column


from .base import BaseModel


class Application(BaseModel):
    __tablename__ = 'application'

    full_name: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    goals: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=True)

    def __str__(self):
        return f"{self.full_name}\n{self.phone_number}"
