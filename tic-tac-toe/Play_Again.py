from Play_game import play_game


def play_again():
    reset = input("Do you want to play again?(Y for yes, N for no)")
    if reset.lower().startswith("y"):
        play_game()
    else:
        quit()
