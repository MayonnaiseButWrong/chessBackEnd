from .findImportantPieces import findImportantPieces
from .generateMovesUsingImportantPieces import generateMovesUsingImportantPieces
from .ratingBasedOnNeuralNetwork import ratingBasedOnNeuralNetwork

def rateMoveBasedOnWinProbability(boardLayout,depth):
    p=0
    maxDepth=50
    wImportantPieces1,bImportantPieces1=findImportantPieces(boardLayout)
    wmoves=generateMovesUsingImportantPieces(boardLayout, wImportantPieces1, bImportantPieces1)
    for wmove in wmoves:
        wImportantPieces2,bImportantPieces2=findImportantPieces(wmove)
        bmoves=generateMovesUsingImportantPieces(wmove, bImportantPieces2, wImportantPieces2)
        if len(bmoves)>0:
            p-=2
        else:
            for bmove in bmoves:
                wImportantPieces3,bImportantPieces3=findImportantPieces(wmove)
                checkMoves=generateMovesUsingImportantPieces(bmove, wImportantPieces3, bImportantPieces3)
                if len(checkMoves)>0 is True:
                    p+=2
                elif depth<maxDepth:
                    depth+=1
                    p+=rateMoveBasedOnWinProbability(bmove, depth)
                else:
                    p+=ratingBasedOnNeuralNetwork(bmove)
    return p
