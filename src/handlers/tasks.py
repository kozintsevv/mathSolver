from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, callback_query
from aiogram.filters import StateFilter

from strings.ru import *

from keyboards.for_task import get_task_ma, get_task_la

from states.input import Input

from collections import deque


router = Router()

stack_deque = deque()


# @router.callback_query(Input.choosing_task,F.data == "ma")
@router.callback_query(Input.choosing_subject, F.data == "ma")
async def choose_task_ma(callback: callback_query, state: FSMContext):
    sent_message = await callback.message.edit_text(
        "Выбери задание:", reply_markup=get_task_ma()
    )

    await state.set_state(Input.choosing_task)

    stack_deque.appendleft(sent_message)


@router.callback_query(Input.choosing_subject, F.data == "la")
async def choose_task_la(callback: callback_query, state: FSMContext):
    sent_message = await callback.message.edit_text(
        "Выбери задание:", reply_markup=get_task_la()
    )

    await state.set_state(Input.choosing_task)

    stack_deque.appendleft(sent_message)


@router.callback_query(
    StateFilter(Input.input_double_integral, Input.input_extrem),
    F.data == "back",
)
async def to_task_state(callback: callback_query, state: FSMContext):
    if stack_deque:
        sent_message = stack_deque.popleft()
        await sent_message.delete()
    await state.set_state(Input.choosing_task)


@router.callback_query(
    StateFilter(Input.input_linear_combination),
    F.data == "back",
)
async def to_task_state(callback: callback_query, state: FSMContext):
    if stack_deque:
        sent_message = stack_deque.popleft()
        await sent_message.delete()
    await state.set_state(Input.choosing_task)


@router.callback_query(
    StateFilter(Input.domain),
    F.data == "back",
)
async def to_task_state(callback: callback_query, state: FSMContext):
    if stack_deque:
        sent_message = stack_deque.popleft()
        await sent_message.delete()
    await state.set_state(Input.choosing_task)


@router.callback_query(
    StateFilter(Input.det),
    F.data == "back",
)
async def to_task_state(callback: callback_query, state: FSMContext):
    if stack_deque:
        sent_message = stack_deque.popleft()
        await sent_message.delete()
    await state.set_state(Input.choosing_task)
