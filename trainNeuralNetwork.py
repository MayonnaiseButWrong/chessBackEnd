from createBoardLayout import createBoardLayout
from stockfish import Stockfish
from translations import *
from ratingBasedOnNeuralNetwork import NNUE

#finding a way to constantly generate a dataset was out of the scope of this project, so i am just assuming that whatever stockish says is the best possible move and using that to train my own NNUE
stockfish=Stockfish(path='/stockfish',depth=10, parameters={"Threads": 2, "Minimum Thinking Time":10,"UCI_Chess960": "false","UCI_LimitStrength": "false","UCI_Elo": 3000, "Hash": 2048})

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
                if depth<maxDepth:
                    depth+=1
                    rateMoveBasedOnWinProbability(bmove, depth)
                else:
                    stockfish.set_fen_position(toFEN(bmove)+' b')
                    eval=stockfish.get_evaluation()
                    NNUE.train([bmove,eval])
                    
                    
                    

def trainNeuralNetwork(StartingLayout,listOfMoves):
    for count in range(listOfMoves):
        if count>0:
            move=createBoardLayout(listOfMoves[count], move)
        else:
            move=createBoardLayout(listOfMoves[count], StartingLayout)
        comparingProbabilities(move, 0)
        