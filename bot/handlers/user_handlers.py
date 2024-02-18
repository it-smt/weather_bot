from aiogram import types, Dispatcher

from bot import db
from bot.keyboards.user_keyboard import get_main_kb


async def cmd_start(msg: types.Message) -> None:
    """Обработчик команды '/start'."""
    is_premium = False
    if msg.from_user.is_premium is not None:
        is_premium = True
    db.add_user(msg.from_user.id, msg.from_user.username, msg.from_user.full_name, msg.from_user.is_bot,
                is_premium, msg.from_user.language_code, msg.from_user.language_code)
    await msg.answer(text=f'Здравствуйте, {msg.from_user.username}!', reply_markup=get_main_kb())


async def cmd_help(msg: types.Message) -> None:
    text = ('Вот список всех команд бота:\n\n'
            '<b>Основные:</b>\n'
            '<b><i>/start</i></b> - начало работы с ботом\n'
            '<b><i>/help</i></b> - список всех команд бота\n'
            '<b><i>/weather</i></b> - погода в вашем городе\n')
    await msg.answer(text=text, parse_mode='HTML')


def register_user_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_help, commands=['help'])
