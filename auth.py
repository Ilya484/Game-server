from database import *
from colorama import init, Fore

init(autoreset=True)


def safe_input(greetting):
    while True:
        s = input(greetting).strip()
        if all(sub not in s for sub in r"'\"\\,"):
            return s
        print(Fore.RED + "Ник содержит недопустимые символы. Пожалуйста, выполните ввод снова!")



def sign_in():
    """
    Регистрация пользователя
    :return:
    """
    while True:
        nick = safe_input("Введите ник: ")
        try_create()
        cursor.execute(f"SELECT nickname FROM users WHERE nickname = '{nick}'")
        if cursor.fetchone() is None:
            login = safe_input("Введите логин: ")
            pswd = safe_input("Введите пароль: ")
            cursor.execute(f"INSERT INTO users (nickname, login, password) VALUES (?, ?, ?)",
                               (nick, login, pswd))
            db.commit()
            print("Регистрация прошла успешно!")
            break
        else:
            print(Fore.RED + "Этот ник занят! Используйте другой")



def authentication() -> None:
    """
    Аутентификация пользователя
    :return:
    """
    while True:
        print("[1] Вход; [2] Регистрация\nВведите 1 или 2: ", end='')
        try:
            digit = int(input())
            match digit:
                case 1:
                    break
                case 2:
                    sign_in()
                    break
                case _:
                    print(Fore.RED + "Такого варианта нет. Пожалуйста, выполните ввод снова!")
        except ValueError:
            print(Fore.RED + "Ввод некорректный. Пожалуйста, выполните ввод снова!")
