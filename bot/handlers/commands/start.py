from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.deep_linking import get_start_link

from decouple import config

from loader import dp
from keyboards.default import buttons


async def create_link(id: int) -> str:
    return await get_start_link(id)


@dp.message_handler(CommandStart())
async def start(message: types.Message) -> None:
    args = message.get_args()
    text = "Assalomu alaykum! {full_name} xush kelibsiz!\nKurslarga yozilish uchun pastdagi <b>Murojaat</b> tugmasini bosing."
    if args:
        print(args)
    await message.answer(text=text, parse_mode=types.ParseMode.HTML, reply_markup=buttons)
