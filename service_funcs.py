from colorama import init, Fore
from database import cursor, db
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
