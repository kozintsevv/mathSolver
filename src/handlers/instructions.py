from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

from bot import BotDB
from states.input import Input


router = Router()


@router.message(StateFilter(None, Input.choosing_subject), Command("start"))
async def send_instructions(message: Message, state: FSMContext):
    await message.answer(
        "<b>Двойной интеграл.</b>\nВведи формулу, и два интервала, сначала для <code>x</code> , потом для <code>y</code> (интервалы должны быть заключены в круглые скобки). Формула и интервалы должны быть разделены пробелами.\n<b>Задание:</b>",
        parse_mode=ParseMode.HTML,
        reply_markup=ReplyKeyboardRemove(),
    )
    double_integral = FSInputFile("instructions_images/double_integral.jpg")
    await message.answer_photo(double_integral)
    await message.answer(
        "<b>Ввод:</b> \n<code>x**2+y (0,2) (1,3)</code>", parse_mode=ParseMode.HTML
    )

    await message.answer(
        "<b>Локальные экстремумы.</b>\n<b>Задание:</b>", parse_mode=ParseMode.HTML
    )
    extrems = FSInputFile("instructions_images/extrems.jpg")
    await message.answer_photo(extrems)
    await message.answer(
        "<b>Ввод:</b> \n<code>3*x**2+y**3-6*x*y-9*y+2</code>", parse_mode=ParseMode.HTML
    )

    await message.answer(
        "<b>Найти область определения.</b>\n<b>Задание:</b>", parse_mode=ParseMode.HTML
    )
    domen = FSInputFile("instructions_images/domen.jpg")
    await message.answer_photo(domen)
    await message.answer(
        "<b>Ввод:</b>\n <code>sqrt((x**2+y**2-x)/(2*x-x**2-y**2))</code>\n<code>log(x+y,10)</code>\n<code>asin(x/y**2)+acos(1-y)</code>",
        parse_mode=ParseMode.HTML,
    )

    await message.answer(
        "<b>Детерминант | Обратная матрица.</b>\n<b>Задание:</b>",
        parse_mode=ParseMode.HTML,
    )
    det = FSInputFile("instructions_images/det.jpg")
    await message.answer_photo(det)
    await message.answer(
        "<b>Ввод:</b>\n <code>[2,0,3,-1],[0,-1,0,1],[1,2,3,2],[-1,3,-1,0]</code>",
        parse_mode=ParseMode.HTML,
    )

    if not BotDB.user_exists(message.from_user.id):
        BotDB.add_user(
            message.from_user.id,
            message.from_user.username if message.from_user.username else "no_nickname",
        )

    await state.clear()
