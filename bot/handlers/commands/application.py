from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.default import check_button


@dp.message_handler(text="📝 Murojaat", state=None)
async def application(message: types.Message, state: FSMContext) -> None:
    text = "F.I.SH. kiriting!\nMisol uchun: Abdusattor Abdullayev yoki G'anisher Safaraliyev Abdusamad o'g'li"
    await state.set_state("get_fullname")
    await message.reply(text=text)


@dp.message_handler(state="get_fullname")
async def get_fullname(message: types.Message, state: FSMContext) -> None:
    getted_full_name = await message.from_user.id
    text = "F.I.SH. kiriting!\nMisol uchun: Abdusattor Abdullayev yoki G'anisher Safaraliyev Abdusamad o'g'li"
    await state.set_state("get_phonenumber")
    await message.reply(text=text)
