import os

import requests


class WeatherService:
    """Класс для работы с сервисом погоды."""

    def __init__(self) -> None:
        """Инициализация."""
        self.OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')
        self.city = ''
        self.url = f'https://api.openweathermap.org/data/2.5/weather'
        self.descriptions = None
        self.temp = None
        self.temp_feels_like = None
        self.temp_min = None
        self.temp_max = None
        self.humidity = None
        self.wind_speed = None
        self.resp_city_name = None

    def set_city_name(self, new_city_name: str):
        self.city = new_city_name

    def get_weather_data(self) -> dict:
        """Получает json с данными."""
        print(self.city)
        params = {
            'q': self.city.capitalize(),
            'appid': self.OPEN_WEATHER_API_KEY,
            'units': 'metric',
            'lang': 'ru',
        }
        resp = requests.get(self.url, params=params).json()
        return resp

    def get_formatted_weather_data(self) -> str:
        try:
            data = self.get_weather_data()
            print(data)
            self.descriptions = []
            for item in data['weather']:
                self.descriptions.append(item['description'])
            self.temp = round(data['main']['temp'])
            self.temp_feels_like = round(data['main']['feels_like'])
            self.temp_min = round(data['main']['temp_min'])
            self.temp_max = round(data['main']['temp_max'])
            self.humidity = round(data['main']['humidity'])
            self.wind_speed = round(data['wind']['speed'])
            self.resp_city_name = data['name']

            formatted_text = (f'Погода в городе {self.resp_city_name}:\n\n'
                              f'{", ".join(self.descriptions)}\n\n'
                              f'Температура: {self.temp}°C\n'
                              f'Комфорт: {self.temp_feels_like}°C\n'
                              f'Минимальная: {self.temp_min}°C\n'
                              f'Максимальная: {self.temp_max}°C\n'
                              f'Влажность: {self.humidity}%\n'
                              f'Скорость ветра: {self.wind_speed} м/c\n')
        except Exception as _ex:
            formatted_text = 'Упс... Что-то пошло не так.'

        return formatted_text
