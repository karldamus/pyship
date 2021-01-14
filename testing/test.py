# Pyship ©2020 Karl Damus, All Rights Reserved
# test.py
# from "../" import nameof

SIZE = 8
SHIPS = 5
DIFFICULTY = 2
# PLAYER_NAME = ""
# GAME_BOARD = []

MIN_BOARD_SIZE = 8
MAX_BOARD_SIZE = 20

def main():
    # display_grid()
    # dictionaryTesting()
    # testNameOf()
    testVariableCalling()

def display_grid():
    positions = [(2,2)]
    size = 6 + 2
    outer_grid_list = []

    for i in range(size):
        inner_grid_list = []
        if (i == 0) or (i == size - 1):
            for j in range(size):
                inner_grid_list.append("#")
        else:
            for j in range(size):
                if (j == 0) or (j == size - 1): 
                    inner_grid_list.append("#")
                else:
                    inner_grid_list.append(" ")
        outer_grid_list.append(inner_grid_list)

    for marker in positions:
        x_coord = marker[0]
        y_coord = marker[1]
        if (x_coord == 0) or (x_coord == (size - 1)) or (y_coord == 0) or (y_coord == (size - 1)):
            print("\n\tYou have a faulty coordinate. Please refer to line 25 of test.py\n") 
        else:
            outer_grid_list[y_coord][x_coord] = "="

    for v in outer_grid_list:
        for w in v:
            print(w, end="  ")
        print("")

def dictionaryTesting():
    # size = "DIFFICULTY"
    # localMessageDict = {
    #     'SIZE_MESSAGES': ["\nWhat would you like the size of the board to be? ", ("Please enter a number greater than or equal to " + str(MIN_BOARD_SIZE)), ("Fantastic! Your new board size is: " + str(SIZE))],
    #     'DIFFICULTY_MESSAGES': ["\nWhat would you like to set the difficulty to? (Enter a number 1-3): ", "Please enter a number between 1-3", "Fantastic! Difficulty level " + str(DIFFICULTY) + " has been set"],
    #     'SHIPS_MESSAGES': ["\nHow many playable ships would you like access too? (Enter a number between 5-7): ", "Please enter a number between 5-7", "Fantastic! A total of " + str(SHIPS) + " are available to play with"]
    # }
    # print(localMessageDict[size + "_MESSAGES"][0])

    localIfStatements = {
        'SIZE_IF': (6 < 5),
        'DIFFICULTY_IF': (4 < 5),
        'SHIPS_IF': (4 < 5)
    }

    if (localIfStatements["SIZE_IF"]):
        print("True")
    else:
        print("false")

def testNameOf():
    variableOne = "This is a variable"
    variableTwo = "This is also a variable"

    print(nameOf(variableOne))
    print(variableTwo)

a = 5

def testVariableCalling():
    print(globals()['a'])

    

if __name__ == "__main__":
    main()