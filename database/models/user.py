from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column


from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=True)
    telegram_id: Mapped[int] = mapped_column(Integer, nullable=False)

    def __str__(self):
        return f"{self.name}\n{self.email}\n{self.password}"
