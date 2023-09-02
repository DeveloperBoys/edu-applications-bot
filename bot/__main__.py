import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from . import handlers
from .loader import dp, bot, WEBHOOK_URL, WEBHOOK_PATH
from database.connection import create_pool, make_connection_string

app = FastAPI(
    docs_url="/docs",
    version="1.0.0"
)

# Load configurations and create database connection pool
pool = create_pool(url=make_connection_string())

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize aiogram Dispatcher and Bot
dp.middleware.setup(LoggingMiddleware())
Bot.set_current(bot)
Dispatcher.set_current(dp)


# Set up the webhook for the Telegram bot
@app.on_event("startup")
async def on_startup():
    url = await bot.get_webhook_info()
    print(url)
    print(WEBHOOK_URL)
    if url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)


# Handle incoming webhook updates
@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


# Shutdown event to close the bot session
@app.on_event("shutdown")
async def on_shutdown():
    await bot.get_session().close()

if __name__ == '__main__':
    uvicorn.run(
        "__main__:app",  # Replace "your_script_name" with the actual name of your script
        host="127.0.0.1",
        port=8000
    )
