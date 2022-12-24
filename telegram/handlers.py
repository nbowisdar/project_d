from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text, Command
from telegram.keyboards import stop_btn
from telegram.messages import all_messages
import asyncio

main_router = Router()
IS_WORKING = False


@main_router.message(Command(commands="start"))
async def test(message: Message):
    global IS_WORKING
    if not IS_WORKING:
        IS_WORKING = True
        await pulling_messages(message)
        await message.answer("Бот запущен!", reply_markup=stop_btn)
    else:
        await message.reply("Кто-то уже запустил бота!")


async def pulling_messages(message: Message):
    if not IS_WORKING:
        return
    for msg in all_messages:
        await message.answer(msg, parse_mode="MARKDOWN")
    await asyncio.sleep(30)


@main_router.message(Text(text="Стоп"))
async def stop_pulling(message: Message):
    global IS_WORKING
    IS_WORKING = False
    await message.reply("Бот остановлен!")