from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def get_task_kb() -> InlineKeyboardBuilder:
    buttons={
        'double_integral':'Вычислить двойной интеграл по области',
        'extrem':'Найти локальный экстремумы'
    }
    kb = InlineKeyboardBuilder()
    for button_callback,button_text in buttons.items():
        kb.add(types.InlineKeyboardButton(
            text=button_text,
            callback_data=button_callback)
        )
    return kb.as_markup(resize_keyboard=True)
