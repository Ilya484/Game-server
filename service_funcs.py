from customs_types import function

from colorama import init, Fore
from database import cursor
from crypto import encrypt

init(autoreset=True)


def safe_input(greeting: str) -> str:
    """
    Безопасный ввод
    :param greeting: str
    :return: str
    """
    while True:
        s = input(greeting).strip()
        if s and all(sub not in s for sub in r"'\"\\,"):
            return s
        print(Fore.RED + "Строка содержит недопустимые символы. Пожалуйста, выполните ввод снова!")


def retry_input_pas() -> str:
    """
    Ввод пароля с повтором
    :return: str
    """
    while True:
        pas = safe_input("Введите пароль: ")
        retry_pas = safe_input("Повторите пароль: ")
        if pas == retry_pas:
            return encrypt(pas)
        else:
            print(Fore.RED + "Пароли не совпадают. Пожалуйста, выполните ввод снова!")


def get_request(field: str, expresion: dict, table: str = "users"):
    strings_of_exp = []
    for k, v in expresion.items():
        if isinstance(v, int):
            strings_of_exp.append(f"{k} = {v}")
        else:
            strings_of_exp.append(f"{k} = '{v}'")
    cursor.execute(f"SELECT {field} FROM {table} WHERE {' AND '.join(strings_of_exp)}")
    return cursor.fetchone()


def back_to(cur_func: function, params_of_cur_func: tuple, back_func: function, params_of_back_func: tuple) -> None:
    """
    Навигация назад
    :param cur_func: function
    :param params_of_cur_func: tuple
    :param back_func: function
    :param params_of_back_func: tuple
    :return: None
    """
    while True:
        sog = safe_input("Вы точно хотите вернуться? [Y/д] [N/н]").lower()
        match sog:
            case "y" | "д":
                back_func(*params_of_back_func)
                break
            case "n" | "н":
                cur_func(*params_of_cur_func)
                break
            case _:
                print(Fore.RED + "Такого варианта нет. Пожалуйста, выполните ввод снова!")
