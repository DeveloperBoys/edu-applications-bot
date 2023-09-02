from aiogram import types
from aiogram.dispatcher import FSMContext

from decouple import config

from loader import dp, bot


@dp.message_handler(text="📝 Murojaat", state="*")
async def application(message: types.Message, state: FSMContext) -> None:
    text = "F.I.SH. kiriting!\nMisol uchun: Abdusattor Abdullayev yoki G'anisher Safaraliyev Abdusamad o'g'li"
    await message.reply(text=text)
    await state.set_state("get_fullname")


@dp.message_handler(state="get_fullname")
async def get_fullname(message: types.Message, state: FSMContext) -> None:
    full_name = message.text
    await state.update_data(full_name=full_name)
    text = "Bog'lanish uchun telefon raqamingizni qoldiring\nMisol uchun: +998900459442 yoki 900459442"
    await message.reply(text=text)
    await state.set_state("get_phonenumber")


@dp.message_handler(state="get_phonenumber")
async def get_fullname(message: types.Message, state: FSMContext) -> None:
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    text = "Siz aynan qaysi kursga yozilmoqchi ekanligingiz va bizdan nimalarni kutayotganingizni qisqacha yozing."
    await message.reply(text=text)
    await state.set_state("get_goals")


@dp.message_handler(state="get_goals")
async def get_goals(message: types.Message, state: FSMContext) -> None:
    goals = message.text
    full_name = await state.get_data("full_name")
    phone_number = await state.get_data("phone_number")
    username = message.from_user.username
    text = ""

    if username:
        text += "\nTelegram: {username}".format(username=username)

    text += "<b>Yangi murojaat!</b>\nF.I.SH: {full_name}\nTelefon raqami: {phone_number}\nMaqsadi: {goals}".format(
        full_name=full_name, phone_number=phone_number, goals=goals)

    await bot.send_message(chat_id=config("CHAT_ID"), text=text)
    await message.answer(text="Ma'lumotlaringiz muvaffaqiyatli yuborildi! Tezda siz bilan bog'lanamiz.")
    await state.finish()
