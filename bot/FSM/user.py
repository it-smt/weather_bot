from aiogram.dispatcher.filters.state import StatesGroup, State


class CityName(StatesGroup):
    waiting_for_city_name = State()
