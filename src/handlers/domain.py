from vsb_math.graphics import draw_domain

from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from states.input import Input


router = Router()


@router.message(Input.domain)
async def send_domain(message: Message, state: FSMContext):
    from bot import BotDB

    BotDB.increment_action(
        message.from_user.id,
    )
    await message.answer_sticker(
        r"CAACAgIAAxkBAAJpOWWBnQpNP4BacSk_fc3Z2d5Xev1KAALUFAAC8i2ZSFHAjhpo6zLnMwQ"
    )

    draw_domain(message.text)
    domain = FSInputFile("graphics_output/xy_projection.png")
    await message.answer_photo(domain)
    await state.clear()
