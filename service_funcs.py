from colorama import init, Fore

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
