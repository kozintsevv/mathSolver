from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from vsb_math.linear_algebra import LinearAlgebra

from strings.ru import *

from states.input import Input

from handlers.tasks import stack_deque

from sympy import sympify, Matrix

router = Router()


@router.message(Input.det)
async def send_det(message: Message, state: FSMContext):
    await message.answer_sticker(
        r"CAACAgIAAxkBAAJpOWWBnQpNP4BacSk_fc3Z2d5Xev1KAALUFAAC8i2ZSFHAjhpo6zLnMwQ"
    )
    matrix = LinearAlgebra()
    matrix.det_laplace(Matrix(list(sympify(message.text))))

    with_mat_strings = matrix.with_matrix.split("|")
    sum_diagonals_strings = matrix.sum_diagonals.split("|")
    sub_strings = matrix.sub.split("|")

    last_string = ""

    for i in range(len(with_mat_strings) - 1):
        await message.answer(with_mat_strings[i])
    for i in range(len(sum_diagonals_strings) - 1):
        await message.answer(sum_diagonals_strings[i])
    for i in range(len(sub_strings) - 1):
        last_string += f"+ {sub_strings[i]}"

    if last_string:
        await message.answer(last_string)
    if matrix.sum:
        await message.answer(f"Ответ : {matrix.sum}")

    await state.clear()
