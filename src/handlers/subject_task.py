from aiogram import Router, F
from aiogram.filters import Command,StateFilter
from aiogram.types import Message, ReplyKeyboardRemove,callback_query
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from vsb_math.extrems import Extrems
from vsb_math.double_integral import DoubleIntegral
from strings.ru import *
 
from keyboards.for_subject import get_subject_kb
from keyboards.for_task import get_task_kb

class SolveTask(StatesGroup):
    choosing_subject = State()
    choosing_task = State()
    input_extrem=State()
    input_double_integral=State()

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
    await callback.message.answer('Введи функцию и интервалы(разделенные пробелом):')
    await state.set_state(SolveTask.input_double_integral)

@router.callback_query(SolveTask.choosing_task,F.data=='extrem')
async def extrem_input(callback:callback_query,state:FSMContext):
    await callback.message.answer('Введи функцию:')
    await state.set_state(SolveTask.input_extrem)

@router.message(SolveTask.choosing_task)
async def incorrect_task(message: Message):
    await message.answer(
        text="Выбери задание из списка:",
        reply_markup=get_task_kb()
    )

@router.message(SolveTask.input_extrem)
async def extrem_output(message:Message,state:FSMContext):
    await message.answer_sticker(r'CAACAgIAAxkBAAJpOWWBnQpNP4BacSk_fc3Z2d5Xev1KAALUFAAC8i2ZSFHAjhpo6zLnMwQ')
    extrem=Extrems(message.text)
    extrem.find_extrems()
    await message.answer(solved_extrem.format(
        derivate_x=extrem.deff_x,
        derivate_y=extrem.deff_y,
        roots=extrem.roots,
        derivate_x_x=extrem.deff_x_x,
        derivate_y_x=extrem.deff_y_x,
        derivate_y_y=extrem.deff_y_y,
        matrixes=extrem.matrixes
        ))
    await validate_extrem(message,extrem)
    
    await state.clear()

@router.message(SolveTask.input_double_integral)
async def extrem_output(message:Message,state:FSMContext):
    await message.answer_sticker(r'CAACAgIAAxkBAAJpOWWBnQpNP4BacSk_fc3Z2d5Xev1KAALUFAAC8i2ZSFHAjhpo6zLnMwQ')
    args=validate_double_integral(message.text)
    double_integral=DoubleIntegral(args[0],args[1],args[2])
    double_integral.calculate()
    await message.answer(solved_double_integral.format(
        integrate_y=double_integral.integrate_y,
        upper_sub_y=double_integral.upper_sub_y,
        lower_sub_y=double_integral.lower_sub_y,
        difference_y=double_integral.subtract_y,
        integrate_x=double_integral.integrate_x,
        upper_sub_x=double_integral.upper_sub_x,
        lower_sub_x=double_integral.lower_sub_x,
        difference_x=double_integral.subtract_x
    ))
    await state.clear()

def validate_double_integral(str):
    return str.split()

async def validate_extrem(message:Message,extrem):
    index = 0
    for matrix in extrem.matrixes:
        delta2 = matrix[0] * matrix[3] - matrix[1] * matrix[2]
        delta1 = matrix[0]
        if delta2 > 0:
            await message.answer(local_min.format(min=extrem.roots[index])) if delta1>0 else await message.anwser(local_max.format(max=extrem.roots[index]))
        elif delta2 < 0:
            await message.answer(no_extrem.format(no_extr=extrem.roots[index]))
        else:
            await message.answer(no_solution)
        index += 1  
    

