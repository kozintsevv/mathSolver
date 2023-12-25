from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from vsb_math.extrems import Extrems

from strings.ru import *

from states.input import Input


router = Router()


@router.message(Input.input_extrem)
async def send_extremes(message: Message, state: FSMContext):
    await message.answer_sticker(
        r"CAACAgIAAxkBAAJpOWWBnQpNP4BacSk_fc3Z2d5Xev1KAALUFAAC8i2ZSFHAjhpo6zLnMwQ"
    )

    extrem = Extrems(message.text)
    extrem.find_extrems()

    await message.answer(
        solved_extrem.format(
            derivate_x=extrem.deff_x,
            derivate_y=extrem.deff_y,
            roots=extrem.roots,
            derivate_x_x=extrem.deff_x_x,
            derivate_y_x=extrem.deff_y_x,
            derivate_y_y=extrem.deff_y_y,
            matrixes=extrem.matrixes,
        )
    )
    await find_points(message, extrem)

    await state.clear()


async def find_points(message: Message, extrem):
    index = 0
    for matrix in extrem.matrixes:
        delta2 = matrix[0] * matrix[3] - matrix[1] * matrix[2]
        delta1 = matrix[0]
        if delta2 > 0:
            await message.answer(
                local_min.format(min=extrem.roots[index])
            ) if delta1 > 0 else await message.anwser(
                local_max.format(max=extrem.roots[index])
            )
        elif delta2 < 0:
            await message.answer(no_extrem.format(no_extr=extrem.roots[index]))
        else:
            await message.answer(no_solution)
        index += 1
