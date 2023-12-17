from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.for_exercises import get_exercise_kb

router = Router()


@router.message(Command('menu'))
async def keyboard_answer(message: Message):
    await message.answer(text='Choose exercise.', reply_markup=get_exercise_kb())


@router.message(F.text.lower() == "find local extrems")
async def local_extrems(message: Message):
    await message.reply("Введи функцию", reply_markup=ReplyKeyboardRemove())


@router.message()
async def answer(message: Message):
    await message.reply(f'test')


@router.message(F.text.lower() == "count double integral")
async def double_intregral(message: Message):
    await message.reply("Введи функцию", reply_markup=ReplyKeyboardRemove())
