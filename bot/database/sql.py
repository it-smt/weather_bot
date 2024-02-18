import sqlite3

from bot import settings


class DB:
    """Класс для работы с БД."""

    def __init__(self):
        """Инициализирует подключение к БД."""
        self.conn = sqlite3.connect(settings.DATABASE['NAME'])
        self.cursor = self.conn.cursor()

        self.create_table_users()

    def close(self):
        """Закрывает соединение с БД."""
        self.conn.close()

    def create_table_users(self):
        """Создает таблицу 'users'."""
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS `users` (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL UNIQUE,
                username VARCHAR(255) NOT NULL UNIQUE,
                full_name VARCHAR(255) NOT NULL,
                is_bot BOOLEAN NOT NULL DEFAULT false,
                is_premium BOOLEAN NOT NULL DEFAULT false,
                is_admin BOOLEAN NOT NULL DEFAULT false,
                language_code VARCHAR(10) NOT NULL,
                locale VARCHAR(10) NOT NULL,
                city_name VARCHAR(255)
            )"""
        )
        self.conn.commit()

    def add_user(self, user_id: int, username: str, full_name: str, is_bot: bool, is_premium: bool, language_code: str,
                 locale: str):
        """Добавляет пользователя, если его еще нет."""
        if self.get_user(user_id) is None:
            self.cursor.execute(
                """INSERT INTO `users` (
                    `user_id`, 
                    `username`, 
                    `full_name`, 
                    `is_bot`, 
                    `is_premium`, 
                    `language_code`, 
                    `locale`
                ) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (user_id, username, full_name, is_bot, is_premium, language_code, locale)
            )
            self.conn.commit()

    def get_user(self, user_id: int):
        """Проверяет, есть ли пользователь в БД."""
        user = self.cursor.execute(
            """SELECT * FROM `users` WHERE `user_id` = ?""",
            (user_id,)
        )
        return user.fetchone()

    def is_city_name_exist(self, user_id: int):
        """Проверяет, заполнено ли поле 'city_name'."""
        city_name = self.cursor.execute(
            """SELECT `city_name` FROM `users` WHERE `user_id` = ?""",
            (user_id,)
        )
        return city_name.fetchone() is not None

    def get_city_name(self, user_id: int):
        """Возвращает 'city_name' из БД."""
        city_name = self.cursor.execute(
            """SELECT `city_name` FROM `users` WHERE `user_id` = ?""",
            (user_id,)
        )
        return city_name.fetchone()[0]

    def set_city_name(self, user_id: int, city_name: str):
        self.cursor.execute(
            """UPDATE users SET city_name = ? WHERE user_id = ?""",
            (city_name, user_id)
        )
        self.conn.commit()
