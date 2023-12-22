from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, callback_query
from aiogram.fsm.context import FSMContext

from states.input import Input

from typing import Union

from keyboards.for_subject import get_subject_kb

from handlers.tasks import stack_deque


router = Router()


@router.message(Input.choosing_subject)
@router.callback_query(Input.choosing_task, F.data == "back")
@router.message(StateFilter(None), Command("menu"))  # 1)Выбор предмета
async def choose_subject(
    message: Union[Message, callback_query.CallbackQuery], state: FSMContext
):
    if isinstance(message, Message):
        await message.answer(text="Выбери предмет.", reply_markup=get_subject_kb())
        await message.answer_sticker(
            r"CAACAgIAAxkBAAJowmWAIKp4YuYZdsvZy3UQNpOFsIiyAAL6NQACMFKBSM1oUiZzBlLkMwQ"
        )

    elif isinstance(message, callback_query.CallbackQuery):
        if stack_deque:
            sent_message = stack_deque.popleft()
            await sent_message.delete()

        await message.message.answer(
            text="Выбери предмет.", reply_markup=get_subject_kb()
        )

        await message.message.answer_sticker(
            r"CAACAgIAAxkBAAJowmWAIKp4YuYZdsvZy3UQNpOFsIiyAAL6NQACMFKBSM1oUiZzBlLkMwQ"
        )

    await state.set_state(Input.choosing_subject)
