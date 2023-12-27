from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types


def get_task_ma() -> InlineKeyboardMarkup:
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Двойной интеграл по области", callback_data="double_integral"
            )
        ],
        [
            types.InlineKeyboardButton(
                text="Локальный экстремум", callback_data="extrem"
            )
        ],
        [
            types.InlineKeyboardButton(
                text="Найти область определения", callback_data="domain"
            )
        ],
        [types.InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_task_la() -> InlineKeyboardMarkup:
    buttons = [
        # [
        #     types.InlineKeyboardButton(
        #         text="Линейная комбинация", callback_data="linear_combination"
        #     )
        # ],
        [types.InlineKeyboardButton(text="Детерминант", callback_data="det")],
        [types.InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
