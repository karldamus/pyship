# Pyship ©2020 Karl Damus, All Rights Reserved
# drawGameBoards.py

def drawEmptyGameBoard(SIZE):
    generatedBoardSize = SIZE + 2
    outerGrid = []

    for emptySingleGrid in range(generatedBoardSize):
        innerGrid = []
        if (emptySingleGrid == 0) or (emptySingleGrid == generatedBoardSize - 1):
            for secondEmptySingleGrid in range(generatedBoardSize):
                innerGrid.append("#")
        else:
            for secondEmptySingleGrid in range(generatedBoardSize):
                if (secondEmptySingleGrid == 0) or (secondEmptySingleGrid == generatedBoardSize - 1): 
                    innerGrid.append("#")
                else:
                    innerGrid.append(" ")
        outerGrid.append(innerGrid)
    return outerGrid

def drawPlayerGuessesOnEmptyGameboard():
    pass

def drawPlayerGameboard(SIZE, LIST_OF_PLAYER_SHIPS, ):
    generatedBoardSize = SIZE + 2
    outerGrid = []

    for emptySingleGrid in range(generatedBoardSize):
        innerGrid = []
        if (emptySingleGrid == 0) or (emptySingleGrid == generatedBoardSize - 1):
            for secondEmptySingleGrid in range(generatedBoardSize):
                innerGrid.append("#")
        else:
            for secondEmptySingleGrid in range(generatedBoardSize):
                if (secondEmptySingleGrid == 0) or (secondEmptySingleGrid == generatedBoardSize - 1): 
                    innerGrid.append("#")
                else:
                    innerGrid.append(" ")
        outerGrid.append(innerGrid)

    for emptyGridSpace in LIST_OF_PLAYER_COORDINATES:
        x_coord = emptyGridSpace[0]
        y_coord = emptyGridSpace[1]
        if (x_coord == 0) or (x_coord == (generatedBoardSize - 1)) or (y_coord == 0) or (y_coord == (generatedBoardSize - 1)):
            print("\n\tYou have a faulty coordinate. Please refer to line 25 of test.py\n") 
        else:
            outerGrid[y_coord][x_coord] = "="

def drawEnemyMissesOnPlayerGameboard():
    pass

def drawEnemyHitsOnPlayerGameboard():
    pass
