from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, callback_query
from aiogram.fsm.context import FSMContext

from states.input import Input

from typing import Union

from keyboards.for_subject import get_subject_kb

from handlers.tasks import stack_deque


router = Router()


@router.callback_query(Input.choosing_task, F.data == "back")
@router.message(StateFilter(None), Command("menu"))
async def choose_subject(
    message: Union[Message, callback_query.CallbackQuery], state: FSMContext
):
    if isinstance(message, Message):
        await message.answer(text="Выбери предмет:", reply_markup=get_subject_kb())

    elif isinstance(message, callback_query.CallbackQuery):
        await message.message.edit_text(
            "Выбери предмет:", reply_markup=get_subject_kb()
        )

    await state.set_state(Input.choosing_subject)
