from telegram.handlers import main_router
import asyncio
from aiogram import Bot, Dispatcher

TOKEN = "5699483594:AAFFwC758bmMioThvKXgtLjPTaOHlx1xwlI"

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def start():
    dp.include_router(main_router)
    await dp.start_polling(bot)


def start_tg_bot():
    asyncio.run(start())