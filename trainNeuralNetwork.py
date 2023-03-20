from createBoardLayout import createBoardLayout
from stockfish import Stockfish
from translations import *
from ratingBasedOnNeuralNetwork import NNUE

#finding a way to constantly generate a dataset was out of the scope of this project, so i am just assuming that whatever stockish says is the best possible move and using that to train my own NNUE
#stockfish=Stockfish('stockfish.exe')


def tobinary(ins):
    out=[]
    if ins<1:
        while ins<1:
            ins=ins*2
            out.append(0)
        out.append(1)
        for i in range(5):
            if ins>1: 
                out.append(1)
                ins-=1
            else: out.append(0)
        return out[1:-1]
    else:
        while ins>=1:
            out.append(ins%2)
            ins=ins//2
        while len(out)<4:
            out.append(0)
        return out[::-1]

def twoscompliment(ins):
    ins=tobinary(ins)
    flag,out=False,''
    for n in range(len(ins)):
        if n>len(ins):n=0
        if ins[-n]=='1' and flag==False:
            out='1'+out
            flag=True
        elif ins[-n]=='1':
            out='0'+out
        else:
            out='1'+out
    return out
        
def tomantissa(ins):
    ins=tobinary(ins)
    if len(ins)>6:
        exponent=len(ins)-6
        if exponent>14:
            exponent=twoscompliment(exponent)
            return exponent+ins[-6:-1]
        else:
            exponent=tobinary(exponent)
            return exponent+ins[-6:-1]
    else:
        return [0,0,0,0]+ins
    #fix this pls
    
def format(ins,n):
    out=[]
    if ins<0:
        a=tomantissa((float(n+int(ins))/n))
    else:
        a=tomantissa(float(int(ins)/n))
    for b in a:
        out.append([b])
    return out
        
def numberofpoints(ins):
    points,t={'B':3,'N':3,'Q':9,'K':0,'R':4,'P':1,'T':0},0
    for j in range(8):
        for i in range(8):
            t+=points[ins[j][i][1]]
    return t

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
                if len(checkMoves)>0:
                    continue
                if depth<maxDepth:
                    depth+=1
                    rateMoveBasedOnWinProbability(bmove, depth)
                else:
                    stockfish.set_fen_position(toFEN(bmove)+' b - - 0 1')
                    eval=stockfish.get_evaluation()
                    print(eval)
                    #eval=format(eval['value'],numberofpoints(bmove))
                    #NNUE.train([bmove,eval])
                    
def trainNeuralNetwork(StartingLayout,listOfMoves):
    for count in range(listOfMoves):
        if count>0:
            move=createBoardLayout(listOfMoves[count], move)
        else:
            move=createBoardLayout(listOfMoves[count], StartingLayout)
        comparingProbabilities(move, 0)

if __name__=="__main__":
    defaultLayout=[['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']]
    #isvalid=stockfish.is_fen_valid(toFEN(defaultLayout) + ' b - - 0 1')
    #if isvalid is True:
        #stockfish.set_fen_position(toFEN(defaultLayout) + ' b - - 0 1')
        #eval=stockfish.get_evaluation()
        #print(eval)
        #eval=format(eval['value'],numberofpoints(defaultLayout))
        #print(eval)
    eval=format(2,numberofpoints(defaultLayout))
    print(eval)
    NNUE.train([defaultLayout,eval])
    print('here')
