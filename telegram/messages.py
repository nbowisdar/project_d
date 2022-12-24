from schema.new_schema import DataForMessage

all_messages = []


def _build_sold_items(items: list[DataForMessage]) -> str:
    msg = "Привет, эти предметы были проданы: \n"
    for item in items:
        msg += f"Название предмета: `{item.item_name}` \n"
        msg += f"Ссылка на трейд: `{item.trade_link}` \n"
    return msg


def add_message(items: list[DataForMessage]):
    all_messages.append(
        _build_sold_items(items)
    )

