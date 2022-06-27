from database import *
from service_funcs import *
from crypto import encrypt
from mlogging import logger


class User:
    def __init__(self, nick=None, email=None, pas=''):
        self.nick = nick
        self.email = email
        self.pas = encrypt(pas)
        self.is_login = False
        try:
            self.coins = self.get_balance()
        except TypeError:
            self.coins = 0

    def get_balance(self) -> int:
        """
        Получение баланса из БД
        :return: int
        """
        return get_request("coins", {"email":self.email})[0]

    def update_balance(self, delta: int) -> None:
        """
        Обновление в БД баланса на delta
        :param delta: int
        :return: None
        """
        current_balance = self.get_balance()
        cursor.execute(f"UPDATE users SET coins = {current_balance + delta} WHERE email = '{self.email}'")
        db.commit()
        self.coins = current_balance + delta
        logger.info("Balance updated succession")

    def sign_in(self) -> None:
        """
        Регистрация пользователя
        :return: None
        """
        if not (self.email is None):
            cursor.execute(f"INSERT INTO users (nickname, email, password, coins) VALUES (?, ?, ?, ?)",
                           (self.nick, self.email, self.pas, 5))
            db.commit()
            return
        self.nick = safe_input("Введите ник: ")
        while True:
            self.email = safe_input("Введите email: ")
            if (e := get_request('email', {"email": self.email})) is None or e[0] != self.email:
                passwd = retry_input_pas()
                cursor.execute(f"INSERT INTO users (nickname, email, password, coins) VALUES (?, ?, ?, ?)",
                               (self.nick, self.email, passwd, 5))
                db.commit()
                del passwd
                del e
                print("Регистрация прошла успешно!")
                logger.info("User sign in succession")
                break
            else:
                print(Fore.RED + "Эта почта уже занята! Используйте другую")

    def sign_up(self) -> None:
        """
        Вход пользователя
        :return: None
        """
        if not (self.email is None):
            self.is_login = True
            return
        while True:
            self.email = safe_input("Введите email: ")
            passwd = encrypt(safe_input("Введите пароль: "))
            correct_email = get_request('email', {"email": self.email})[0]
            correct_passwd = get_request('password', {"email": self.email})[0]
            if self.email == correct_email and passwd == correct_passwd:
                self.nick = get_request('nickname', {"email": self.email})[0]
                print(f"Вход прошёл успешно! Привет, {self.nick}")
                logger.info("User sign up succession")
                self.is_login = True
                self.coins = get_request("coins", {"email": self.email})[0]
                return
            else:
                print(Fore.RED + "Неверный email и/или пароль!")
