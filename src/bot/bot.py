import asyncio
import logging

from config_reader import config
from handlers import exercises

from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_routers(exercises.router)

    logging.basicConfig(level=logging.INFO)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
