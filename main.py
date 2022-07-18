# Tic-Tac-Toe player, soon to be the perfect bot which cannot lose, hopefully it turns in to a pygame

# to clear screen after each game
from os import system, name
# to see the final board for a bit longer
from time import sleep


# its spaces for eazy printing the board
# spaces mean nobody played there
board=[" "," "," ", " "," "," ", " "," "," "]

# Change this to have diffrent simbol placed on the board
player_string = ("X","O")

move_counter = 0
on_move = player_string[0]





#the beggining printing
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
start_of_game_printing()


# to see clearer / to bo more organized
# printing the board fuction
def print_board():
    for i,e in enumerate(board):
        # if not end line
        if (i + 1) % 3 != 0:
            	print(f"{e}|", end = "")
        elif i >= 8:
            print(e)
        else:
            print(f"{e}\n-----")


# when the game is over/no more moves left or the game is won
def start_over():
    global move_counter, board, on_move
    move_counter = 0
    board=[" "," "," ", " "," "," ", " "," "," "]
    on_move = player_string[0]

    #change this number(it can be a integer or a float) to change how many seconds to freeze the screen
    sleep(3.5)
    if name == 'nt':
        system('cls')
    else:
        system('clear')


#to see if somebody won
def winning_conditions():
    #three in a row
    for i in range(0,9,3):
        if board[i] != " ":
            if board[i] == on_move and board[i+1] == on_move and board[i+2] == on_move:
                win()
    #three in a collumn
    for i in range(3):
        if board[i] != " ":
            if board[i] == on_move and board[i+3] == on_move and board[i+6] == on_move:
                win()
    #three in a diagonal
    #from upper left to bottom right
    if board[0] != " ":
        if board[0] == on_move and board[4] == on_move and board[8] == on_move:
            win()
    #from upper right to bottom left
    if board[2] != " ":
        if board[2] == on_move and board[4] == on_move and board[6] == on_move:
            win()
    

#to be organized
def win():
    print()
    print(f"{on_move}'s won!")
    sleep(1)
    print("Congratulations!")
    start_over()







# main loop
while True:

    # making the move and seeing if it is a valid number
    try:
        move = int(input(f"Place your turn ({on_move}): "))
    except ValueError:
        print("Please press a integer, not whatever you typed!")
        continue
    except KeyboardInterrupt:
        print("Shutting down now")
        start_over()
        break
    print()
    
    if move < 1:
        print("Shutting down now!")
        start_over()
        break

    # seeing if a valid number is put
    try:
        # has he played it
        if board[move - 1] == " ":
            # inserting the move
            board[move - 1] = on_move
            move_counter += 1
        else:
            print("That move has allready been played!")
            print()
            continue
    except IndexError:
        print("Shutting down now!")
        start_over()
        break

    print_board()

    winning_conditions()

    # who's turn is it
    if on_move == player_string[0]:
        on_move = player_string[1]
    else:
        on_move = player_string[0]
    
    # is there any moves left to play
    if move_counter >= 9:
        start_over()
