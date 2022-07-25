# all the functions for every use in main.py

# to clear screen after each game
from os import system, name
# to see the final board for a bit longer
from time import sleep


# the beggining printing
def start_of_game_printing():
    sleep(1)
    print()
    print("This is a Tic-Tac-Toe game!")
    sleep(1)
    print("To exit press a number diffrent from 1-9 or press 'ctrl + c'!")
    sleep(2)
    print("To play, press the number corresponding to the place (see below)")
    print()
    sleep(2)
    print("1|2|3\n-----\n4|5|6\n-----\n7|8|9")
    sleep(3)
    print()


# to see clearer / to bo more organized
# printing the board fuction
def print_board(board):
    for i, e in enumerate(board):
        # if not end line
        if (i + 1) % 3 != 0:
            print(f"{e}|", end="") if e != " " else print(f"{i+1}|", end="")
        elif i >= 8:
            print(e) if e != " " else print(i+1)
        else:
            print(f"{e}\n-----") if e != " " else print(f"{i+1}\n-----")


# when the game is over/no more moves left or the game is won
def start_over():
    # change this number(it can be a integer or a float) to change how many seconds to freeze the screen
    sleep(3.5)
    if name == 'nt':
        system('cls')
    else:
        system('clear')


# to see if somebody won
def winning_conditions(board, on_move_string):
    # three in a row
    for i in range(0, 9, 3):
        if board[i] != " ":
            if board[i] == on_move_string and board[i+1] == on_move_string and board[i+2] == on_move_string:
                win(on_move_string)
    # three in a collumn
    for i in range(3):
        if board[i] != " ":
            if board[i] == on_move_string and board[i+3] == on_move_string and board[i+6] == on_move_string:
                win(on_move_string)
    # three in a diagonal
    # from upper left to bottom right
    if board[0] != " ":
        if board[0] == on_move_string and board[4] == on_move_string and board[8] == on_move_string:
            win(on_move_string)
    # from upper right to bottom left
    if board[2] != " ":
        if board[2] == on_move_string and board[4] == on_move_string and board[6] == on_move_string:
            win(on_move_string)


# to be organized
def win(on_move_string):
    print()
    print(f"{on_move_string}'s won!")
    sleep(1)
    print("Congratulations!")
    start_over()


def grab_input(board, on_move_string):
    try:
        move = int(input(f"Place your turn ({on_move_string}): "))
    except ValueError:
        print("Please press a integer, not whatever you typed!")
        return 1
    except KeyboardInterrupt:
        print("Shutting down now")
        start_over()
        return 0
    print()

    if move < 1:
        print("Shutting down now!")
        start_over()
        return 0

    # seeing if a valid number is put
    try:
        # has he played it
        if board[move - 1] == " ":
            # inserting the move
            board[move - 1] = on_move_string
            move_counter += 1
        else:
            print("That move has allready been played!")
            print()
            return 1
    except IndexError:
        print("Shutting down now!")
        start_over()
        return 0


# who's turn is it
def change_turn(on_move_string, player_string):

    if on_move_string == player_string[0]:
        return player_string[1]
    else:
        return player_string[0]
