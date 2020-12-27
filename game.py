# Pyship ©2020 Karl Damus, All Rights Reserved
# game.py

import random
from rich import print
from rich.console import Console
import sys

from data import grid, ai
from art import art
from display import messages
from display import menu

console = Console()

# global variables
SIZE = 8
SHIPS = 5
DIFFICULTY = 2
name = ""
# unchanged
MIN_BOARD_SIZE = 8

SHIP_TYPES = [
        {'name': ('carrier'), 'length': 5, 'points': 250, 'length': 5, 'initials': 'CA'},
        {'name': ('battleship'), 'length': 4, 'points': 200, 'length': 4,  'initials': 'BT'},
        {'name': ('destroyer'), 'length': 3, 'points': 150, 'length': 3,  'initials': 'DT'},
        {'name': ('submarine'), 'length': 2, 'points': 150, 'length': 3,  'initials': 'SB'},
        {'name': ('patrol'), 'length': 2, 'points': 50, 'length': 2,  'initials': 'PT'},
    ] 

def main():
    welcome()
    # setup_game()

def welcome():
    art.logo()
    name = input("\n\n To start, please enter your name: ")
    display_menu()

def display_menu():
    global SIZE
    global SHIPS
    global DIFFICULTY
    
    setup_game()

'''
def set_variables(size_01, ships_01, difficulty_01, name_01):
    global SIZE
    global SHIPS
    global DIFFICULTY
    global name
    
    SIZE = size_01
    SHIPS = ships_01
    DIFFICULTY = difficulty_01
    name = name_01
'''

def setup_game():
    print("Game has been started")

def add_pyship(coords, player_board):
    pass

def fire_missile(coords, list_of_guesses):
    pass

def game_controller():
    pass

def terminateGame():
    sys.exit()

if __name__ == "__main__":
    main()