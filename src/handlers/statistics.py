from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, callback_query


router = Router()


@router.message(Command("admin"))
async def choose_subject(message: Message):
    from bot import BotDB

    if message.from_user.id == 394943158:
        result = BotDB.get_statistic()
        for user in result:
            await message.answer(f"{user}")
