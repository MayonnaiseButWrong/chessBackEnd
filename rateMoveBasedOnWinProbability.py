from .findImportantPieces import findImportantPieces
from .generateMovesUsingImportantPieces import generateMovesUsingImportantPieces
from .ratingBasedOnNeuralNetwork import ratingBasedOnNeuralNetwork

def isCheckMate(boardLayout):
    print('mkjhbkl')

def rateMoveBasedOnWinProbability(boardLayout,depth):
    p=0
    maxDepth=50
    wImportantPieces1,bImportantPieces1=findImportantPieces(boardLayout)
    wmoves=generateMovesUsingImportantPieces(boardLayout, bImportantPieces1, wImportantPieces1)
    for wmove in wmoves:
        if isCheckMate(wmove):
            p-=2
        else:
            wImportantPieces2,bImportantPieces2=findImportantPieces(wmove)
            bmoves=generateMovesUsingImportantPieces(wmove, bImportantPieces2, wImportantPieces2)
            for bmove in bmoves:
                if isCheckMate(bmove) is True:
                    p+=2
                elif depth<maxDepth:
                    depth+=1
                    p+=rateMoveBasedOnWinProbability(bmove, depth)
                else:
                    p+=ratingBasedOnNeuralNetwork(bmove)
    return p