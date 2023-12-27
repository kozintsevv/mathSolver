from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types


def get_subject_kb() -> InlineKeyboardMarkup:
    buttons = [
        [types.InlineKeyboardButton(text="Мат. Анализ", callback_data="ma")],
        [types.InlineKeyboardButton(text="Линейная алгебра", callback_data="la")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
