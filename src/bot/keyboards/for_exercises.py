from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_exercise_kb()->ReplyKeyboardMarkup:
    button_texts=['Count double integral','Find local extrems']
    kb=ReplyKeyboardBuilder()
    for button_text in button_texts:
        kb.button(text=button_text)
    kb.adjust(4)
    return kb.as_markup(resize_keyboard=True)
    