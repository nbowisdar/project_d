from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

stop_btn = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Стоп")]],
    resize_keyboard=True
)


main_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Старт")]],
    resize_keyboard=True
)