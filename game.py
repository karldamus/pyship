# Pyship ©2020 Karl Damus, All Rights Reserved
# game.py

import random
from rich import print
from rich.console import Console

from data import grid, ai
from art import art

console = Console()

# global variables
size = 0
ships = 0
difficulty = 0
name = ""


def main():
    welcome()
    setup_game()

def error_message(message):
    console.print("\n  " + str(message), style="bold red")

def welcome():
    art.logo()
    name = input("\n\n To start, please enter your name: ")
    display_menu()

def display_menu():
    print("\n  [bold green]1.[/bold green] Set [underline]size[/underline] of playable area.")
    print("  [bold green]2.[/bold green] Set [underline]difficulty[/underline] of enemy.")
    print("  [bold green]3.[/bold green] Set number of [underline]ships[/underline] to play with.")
    print("  [bold green]4.[/bold green] [red]Quit Game.[/red]")

    menu_choice = input("\n  Please enter a number (1-4): ")

    if menu_choice.isdigit():
        mc = int(menu_choice)
        if mc == 1:
            new_board_size = input("What would you like the size of the board to be? ")
        
    else:
        error_message("Please enter a valid number!")
        display_menu()

def set_variables(size_01, ships_01, difficulty_01, name_01):
    global size
    global ships
    global difficulty
    global name
    
    size = size_01
    ships = ships_01
    difficulty = difficulty_01
    name = name_01

def setup_game():
    pass

def add_pyship(coords, player_board):
    pass

def fire_missile(coords, list_of_guesses):
    pass

def game_controller():
    pass


if __name__ == "__main__":
    main()