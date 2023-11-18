from misc.loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import *
from static.kb import *
from data.db import *
from data.config import *
from data.texts import text_dict
from static.states import StorageText

@dp.message_handler(commands=['start'], state="*")
async def start(msg: Message, state: FSMContext):
    await state.finish()

    await msg.reply(text_dict['welcome'], reply_markup = main_menu, reply=False)


@dp.message_handler(text="📩 Написать Письмо", state="*")
async def text_handler(msg: Message, state: FSMContext):
    await state.finish()

    await msg.reply(text_dict['send_letter'], reply=False)
    await StorageText.text.set()

@dp.message_handler(state=StorageText.text)
async def letter_trigger(msg: Message, state: FSMContext):
    await state.update_data({
        "text": msg.text
    })
    
    await msg.reply(text_dict["is_anon"], reply_markup=anon_kb, reply=False)

@dp.callback_query_handler(text_startswith = "anon_", state = "*")
async def anon_checked(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data['text']
    is_anon = 1 if cb.data.split("_")[1] == "false" else 0
    
    r = await new_text(text, is_anon)
    await state.finish()

    await cb.message.reply(text_dict["anon_checked"], reply=False)

    for admin in admins:
        await bot.send_message(admin, text=f"➕ Новое письмо, <code>id: {r[0]}</code>", parse_mode='HTML')

@dp.message_handler(commands=["c"],state="*")
async def devv(msg: Message, state: FSMContext):
    for admin in admins:
        await bot.send_message(admin, text=f"➕ Новое письмо, <code>id: {msg.text}</code>", parse_mode='HTML')

