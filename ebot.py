#all the functions made for the easy bot

from random import randint


def get_input(board, player_string):
    flag = 1
    while flag:
        move = randint(1,9)
        if board[move - 1] != player_string[0] and board[move - 1] != player_string[1]:
            print("The bot made the move!\n")
            return move
    