from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/help'))

    return kb
