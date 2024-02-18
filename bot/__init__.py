from dotenv import load_dotenv

from bot.database.sql import DB
from bot.services.open_weather import WeatherService

load_dotenv()

db = DB()

weather = WeatherService()
