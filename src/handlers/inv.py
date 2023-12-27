from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from vsb_math.linear_algebra import invert_matrix

from strings.ru import *

from states.input import Input

from handlers.tasks import stack_deque


router = Router()


@router.message(Input.inv)
async def send_inv(message: Message, state: FSMContext):
    from bot import BotDB

    BotDB.increment_action(
        message.from_user.id,
    )
    await message.answer_sticker(
        r"CAACAgIAAxkBAAJpOWWBnQpNP4BacSk_fc3Z2d5Xev1KAALUFAAC8i2ZSFHAjhpo6zLnMwQ"
    )
    await invert_matrix(message)

    await state.clear()
