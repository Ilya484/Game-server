from os import system

from rooms import main_menu, menu_of_auth_user
from src.database import try_create
from src.class_ import User


def main():
    try_create()
    system("cls")
    user = User()

    main_menu(user)
    if user.is_login:
        menu_of_auth_user(user)
    else:
        print("Пока!")


if __name__ == '__main__':
    main()

