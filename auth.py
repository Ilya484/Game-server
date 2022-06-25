from crypto import encrypt
from database import *
from mlogging import *
from service_funcs import safe_input, get_request
# from class_ import User

from colorama import init, Fore

init(autoreset=True)



def authentication() -> None:
    """
    Аутентификация пользователя
    :return: None
    """
    print("[1] Вход; [2] Регистрация")
    while True:
        digit = safe_input("Введите 1 или 2: ")
        match digit:
            case "1":
                return sign_up()
            case "2":
                return sign_in()
            case _:
                print(Fore.RED + "Такого варианта нет. Пожалуйста, выполните ввод снова!")
