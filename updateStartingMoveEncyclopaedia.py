from .createBoardLayout import createBoardLayout
from .generateMovesUsingImportantPieces import UseGenericTacticToGenerateMove
from .translations import *

def updateStartingMoveEncyclopaedia(StartingLayout,listOfMoves):
    for count in range(listOfMoves):
        if count>0:
            move=createBoardLayout(listOfMoves[count], move)
        else:
            move=createBoardLayout(listOfMoves[count], StartingLayout)
        if count%2==0:
            move=mirrorBoard(move)
            #if not found in online starting move databse
            #get best follow-up move from the starting move database
            #DatabaseMove=to_xenonnumber(move)
            newBestMove=UseGenericTacticToGenerateMove(move,listOfMoves)
            newBestMove=to_xenonnumber(move)
            #if not newBestMove is the same as move from starting move database
            #update move in starting move database
    return move
