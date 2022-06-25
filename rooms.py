from class_ import User
from colorama import init, Fore
from tabulate import tabulate
from auth import *

init(autoreset=True)


def game_menu(user: User) -> None:
    """
    Меню авторизованного пользователя
    :param user: User
    :return: None
    """
    print("Меню:\n[1] Личный кабинет; [2] Список игр")
    while True:
        chapter = safe_input("Введите цифру: ")
        match chapter:
            case "1":
                personal_account(user)
                return


def main_menu(user: User) -> None:
    """
    Главное меню игры
    :param user: User
    :return: None
    """
    print(Fore.RED + "Добро пожаловать в Game Server!\n", "Для начала нужно выполнить вход или зарегистрироваться!",
          sep='')
    print("[1] Вход; [2] Регистрация")
    while True:
        digit = safe_input("Введите 1 или 2: ")
        match digit:
            case "1":
                user.sign_up()
                break
            case "2":
                user.sign_in()
                print("Для продолжения нужно совершить вход!")
                user.sign_up()
                break
            case _:
                print(Fore.RED + "Такого варианта нет. Пожалуйста, выполните ввод снова!")


def personal_account(user: User) -> None:
    """
    Личный кабинет
    :param user: User
    :return: None
    """
    print("Личный кабинет")
    headers = ("Ник", "Почта", "Coins")
    data = [(user.nick, user.email, f"{user.coins}")]
    print(tabulate(data, headers=headers))
