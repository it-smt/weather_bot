from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def change_city_name_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Сменить город'))

    return kb
