board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]


def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def check_full(board : list):
    flag = 0
    for i in range(len(board)):
        if board[i] == " ":
            flag += 1
    if flag != 0:
        return True


def win_check(board:list, mark):
    return ((board[6] == mark and board[7] == mark and board[8] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[6] == mark and board[3] == mark and board[0] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[6] == mark and board[4] == mark and board[2] == mark) or
            (board[8] == mark and board[4] == mark and board[0] == mark))
