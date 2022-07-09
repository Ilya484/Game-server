from random import randint
from colorama import init, Fore

from src.class_ import User
from src.service_funcs import safe_input

init(autoreset=True)

__import__("guess_number")

_greeting = \
    """Добро пожаловать в игру \"Угадай число\"!
В режиме Лёгкая бот загадает число от 1 до 10, на отгадывание будет дано 3 попытки;
в режиме Средняя бот загадает число от 1 до 20, на отгадывание будет дано 3 попытки;
в режиме Сложная бот загадает число от 1 до 50, на отгадывание будет дано 3 попытки
Выбери режим:
[1] Лёгкая (без coins);
[2] Средняя (5 coins за вход и Вы получите 10 coins в случае победы);
[3] Сложная (5 coins за вход и Вы получите 20 coins в случае победы)
"""


def guess_number(user: User) -> None:
    print(Fore.GREEN + _greeting)

    while True:
        chapter = safe_input(Fore.YELLOW + "Введите цифру: ")
        match chapter:
            case "1":
                _easy(user)
                break
            case "2":
                _middle(user)
                break
            case "3":
                _hard(user)
                break
            case _:
                print(Fore.RED + "Такого варианта нет. Пожалуйста, выполните ввод снова!")
            

def _health(h: int) -> str:
    match h:
        case 0:
            return "попыток"
        case 1:
            return "попытку"
        case 2 | 3:
            return "попытки"


def remove_from_balance(call_func: str, user: User):
    """

    :param call_func:
    :param user:
    :return:
    """
    match call_func:
        case "m" | "h":
            user.update_balance(-5)
            print("Со счёта снято 5 coins!")


def _easy(user: User):
    print(f"{user.nick}, Вы попали в режим Лёгкая!")
    num = randint(1, 10)
    logic(num, 10, "e", user)


def _middle(user: User):
    if user.coins >= 5:
        print(f"{user.nick}, Вы попали в режим Средняя!")
        num = randint(1, 20)
        logic(num, 20, "m", user)
    else:
        print(f"Недостаточно средств!")


def _hard(user: User):
    if user.coins >= 5:
        print(f"{user.nick}, Вы попали в режим Сложная!")
        num = randint(1, 50)
        logic(num, 50, "h", user)
    else:
        print(f"Недостаточно средств!")


def logic(num: int, limit_high: int, call_func: str, user: User) -> None:
    """
    Логика игры

    :param int num:
    :param int limit_high:
    :param str call_func:
    :param User user:
    :return:
    """
    remove_from_balance(call_func, user)
    _range = range(1, limit_high + 1)

    health = 3
    while health:
        try:
            user_num = int(safe_input(f"Введите число от 1 до {limit_high}: "))
            if user_num not in _range:
                print(f"Введено число не от 1 до {limit_high}!")
            elif user_num == num:
                health_ = 3 - health + 1
                print(f"Поздравляю, {user.nick}! Вы угадали за {health_} {_health(health_)}")
                if call_func == "m":
                    user.update_balance(10)
                    print("Вам начислено 10 coins!")
                elif call_func == "h":
                    user.update_balance(20)
                    print("Вам начислено 20 coins!")
                break
                
            elif user_num > num:
                health -= 1
                print(f"Перелёт! Осталось {health} {_health(health)}")
            else:
                health -= 1
                print(f"Недолёт! Осталось {health} {_health(health)}")
        except ValueError:
            print(Fore.RED + "Введено не число!")
        
        if health == 0:
            print(f"Вы проиграли! Было загадано число {num}.")
