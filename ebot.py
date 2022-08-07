# all the functions made for the easy bot

from random import choice


def get_input(board):
    # getting the unplayed moves
    bar = []
    for e, i in enumerate(board):
        if i == " ":
            bar.append(e+1)

    # choosing the random number
    move = choice(bar)
    print(f"The bot made the move {move}!\n")
    return move
