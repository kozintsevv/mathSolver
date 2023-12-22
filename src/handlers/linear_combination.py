from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from vsb_math.linear_combination import LinearCombination

from strings.ru import *

from states.input import Input

from handlers.tasks import stack_deque

router = Router()


@router.message(Input.input_extrem)
async def send_extremes(message: Message, state: FSMContext):
    await message.answer_sticker(
        r"CAACAgIAAxkBAAJpOWWBnQpNP4BacSk_fc3Z2d5Xev1KAALUFAAC8i2ZSFHAjhpo6zLnMwQ"
    )

    # vectors = Extrems(message.text)
    # extrem.find_extrems()

    # await message.answer(
    #     solved_extrem.format(
    #         derivate_x=extrem.deff_x,
    #         derivate_y=extrem.deff_y,
    #         roots=extrem.roots,
    #         derivate_x_x=extrem.deff_x_x,
    #         derivate_y_x=extrem.deff_y_x,
    #         derivate_y_y=extrem.deff_y_y,
    #         matrixes=extrem.matrixes,
    #     )
    # )
    # await find_points(message, extrem)

    await state.clear()
