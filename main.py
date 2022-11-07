# Tic-Tac-Toe player, soon to be the perfect bot which cannot lose, hopefully it turns in to a pygame

# to clear screen after each game
from os import system, name
# to see the final board for a bit longer
from time import sleep
from random import randint
# to get all functions for the general game
import functions as game
import ebot
import mbot

# its spaces for eazy printing the board
# spaces mean nobody played there
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Change this to have diffrent simbol placed on the board
player_string = ("X", "O")

move_counter = 0
num_of_games = 0

on_move = player_string[num_of_games % 2]


game.start_of_game_printing()

opponent = game.choose_opponent()

# main loop
while True:

    if opponent == "e":
        if on_move == player_string[0]:
            returned = game.grab_check_input(board, on_move)
        else:
            returned = ebot.get_input(board)
    elif opponent == "m":
        if on_move == player_string[0]:
            returned = game.grab_check_input(board, on_move)
        else:
            returned = mbot.get_input(board,player_string)
    elif opponent == "p":
        returned = game.grab_check_input(board, on_move)

    if returned == 10:
        break
    elif returned == 11:
        continue
    else:
        board[returned - 1] = on_move
        move_counter += 1

    game.print_board(board)

    if game.winning_conditions(board, on_move):
        game.win(on_move)
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        num_of_games += 1
        on_move = player_string[num_of_games % 2]
        move_counter = 0
        continue

    on_move = game.change_turn(on_move, player_string)

    # is there any moves left to play
    if move_counter >= 9:
        game.start_over()
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        num_of_games += 1
        on_move = player_string[num_of_games % 2]
        move_counter = 0
