# all the functions made for the easy bot

from random import choice
from functions import return_non_empty


def get_input(board):
    # choosing the random number
    move = choice(return_non_empty(board)) + 1
    print(f"The bot made the move {move}!\n")
    return move
