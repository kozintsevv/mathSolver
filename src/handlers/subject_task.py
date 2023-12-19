from aiogram import Router, F
from aiogram.filters import Command,StateFilter
from aiogram.types import Message, ReplyKeyboardRemove,callback_query
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from vsb_math.extrems import Extrems
from strings.ru import solved_extrem
 
from keyboards.for_subject import get_subject_kb
from keyboards.for_task import get_task_kb

class SolveTask(StatesGroup):
    choosing_subject = State()
    choosing_task = State()
    input_task=State()

router = Router()

@router.message(StateFilter(None),Command('menu'))
async def choose_subject(message: Message,state:FSMContext):
    await message.answer(text='Выбери предмет.', reply_markup=get_subject_kb())
    await message.answer_sticker(r"CAACAgIAAxkBAAJowmWAIKp4YuYZdsvZy3UQNpOFsIiyAAL6NQACMFKBSM1oUiZzBlLkMwQ")
    await state.set_state(SolveTask.choosing_subject)


@router.message(SolveTask.choosing_subject,F.text.lower() == "ma2")
async def choose_task_ma2(message: Message,state:FSMContext):
    await state.update_data(chosen_subject=message.text.lower())
    await message.reply(f'Выбери типа задания по предмету {message.text}:', reply_markup=get_task_kb())
    await state.set_state(SolveTask.choosing_task)

@router.message(SolveTask.choosing_subject,F.text.lower() == "la")
async def choose_task_la(message: Message,state:FSMContext):
    await state.update_data(chosen_subject=message.text)
    await message.reply(f'Выбери типа задания по предмету {message.text}:',reply_markup=ReplyKeyboardRemove())
    await state.set_state(SolveTask.choosing_task)

@router.message(SolveTask.choosing_subject)
async def incorrect_subject(message: Message):
    await message.answer(
        text="Выбери предмет из списка:",
        reply_markup=get_subject_kb()
    )

@router.callback_query(SolveTask.choosing_task,F.data=='double_integral')
async def double_integral_input(callback:callback_query,state:FSMContext):
    await callback.message.answer('Введи функцию и интервалы:')
    await state.set_state(SolveTask.input_task)

@router.callback_query(SolveTask.choosing_task,F.data=='extrem')
async def extrem_input(callback:callback_query,state:FSMContext):
    await callback.message.answer('Введи функцию:')
    await state.set_state(SolveTask.input_task)

@router.message(SolveTask.choosing_task)
async def incorrect_task(message: Message):
    await message.answer(
        text="Выбери задание из списка:",
        reply_markup=get_task_kb()
    )

@router.message(SolveTask.input_task)
async def extrem_output(message:Message,state:FSMContext):
    await message.answer_sticker(r'CAACAgIAAxkBAAJpOWWBnQpNP4BacSk_fc3Z2d5Xev1KAALUFAAC8i2ZSFHAjhpo6zLnMwQ')
    extrem=Extrems(message.text)
    extrem.find_extrems()
    await message.answer(solved_extrem)
    await state.clear()

    

