from rooms import main_menu, game_menu
from database import try_create
from class_ import User


def main():
    try_create()
    user = User()
    main_menu(user)
    if user.is_login:
        game_menu(user)
    else:
        print("Пока!")

if __name__ == '__main__':
    main()
