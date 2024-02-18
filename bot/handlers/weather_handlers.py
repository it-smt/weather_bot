from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from bot import db, weather
from bot.FSM.user import CityName
from bot.keyboards.weather_keyboards import change_city_name_keyboard


async def cmd_weather(msg: types.Message, state: FSMContext):
    is_city_name = db.is_city_name_exist(msg.from_user.id)
    weather.set_city_name(db.get_city_name(msg.from_user.id))
    if not is_city_name:
        await msg.answer(text='Введите название города')
        await state.set_state(CityName.waiting_for_city_name.state)
    else:
        text = weather.get_formatted_weather_data()
        await msg.answer(text=text)


async def city_name(msg: types.Message, state: FSMContext):
    db.set_city_name(msg.from_user.id, msg.text.capitalize())
    await msg.answer(f'Город, который вы установили: {msg.text.capitalize()}', reply_markup=change_city_name_keyboard())
    await state.finish()


async def any_text(msg: types.Message, state: FSMContext):
    if msg.text == 'Сменить город':
        await state.set_state(CityName.waiting_for_city_name.state)
        await msg.answer(text='Введите название города')


def register_weather_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_weather, commands=['weather'], state='*')
    dp.register_message_handler(city_name, state=CityName.waiting_for_city_name)
    dp.register_message_handler(any_text, content_types=types.ContentType.TEXT, state='*')
