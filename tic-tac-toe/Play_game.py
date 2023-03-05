import random

from Player_Input import *


def play_again():
    reset = input("Do you want to play again?(Y for yes, N for no)")
    if reset.lower().startswith("y"):
        play_game()
    else:
        quit()


def play_game():
    print("                         Welcome to 'Tic-Tac-Toe' ")
    print("Board with indexes")
    print("1" + "|" + "2" + "|" + "3")
    print("4" + "|" + "5" + "|" + "6")
    print("7" + "|" + "8" + "|" + "9")

    def player_sign():
        first_choose = " "
        while (first_choose.upper() != 'X') or (first_choose.upper() != 'Q'):
            first_choose = input("Player 1 select 'X' or 'O' ,to quit please enter 'Q' :")
            if first_choose.upper() == 'X':
                return 'X', 'O'

            elif first_choose.upper() == 'O':
                return 'O', 'X'

            elif first_choose.upper() == 'Q':
                quit()

    player1, player2 = player_sign()

    flip = random.randint(1, 2)

    def choose_first():

        if flip == 1:
            print("Payer 1 is starting (" + player1 + ")")
        if flip == 2:
            print("Payer 2 is starting (" + player2 + ")")

    choose_first()

    while True:

        if flip == 1:
            print_board()
            index = player_choose(player1)
            if board[index - 1] == " ":
                board[index - 1] = player1
            else:
                print("Index is full , your turn is over")
                flip = 2
            if win_check(board, player1):
                print_board()
                print("Player one has won")

                break
            elif not check_full(board):
                print_board()
                print("Draw")
                break
            else:
                flip = 2
        else:
            print_board()
            index = player_choose(player2)
            if board[index - 1] == " ":
                board[index - 1] = player2

            else:
                print("Index is full , your turn is over")
                flip = 1
            if win_check(board, player2):
                print_board()
                print("Player two has won")
                break
            elif not check_full(board):
                print_board()
                print("Draw")
                break
            else:
                flip = 1

    play_again()
