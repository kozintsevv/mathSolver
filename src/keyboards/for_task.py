from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types


def get_task_kb() -> InlineKeyboardMarkup:
    buttons = [
        [types.InlineKeyboardButton(text='Двойной интеграл по области', callback_data='double_integral')],
        [types.InlineKeyboardButton(text='Локальный экстремум', callback_data='extrem')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard
