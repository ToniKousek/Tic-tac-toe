# all the functions for every use in main.py

# to clear screen after each game
from os import system, name
import string
# to see the final board for a bit longer
from time import sleep


# the beggining printing
def start_of_game_printing():
    #sleep(1)
    print()
    print("This is a Tic-Tac-Toe game!")
    #sleep(1)
    print("To exit press a number diffrent from 1-9 or press 'ctrl + c'!")
    #sleep(2)
    print("To play, press the number corresponding to the place (see below)")
    print()
    #sleep(2)
    print("1|2|3\n-----\n4|5|6\n-----\n7|8|9")
    #sleep(3)
    print()


def choose_opponent():
    print("Who would you like to play against:")
    
    while 1:
        opp = input("press e for the easy bot,\npress m for medium bot\nor press p for another human player: ")
        if opp.strip().lower() == "e" or opp.strip().lower() == "p" or opp.strip().lower() == "m":
            return opp.strip().lower()
        else:
            print("Please press the following, and not gibberish:")


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
    print()


# when the game is over/no more moves left or the game is won
def start_over():
    # change this number(it can be a integer or a float) to change how many seconds to freeze the screen
    #sleep(3.5)
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
                return 1
    # three in a collumn
    for i in range(3):
        if board[i] != " ":
            if board[i] == on_move_string and board[i+3] == on_move_string and board[i+6] == on_move_string:
                return 1
    # three in a diagonal
    # from upper left to bottom right
    if board[0] != " ":
        if board[0] == on_move_string and board[4] == on_move_string and board[8] == on_move_string:
            return 1
    # from upper right to bottom left
    if board[2] != " ":
        if board[2] == on_move_string and board[4] == on_move_string and board[6] == on_move_string:
            return 1


# to be organized
def win(on_move_string):
    print()
    print(f"{on_move_string}'s won!")
    #sleep(1)
    print("Congratulations!")
    start_over()


def grab_check_input(board, on_move_string):
    try:
        move = int(input(f"Place your turn ({on_move_string}): "))
    except ValueError:
        print("Please press a integer, not whatever you typed!")
        return 11
    except KeyboardInterrupt:
        print("Shutting down now")
        start_over()
        return 10
    
    if move > 9:
        print("Shutting down now!")
        start_over()
        return 10

    print()
    

    if move < 1:
        print("Shutting down now!")
        start_over()
        return 10

    # seeing if a valid number is put
    try:
        # has he played it
        if board[move - 1] != " ":
            print("That move has allready been played!")
            print()
            return 11

    except IndexError:
        print("Shutting down now!")
        start_over()
        return 10

    return move

    


# who's turn is it
def change_turn(on_move_string, player_string):

    if on_move_string == player_string[0]:
        return player_string[1]
    else:
        return player_string[0]



# functions used accross bots -----------------------------------------------------------------------------------------------------------------
def return_non_empty(board):
        non_empty = []
        for e, i in enumerate(board):
            if i == " ":
                non_empty.append(e)
        return non_empty

def can_win(board, player_string): 
    for move in return_non_empty(board):
        temp = board[:]
        temp[move] = player_string[1]
        if winning_conditions(temp,player_string[1]):
            return (1,move+1)
        else:
            return (0,0)
        


def can_lose(board,player_string):
    for move in return_non_empty(board):
        temp = board[:]
        temp[move] = player_string[0]
        if winning_conditions(temp,player_string[0]):
            return (1,move+1)
        else:
            return (0,0)