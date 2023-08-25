from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from decouple import config

from loader import dp


@dp.message_handlers(CommandStart())
async def start(message: types.Message):
    text = "Assalomu alaykum! {full_name} xush kelibsiz!\nKurslarga yozilish uchun pastdagi <b>Murojaat</b> tugmasini bosing."
    await message.answer(text=text, parse_mode=types.ParseMode.HTML)
