import asyncio
import logging

from aiogram import executor

from loader import dp

logging.basicConfig(level=logging.INFO)


async def on_startup(dp):
    print("Bot is online")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
