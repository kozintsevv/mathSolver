from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from vsb_math.double_integral import DoubleIntegral

from strings.ru import *

from states.input import Input

from handlers.tasks import stack_deque


router = Router()


def parse_double_integral(str):
    return str.split()


@router.message(Input.input_double_integral)
async def send_double_integral(message: Message, state: FSMContext):
    await message.answer_sticker(
        r"CAACAgIAAxkBAAJpOWWBnQpNP4BacSk_fc3Z2d5Xev1KAALUFAAC8i2ZSFHAjhpo6zLnMwQ"
    )
    args = parse_double_integral(message.text)
    double_integral = DoubleIntegral(args[0], args[1], args[2])
    double_integral.calculate()
    await message.answer(
        solved_double_integral.format(
            integrate_y=double_integral.integrate_y,
            upper_sub_y=double_integral.upper_sub_y,
            lower_sub_y=double_integral.lower_sub_y,
            difference_y=double_integral.subtract_y,
            integrate_x=double_integral.integrate_x,
            upper_sub_x=double_integral.upper_sub_x,
            lower_sub_x=double_integral.lower_sub_x,
            difference_x=double_integral.subtract_x,
        )
    )
    await state.clear()
