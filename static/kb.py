from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton \
						, ReplyKeyboardMarkup
from data.config import admins


main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add("📩 Написать Письмо")
anon_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("🟢 Да", callback_data="anon_true"),InlineKeyboardButton("🔴 Нет", callback_data="anon_false"))