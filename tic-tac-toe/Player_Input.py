from Board import *


def player_choose(marker):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not check_full(board):
        position = int(input("Choose your next position " + marker + ":"))
        return position
