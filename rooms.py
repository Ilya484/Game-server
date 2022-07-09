from os import system

from src.class_ import User
from colorama import init, Fore
from tabulate import tabulate
from src.service_funcs import safe_input, back_to
from minigames.guess_a_number import guess_number

init(autoreset=True)


def game_list(user: User) -> None:
    """
    Список игр
    :param user: User
    :return: None
    """
    print("Список игр:\n[1] Угадай число; [2] Вернуться в меню")
    while True:
        chapter = safe_input("Введите цифру: ")
        match chapter:
            case "1":
                system("cls")
                guess_number(user)
                return
            case "2":
                system("cls")
                back_to(game_list, (user, ), menu_of_auth_user, (user, ))
                return
            case _:
                print(Fore.RED + "Такого варианта нет. Пожалуйста, выполните ввод снова!")

def menu_of_auth_user(user: User) -> None:
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
                system("cls")
                personal_account(user)
                return
            case "2":
                system("cls")
                game_list(user)
                return
            case _:
                print(Fore.RED + "Такого варианта нет. Пожалуйста, выполните ввод снова!")


def main_menu(user: User) -> None:
    """
    Главное меню игры
    :param user: User
    :return: None
    """
    print(Fore.RED + "Добро пожаловать в Game Server!\nДля начала нужно выполнить вход или зарегистрироваться!")
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
    back_to(personal_account, (user, ), menu_of_auth_user, (user,))