from colorama import init, Fore
from auth import *

init(autoreset=True)


def main_menu() -> None:
    """
    Главное меню игры
    :return:None
    """
    print(Fore.RED + "Добро пожаловать в Game Server!\n", "Для начала нужно выполнить вход или зарегистрироваться!", sep='')
    authentication()