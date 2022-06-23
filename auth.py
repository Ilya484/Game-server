from crypto import encrypt
from database import *
from mlogging import *
from service_funcs import safe_input
from class_ import User

from colorama import init, Fore

init(autoreset=True)


def sign_in():
    """
    Регистрация пользователя
    :return:
    """
    nick = safe_input("Введите ник: ")
    try_create()
    cursor.execute(f"SELECT email FROM users WHERE nickname = '{nick}'")
    while True:
        email = safe_input("Введите email: ")
        if cursor.fetchone() != email:
            passwd = safe_input("Введите пароль: ")
            cursor.execute(f"INSERT INTO users (nickname, email, password, coins) VALUES (?, ?, ?, ?)",
                           (nick, encrypt(email), encrypt(passwd), 0))
            db.commit()
            print("Регистрация прошла успешно!")
            logger.info("User sign in succession")
            break
        else:
            print(Fore.RED + "Эта почта уже занята! Используйте другую")


def sign_up():
    """
    Вход пользователя
    :return:
    """
    while True:
        email = encrypt(safe_input("Введите email: "))
        passwd = encrypt(safe_input("Введите пароль: "))
        try_create()
        cursor.execute(f"SELECT email FROM users WHERE email = '{email}'")
        correct_email = cursor.fetchone()[0]
        cursor.execute(f"SELECT password FROM users WHERE email = '{email}'")
        correct_passwd = cursor.fetchone()[0]
        if email == correct_email and passwd == correct_passwd:
            cursor.execute(f"SELECT nickname FROM users WHERE email = '{email}'")
            name = cursor.fetchone()[0]
            print(f"Вход прошёл успешно! Привет, {name}")
            logger.info("User sign up succession")
            return
        else:
            print(Fore.RED + "Неверный email и/или пароль!")


def authentication() -> None:
    """
    Аутентификация пользователя
    :return: None
    """
    print("[1] Вход; [2] Регистрация")
    while True:
        try:
            digit = safe_input("Введите 1 или 2: ")
            match digit:
                case "1":
                    sign_up()
                    break
                case "2":
                    sign_in()
                    break
                case _:
                    print(Fore.RED + "Такого варианта нет. Пожалуйста, выполните ввод снова!")
        except ValueError:
            print(Fore.RED + "Ввод некорректный. Пожалуйста, выполните ввод снова!")
