# Pyship ©2020 Karl Damus, All Rights Reserved
# game.py

import random
from rich import print
from rich.console import Console
import sys

from data import grid, ai
from art import art
from display import messages

console = Console()

# global variables
size = 8
ships = 5
difficulty = 2
name = ""
# unchanged
min_board_size = 8

SHIP_TYPES = [
        {'name': _('carrier'), 'length': 5, 'points': 250, 'length': 5, 'initials': 'CA'},
        {'name': _('battleship'), 'length': 4, 'points': 200, 'length': 4,  'initials': 'BT'},
        {'name': _('destroyer'), 'length': 3, 'points': 150, 'length': 3,  'initials': 'DT'},
        {'name': _('submarine'), 'length': 2, 'points': 150, 'length': 3,  'initials': 'SB'},
        {'name': _('patrol'), 'length': 2, 'points': 50, 'length': 2,  'initials': 'PT'},
    ] 

def main():
    welcome()
    # setup_game()

def welcome():
    art.logo()
    name = input("\n\n To start, please enter your name: ")
    display_menu()

def display_menu():
    global size
    global ships
    global difficulty

    print("\n  [underline]Menu:[/underline]\n")
    print("  [bold green]1.[/bold green][underline] Start Game[/underline]")
    print("  [bold green]2.[/bold green] Set [underline]size[/underline] of playable area.")
    print("  [bold green]3.[/bold green] Set [underline]difficulty[/underline] of enemy.")
    print("  [bold green]4.[/bold green] Set number of [underline]ships[/underline] to play with.")
    print("  [bold green]5.[/bold green] [red]Quit Game.[/red]")
    
    start_game = False
    while start_game == False:

        menu_choice = input("\n  Please enter a number (1-4): ")

        if menu_choice.isdigit():
            mc = int(menu_choice)
            # Setting option 1: Start game
            if mc == 1:
                start_game = True
                break
            # Settings option 5: Quit game
            elif mc == 5:
                terminate_game()
            # Settings option 2: change size of board
            elif mc == 2:
                new_board_size = input("\nWhat would you like the size of the board to be? ")
                if new_board_size.isdigit():
                    if int(new_board_size) < min_board_size:
                        messages.error_message("Please enter a number greater than or equal to " + str(min_board_size))
                    else:
                        size = int(new_board_size)
                        messages.confirmation_message("Fantastic! Your new board size is: " + str(size))
                        display_menu()    
                else:
                    messages.error_message("Please enter a valid number!")
            # change difficulty
            elif mc == 3:
                new_difficulty = input("\nSet the difficulty by typing 1, 2, or 3: ")
                if new_difficulty.isdigit():
                    if int(new_difficulty) < 1 or int(new_difficulty) > 3:
                        messages.error_message("Please enter a number that is equal to 1, 2, or 3")
                    else:
                        difficulty = int(new_difficulty)
                        messages.confirmation_message("Fantastic! Difficulty has been set to: " + str(difficulty))
                        display_menu()    
                else:
                    messages.error_message("Please enter a valid number!")
        else:
            messages.error_message("Please enter a valid number!")
            display_menu()
    
    setup_game()

'''
def set_variables(size_01, ships_01, difficulty_01, name_01):
    global size
    global ships
    global difficulty
    global name
    
    size = size_01
    ships = ships_01
    difficulty = difficulty_01
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

def terminate_game():
    sys.exit()

if __name__ == "__main__":
    main()