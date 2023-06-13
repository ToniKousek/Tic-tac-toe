# all the functions made for the easy bot

from random import choice
from functions import can_lose,can_win,return_non_empty

def best_move(board,player_string):
    move = can_win(board,player_string)
    if move != (0,0):
        print(f"The bot made the move {move}!\n")
        return move[1]
    move = can_lose(board,player_string)
    if move != (0,0):
        print(f"The bot made the move {move}!\n")
        return move[1]
    move = choice(return_non_empty(board)) + 1
    print(f"The bot made the move {move}!\n")
    return move
    

def get_input(board,player_string):
    return best_move(board,player_string)

