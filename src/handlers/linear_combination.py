from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from vsb_math.linear_algebra import LinearCombination

from strings.ru import *

from states.input import Input

from handlers.tasks import stack_deque

router = Router()


@router.message(Input.input_linear_combination)
async def send_linear_combination(message: Message, state: FSMContext):
    await message.answer_sticker(
        r"CAACAgIAAxkBAAJpOWWBnQpNP4BacSk_fc3Z2d5Xev1KAALUFAAC8i2ZSFHAjhpo6zLnMwQ"
    )
    split = message.text.split(" ")
    lin_combination = LinearCombination(split[0], split[1])
    lin_combination.calculate()
    await message.answer(str(lin_combination.roots))

    await state.clear()
