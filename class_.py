from database import *
from mlogging import logger


class User:
    def __init__(self, nick: str, email: str, coins: int):
        self.nick = nick
        self.email = email
        self.coins = coins

    def get_balance(self) -> int:
        """
        Получение баланса из БД
        :return: int
        """
        try_create()
        return cursor.execute(f"SELECT coins FROM users WHERE email = '{self.email}'").fetchone()[0]

    def update_balance(self, delta: int) -> None:
        """
        Обновление в БД баланса на delta
        :param delta:
        :return:
        """
        try_create()
        current_balance = self.get_balance()
        cursor.execute(f"UPDATE users SET coins = '{current_balance + delta}' WHERE email = '{self.email}'")
        db.commit()
        logger.info("Balance updated succession")
