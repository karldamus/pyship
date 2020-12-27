import random
from rich import print
from rich.console import Console
import sys
import messages

console = Console()

# global variables
SIZE = 8
SHIPS = 5
DIFFICULTY = 2
name = ""
# unchanged
MIN_BOARD_SIZE = 8

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

def changeBoardSize():
    boardSizeInput = input("\nWhat would you like the size of the board to be? ")
    if boardSizeInput.isdigit():
        if int(boardSizeInput) < MIN_BOARD_SIZE:
            messages.error_message("Please enter a number greater than or equal to " + str(MIN_BOARD_SIZE))
        else:
            SIZE = int(boardSizeInput)
            messages.confirmation_message("Fantastic! Your new board size is: " + str(SIZE))
            gameMenu(MIN_BOARD_SIZE, SIZE, SHIPS, DIFFICULTY)    
    else:
        messages.error_message("Please enter a valid number!")

def changeDifficulty():
    pass

def changeShipLimit():
    pass

def terminateGame():
    sys.exit()

if __name__ == '__main__':
    gameMenu(MIN_BOARD_SIZE, SIZE, SHIPS, DIFFICULTY)
    print("Size: " + str(SIZE))
    print("Ships: " + str(SHIPS))
    print("Difficulty: " + str(DIFFICULTY))