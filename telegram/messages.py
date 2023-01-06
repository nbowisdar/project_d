import asyncio
from schema.new_schema import DataForMessage
from telegram.runer_tg import bot


def create_message(items: list[DataForMessage]) -> str:
    msg = f"Привет, всего проданно предметов - {len(items)}\n"
    if not items:
        msg += "Нет ссылок на трейд :("
        return msg
    for item in items:
        if not item.trade_link:
            continue
        msg += f"Название предмета: `{item.item_name}` \n"
        msg += f"Ссылка на трейд: `{item.trade_link}` \n"
    return msg


async def _send_messages(msg: str, telegram_users: list[int]):
    for telegram_id in telegram_users:
        await bot.send_message(telegram_id, msg, parse_mode="MARKDOWN")
    await asyncio.sleep(30)


def send_message(messages: str, telegram_users: list[int]):
    asyncio.run(_send_messages(messages, telegram_users))
