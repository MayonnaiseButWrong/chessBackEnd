from .createBoardLayout import createBoardLayout

def comparingProbabilities(boardLayout,depth):
    maxDepth=5
    wImportantPieces1,bImportantPieces1=findImportantPieces(boardLayout)
    wmoves=generateMovesUsingImportantPieces(boardLayout, wImportantPieces1, bImportantPieces1)
    for wmove in wmoves:
        wImportantPieces2,bImportantPieces2=findImportantPieces(wmove)
        bmoves=generateMovesUsingImportantPieces(wmove, bImportantPieces2, wImportantPieces2)
        if len(bmoves)>0:
            continue
        else:
            for bmove in bmoves:
                wImportantPieces3,bImportantPieces3=findImportantPieces(wmove)
                checkMoves=generateMovesUsingImportantPieces(bmove, wImportantPieces3, bImportantPieces3)
                if len(checkMoves)>0 is True:
                    continue
                elif depth<maxDepth:
                    depth+=1
                    rateMoveBasedOnWinProbability(bmove, depth)
                else:
                    p=ratingBasedOnNeuralNetwork(bmove)
                    #find p from stockfish
                    #calculate cost
                    #train neural network

def trainNeuralNetwork(StartingLayout,listOfMoves):
    for count in range(listOfMoves):
        if count>0:
            move=createBoardLayout(listOfMoves[count], move)
        else:
            move=createBoardLayout(listOfMoves[count], StartingLayout)
        comparingProbabilities(move, 0)
        