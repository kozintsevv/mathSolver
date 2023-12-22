from aiogram.filters import StateFilter
from aiogram.types import callback_query
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from strings.ru import *

from states.input import Input

from handlers.tasks import stack_deque


router = Router()


@router.callback_query(Input.choosing_task, F.data == "double_integral")
async def double_integral_input(callback: callback_query, state: FSMContext):
    sent_message = await callback.message.answer(
        "Введи функцию и интервалы(разделенные пробелом):"
    )
    stack_deque.appendleft(sent_message)
    await state.set_state(Input.input_double_integral)


@router.callback_query(Input.choosing_task, F.data == "extrem")
async def extrem_input(callback: callback_query, state: FSMContext):
    sent_message = await callback.message.answer("Введи функцию:")
    stack_deque.appendleft(sent_message)
    await state.set_state(Input.input_extrem)


@router.callback_query(Input.choosing_task, F.data == "linear_combination")
async def extrem_input(callback: callback_query, state: FSMContext):
    sent_message = await callback.message.answer("Введи векторы:")
    stack_deque.appendleft(sent_message)
    await state.set_state(Input.input_linear_combination)
