from .base import Base


class User(Base):

    full_name: str
    phone_number: str
    username: str
    telegram_id: int
