# all the functions made for the easy bot

from random import choice
from functions import can_lose,can_win,return_non_empty

def get_input(board,player_string):
    poss = (can_win(board,player_string),can_lose(board,player_string))
    if poss[0][0] == 1:
        print(f"The bot made the move {poss[0][1]}!\n")
        return poss[0][1]
    elif poss[1][0] == 1:
        print(f"The bot made the move {poss[1][1]}!\n")
        return poss[1][1]
    else:
        # random
        move = choice(return_non_empty(board)) + 1
        print(f"The bot made the move {move}!\n")
        return move

