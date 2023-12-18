from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove,callback_query

from keyboards.for_subject import get_subject_kb
from keyboards.for_task import get_task_kb



router = Router()


@router.message(Command('start'))
async def choose_subject(message: Message):
    await message.answer(text='Выбери предмет.', reply_markup=get_subject_kb())
    await message.answer_sticker(r"CAACAgIAAxkBAAJowmWAIKp4YuYZdsvZy3UQNpOFsIiyAAL6NQACMFKBSM1oUiZzBlLkMwQ")


@router.message(F.text.lower() == "ma2")
async def choose_task(message: Message):
    await message.reply("Выбери типа задания:", reply_markup=get_task_kb())

@router.callback_query(F.data=='double_integral')
async def calculate(callback:callback_query):
    await callback.message.answer('Введи функцию и интервалы:')
    
@router.message(F.text.lower() == "la")
async def answer(message: Message):
    await message.reply('Выбери типа задания.',reply_markup=ReplyKeyboardRemove())


@router.message(F.text.lower() == "count double integral")
async def double_intregral(message: Message):
    await message.reply("Введи функцию", reply_markup=ReplyKeyboardRemove())
