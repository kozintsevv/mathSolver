import asyncio
import logging

from config_reader import config
from handlers import double_integrals, tasks, subjects, inputs, extrems

from aiogram import Bot, Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware


async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.callback_query.middleware(CallbackAnswerMiddleware())
    dp.include_routers(
        tasks.router,
        subjects.router,
        inputs.router,
        extrems.router,
        double_integrals.router,
    )

    logging.basicConfig(level=logging.INFO)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
