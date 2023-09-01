from aiogram import executor

from loader import dp


if __name__ == '__main__':
    from handlers import *
    print("Bot online")
    executor.start_polling(dp, )
