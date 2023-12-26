from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, callback_query
from aiogram.filters import StateFilter

from strings.ru import *

from keyboards.for_task import get_task_ma2, get_task_la

from states.input import Input

from collections import deque


router = Router()

stack_deque = deque()


@router.message(Input.choosing_task)
@router.message(Input.choosing_subject, F.text.lower() == "ma2")
async def choose_task_ma2(message: Message, state: FSMContext):
    disappearing = await message.answer(
        choice.format(subject=message.text),
        reply_markup=ReplyKeyboardRemove(),
    )
    await disappearing.delete()

    sent_message = await message.answer(
        f"Выбери тип задания по предмету MA2:",
        reply_markup=get_task_ma2(),
    )

    await state.set_state(Input.choosing_task)

    stack_deque.appendleft(sent_message)


@router.message(Input.choosing_subject, F.text.lower() == "la")
async def choose_task_la(message: Message, state: FSMContext):
    disappearing = await message.reply(
        choice.format(subject=message.text), reply_markup=ReplyKeyboardRemove()
    )
    await disappearing.delete()
    sent_message = await message.reply(
        f"Выбери типа задания по предмету {message.text}:",
        reply_markup=get_task_la(),
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
