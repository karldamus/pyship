# Pyship ©2020 Karl Damus, All Rights Reserved
# game.py

import random
from rich import print
from rich.console import Console
import sys

import time

from data import ai
from art import art
from display import messages, menu, drawGameBoards

import nameof

console = Console()

SIZE = 8
SHIPS = 5
DIFFICULTY = 2
PLAYER_NAME = ""
GAME_BOARD = []

MIN_BOARD_SIZE = 8
MAX_BOARD_SIZE = 20
MIN_DIFFICULTY = 1
MAX_DIFFICULTY = 3
MIN_SHIPS = 5
MAX_SHIPS = 7

SHIP_TYPES = [
        {'name': ('carrier'), 'length': 5, 'points': 250, 'length': 5, 'initials': 'CA', 'sunk': False, 'placed': False},
        {'name': ('battleship'), 'length': 4, 'points': 200, 'length': 4,  'initials': 'BT', 'sunk': False, 'placed': False},
        {'name': ('destroyer'), 'length': 3, 'points': 150, 'length': 3,  'initials': 'DT', 'sunk': False, 'placed': False},
        {'name': ('submarine'), 'length': 2, 'points': 150, 'length': 3,  'initials': 'SB', 'sunk': False, 'placed': False},
        {'name': ('patrol'), 'length': 2, 'points': 50, 'length': 2,  'initials': 'PT', 'sunk': False, 'placed': False},
    ] 

# ==================================================================================================================== #
# ==================================================================================================================== #
# ==================================================================================================================== #

def main():
    # welcome()

    gameMenu(MIN_BOARD_SIZE, SIZE, SHIPS, DIFFICULTY)
    # setupGame(SIZE, SHIPS, DIFFICULTY)
    gameController()

def printShipNames():
    for i in SHIP_TYPES:
        print(i['name'])

def welcome():
    global PLAYER_NAME
    art.logo()
    PLAYER_NAME = input("\n\n To start, please enter your name: ")

# -----------------------------------------
# Start of menu functions
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
        displayMenu() # show game menu to player
        newMenuChoice = input("\n  Please enter a number (1-5): ")
        
        if newMenuChoice.isdigit():

            if int(newMenuChoice) == 1:
                START_GAME = True
                break
            if int(newMenuChoice) == 5:
                terminateGame()
            if int(newMenuChoice) == 2:
                # !changeBoardSize()
                gameSettingEditor("SIZE")
            if int(newMenuChoice) == 3:
                # !changeDifficulty()
                gameSettingEditor("DIFFICULTY")
            if int(newMenuChoice) == 4:
                # !changeShipLimit()
                gameSettingEditor("SHIPS")
        
        else:
            gameMenu(MIN_BOARD_SIZE, SIZE, SHIPS, DIFFICULTY)
        break

def gameSettingEditor(settingToChangeInStringFormat):
    # this function changes game settings -- usage : gameMenu()
    # 
    global SIZE
    global DIFFICULTY
    global SHIPS

    def localMessageDict(updatedSettingsValue):
        if updatedSettingsValue == "SIZE":
            messageList = ["\n\tWhat would you like the size of the board to be? ", "Please enter a number greater than or equal to " + str(MIN_BOARD_SIZE), "Fantastic! Your new board size is: " + str(SIZE)]
        if updatedSettingsValue == "DIFFICULTY":
            messageList = ["\nWhat would you like to set the difficulty to? (Enter a number 1-3): ", "Please enter a number between 1-3", "Fantastic! Difficulty level " + str(DIFFICULTY) + " has been set"]
        if updatedSettingsValue == "SHIPS":
            messageList = ["\nHow many playable ships would you like access too? (Enter a number between 5-7): ", "Please enter a number between 5-7", "Fantastic! A total of " + str(SHIPS) + " are available to play with"]
        
        return messageList

    this = settingToChangeInStringFormat

    newSettingsInput = input(localMessageDict(this)[0])

    localIfStatements = {
        'SIZE_IF': (int(newSettingsInput) < MIN_BOARD_SIZE) or (int(newSettingsInput) > MAX_BOARD_SIZE),
        'DIFFICULTY_IF': (int(newSettingsInput) < MIN_DIFFICULTY) or (int(newSettingsInput) > MAX_DIFFICULTY),
        'SHIPS_IF': (int(newSettingsInput) < MIN_SHIPS) or (int(newSettingsInput) > MAX_SHIPS)
    }

    if newSettingsInput.isdigit() == False:
        messages.error_message("Please enter a valid number!")
        gameSettingEditor(this)
    else:
        if (localIfStatements[this + "_IF"]) == False: # *the input was possible
            globals()[this] = int(newSettingsInput)
            loading(3)
            messages.confirmation_message(localMessageDict(this)[2])
            gameMenu(MIN_BOARD_SIZE, SIZE, SHIPS, DIFFICULTY)
        else:
            messages.error_message(localMessageDict(this)[1])
            gameSettingEditor(this)

# End of menu functions
# -----------------------------------------

def setupGame():
    # TODO: add code to place (or choose to auto-place) ships onto gameboard
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
    # TODO: add code to control the game throughout the rest of the program
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

# ==================================================================================================================== #
# ==================================================================================================================== #
# ==================================================================================================================== #
# * SYSTEM *

def loading(numberOfTimes):
    print("\n\t", end="")
    for i in range(numberOfTimes):
        time.sleep(.300)
        print(".", end="")
    time.sleep(.300)
    print("\n", end="")

def terminateGame():
    sys.exit()

if __name__ == "__main__":
    main()