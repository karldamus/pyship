# Pyship ©2020 Karl Damus, All Rights Reserved
# game.py

import random
from rich import print
from rich.console import Console
import sys

from data import ai
from art import art
from display import messages, menu, drawGameBoards

console = Console()

# GLOBAL VARIABLES
# 
SIZE = 8
SHIPS = 5
DIFFICULTY = 2
PLAYER_NAME = ""
GAME_BOARD = []
# UNCHANGED
MIN_BOARD_SIZE = 8
# GAME OBJECTS
SHIP_TYPES = [
        {'name': ('carrier'), 'length': 5, 'points': 250, 'length': 5, 'initials': 'CA', 'sunk': False, 'placed': False},
        {'name': ('battleship'), 'length': 4, 'points': 200, 'length': 4,  'initials': 'BT', 'sunk': False, 'placed': False},
        {'name': ('destroyer'), 'length': 3, 'points': 150, 'length': 3,  'initials': 'DT', 'sunk': False, 'placed': False},
        {'name': ('submarine'), 'length': 2, 'points': 150, 'length': 3,  'initials': 'SB', 'sunk': False, 'placed': False},
        {'name': ('patrol'), 'length': 2, 'points': 50, 'length': 2,  'initials': 'PT', 'sunk': False, 'placed': False},
    ] 
# 

def main():
    # welcome()
    # gameMenu(MIN_BOARD_SIZE, SIZE, SHIPS, DIFFICULTY)
    setupGame()
    # gameController()

def printShipNames():
    for i in SHIP_TYPES:
        print(i['name'])

def welcome():
    global PLAYER_NAME
    art.logo()
    PLAYER_NAME = input("\n\n To start, please enter your name: ")

''' Start of menu functions '''

def displayMenu():
    print("\n  [underline]Menu:[/underline]\n")
    print("  [bold green]1.[/bold green][underline] Start Game[/underline]")
    print("  [bold green]2.[/bold green] Set [underline]size[/underline] of playable area.")
    print("  [bold green]3.[/bold green] Set [underline]difficulty[/underline] of enemy.")
    print("  [bold green]4.[/bold green] Set number of [underline]ships[/underline] to play with.")
    print("  [bold green]5.[/bold green] [red]Quit Game.[/red]")

def gameMenu(MIN_BOARD_SIZE, FUNC_SIZE, FUNC_SHIPS, FUNC_DIFFICULTY):
    global SIZE
    global SHIPS
    global DIFFICULTY

    START_GAME = False
    while START_GAME == False:
        displayMenu()
        newMenuChoice = input("\n  Please enter a number (1-5): ")
        
        if newMenuChoice.isdigit():
            # start game
            if int(newMenuChoice) == 1:
                START_GAME = True
                break
            # quit game
            if int(newMenuChoice) == 5:
                terminateGame()
            # change board size
            if int(newMenuChoice) == 2:
                changeBoardSize()
            # change difficulty
            if int(newMenuChoice) == 3:
                changeDifficulty()
            # change ship limit
            if int(newMenuChoice) == 4:
                changeShipLimit()
        else:
            gameMenu(MIN_BOARD_SIZE, SIZE, SHIPS, DIFFICULTY)
        break

def changeBoardSize():
    global SIZE
    boardSizeInput = input("\nWhat would you like the size of the board to be? ")
    if boardSizeInput.isdigit():
        if int(boardSizeInput) < MIN_BOARD_SIZE:
            messages.error_message("Please enter a number greater than or equal to " + str(MIN_BOARD_SIZE))
            changeBoardSize()
        else:
            SIZE = int(boardSizeInput)
            messages.confirmation_message("Fantastic! Your new board size is: " + str(SIZE))
            gameMenu(MIN_BOARD_SIZE, SIZE, SHIPS, DIFFICULTY)    
    else:
        messages.error_message("Please enter a valid number!")
        changeBoardSize()

def changeDifficulty():
    global DIFFICULTY
    difficultyInput = input("\nWhat would you like to set the difficulty to? (Enter a number 1-3): ")
    if difficultyInput.isdigit():
        if (int(difficultyInput) < 1) or (int(difficultyInput) > 3):
            messages.error_message("Please enter a number between 1-3")
            changeDifficulty()
        else:
            DIFFICULTY = int(difficultyInput)
            messages.confirmation_message("Fantastic! Difficulty level " + str(DIFFICULTY) + " has been set")
            gameMenu(MIN_BOARD_SIZE, SIZE, SHIPS, DIFFICULTY)   
    else:
        messages.error_message("Please enter a valid number!")
        changeDifficulty()      

def changeShipLimit():
    global SHIPS
    shipLimitInput = input("\nHow many playable ships would you like access too? (Enter a number between 5-7): ")
    if shipLimitInput.isdigit():
        if (int(shipLimitInput) < 5) or (int(shipLimitInput) > 7):
            messages.error_message("Please enter a number between 5-7")
            changeShipLimit()
        else:
            SHIPS = int(shipLimitInput)
            messages.confirmation_message("Fantastic! A total of " + str(SHIPS) + " are available to play with")
            gameMenu(MIN_BOARD_SIZE, SIZE, SHIPS, DIFFICULTY)   
    else:
        messages.error_message("Please enter a valid number!")
        changeShipLimit()      

''' End of menu functions '''

def setupGame():
    # add code to place (or choose to auto-place) ships onto gameboard
    displaySetupGameMenu()

def displaySetupGameMenu():
    print("\n  [bold green]1.[/bold green][underline] Manually place ships.[/underline]")
    print("  [bold green]2.[/bold green][underline] Generate ship positions.[/underline]")
    setupOption = input("\nChoose an option (1 or 2): ")
    if setupOption.isdigit():   
        if int(setupOption) == 1:
            manuallyPlaceShips()
        elif int(setupOption) == 2:
            automaticallyPlaceShips()
        else:
            messages.error_message("Please enter a valid number. 1 or 2: ")
            displaySetupGameMenu() 
    else:
        messages.error_message("Please enter a valid number. 1 or 2: ")
        displaySetupGameMenu()

def manuallyPlaceShips():
    currentlyPlacedShips = {}
    allShipsPlaced = False
    validMinCoordinate = (SIZE + 2) - SIZE
    validMaxCoordinate = (SIZE + 2) 
    while allShipsPlaced == False:
        input("Please enter a coordinate equal to or between ({minCoord}, {minCoord}) and ({maxCoord}, {maxCoord}): ".format(minCoord = str(validMinCoordinate), maxCoord = str(validMaxCoordinate)))
        txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)

def automaticallyPlaceShips():
    pass

def gameController():
    # add code to control the game throughout the rest of the program
    # GAME_RUNNING = True
    # while GAME_RUNNING == True:
    print(drawGameBoards.drawEmptyGameBoard(SIZE))
    pass

def placeNewShip(coords, PLAYER_BOARD):
    pass

def fireMissile(coords, HIT_LIST, MISS_LIST):
    pass

def isSunk():
    pass



def terminateGame():
    sys.exit()

if __name__ == "__main__":
    main()