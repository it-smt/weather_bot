import asyncio
import os
import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram import Bot, Dispatcher

from bot.handlers.user_handlers import register_user_handlers
from bot.handlers.weather_handlers import register_weather_handlers


def register_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_weather_handlers(dp)


async def main() -> None:

    token = os.getenv('TG_API_TOKEN')
    bot = Bot(token=token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    logging.basicConfig(level=logging.INFO)

    register_handlers(dp)

    try:
        await dp.start_polling()
    except Exception as _ex:
        print(f'Ошибка: {_ex}')


if __name__ == '__main__':
    asyncio.run(main())
