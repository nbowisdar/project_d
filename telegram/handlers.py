from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text, Command
# from telegram.keyboards import stop_btn, main_kb
#from telegram.messages import all_messages, pulling_messages
#from mains.main import all_messages
# import asyncio

main_router = Router()
#IS_WORKING = False

@main_router.message(Command(commands="start"))
async def start(message: Message):
    await message.answer("Привет, у этого бота нет команд, он запускаеться автоматически вместе со скриптом!")


# @main_router.message(Text(text='Старт'))
# @main_router.message(Command(commands="start"))
# async def test(message: Message):
#     global IS_WORKING
#     if not IS_WORKING:
#         IS_WORKING = True
#         await message.answer("Бот запущен!", reply_markup=stop_btn)
#         #await pulling_messages(message)
#     else:
#         await message.reply("Кто-то уже запустил бота!")
#
#
# @main_router.message(Text(text="Стоп"))
# async def stop_pulling(message: Message):
#     global IS_WORKING
#     IS_WORKING = False
#     await message.reply("Бот остановлен!", reply_markup=main_kb)