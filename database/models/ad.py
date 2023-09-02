from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column


from .base import BaseModel


class Ad(BaseModel):
    __tablename__ = 'application'

    chat_name: Mapped[str] = mapped_column(String, nullable=False)
    chat_id: Mapped[str] = mapped_column(Integer, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=True)

    def __str__(self):
        return f"{self.chat_name}\n{self.chat_id}"
