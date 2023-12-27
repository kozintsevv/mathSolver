import asyncio
import logging

from config_reader import config
from handlers import (
    instructions,
    double_integrals,
    tasks,
    subjects,
    inputs,
    extrems,
    linear_combination,
    domain,
    det,
)

from aiogram import Bot, Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from db import BotDB

BotDB = BotDB("tg.db")


async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.callback_query.middleware(CallbackAnswerMiddleware())
    dp.include_routers(
        instructions.router,
        tasks.router,
        subjects.router,
        inputs.router,
        extrems.router,
        double_integrals.router,
        linear_combination.router,
        domain.router,
        det.router,
    )

    logging.basicConfig(level=logging.INFO)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
