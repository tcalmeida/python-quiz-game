from functions import new_game, play_again


def main():
    new_game()

    while play_again():
        new_game()

    print('Thank you for playing!!!')


if __name__ == '__main__':
    main()
