import asyncio
from schema.new_schema import DataForMessage
from telegram.run import bot


def create_message(items: list[DataForMessage]) -> str:
    msg = "Привет, эти предметы были проданы: \n"
    for item in items:
        msg += f"Название предмета: `{item.item_name}` \n"
        msg += f"Ссылка на трейд: `{item.trade_link}` \n"
    return msg


async def _send_messages(msg: str):
    await bot.send_message(286365412, msg, parse_mode="MARKDOWN")
    await asyncio.sleep(30)


def send_message(messages: str):
    asyncio.run(_send_messages(messages))