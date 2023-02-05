from .findImportantPieces import findImportantPieces,bubbleSort
from .generateMovesUsingImportantPieces import generateMovesUsingImportantPieces

def typeOfMove(layout1,layout2):    #0 is a mormal move, 1 is castling, 2 is enpassant
    if layout1[0][4]=='K' and layout2[0][4]=='MT':
        if layout2[0][6]=='BK':
            return 1,0
        elif layout2[0][2]=='BK':
            return 1,0
        else:
            return 0,0
                    
    for i in range(8):
        if not (layout1[4][i]=='MT'and layout1[4][i][0]=='W'):
            if layout1[4][i]=='P' and layout2[4][i]=='MT':
                if layout2[5][i]=='BP':
                    return 0,0
                elif i<7 and layout2[5][i+1]=='BP':
                    return 0,0
                elif i>0 and layout2[5][i-1]=='BP':
                    return 0,0
                else:
                    return 2,i
    return 0
                            
def castlingAllowed(previosMovesList):
    for move in previosMovesList:
        if move[0]==[4,0]:
            return False
        if move[0]==[0,0]:
            return False
        if move[0]==[7,0]:
            return False
    return True

def enPassantAllowed(previosMovesList,i):
    for move in previosMovesList:
        if i<7 and move[0]==[i+1,6] and move[1]==[i+1,4]:
            return True
        if i>0 and move[0]==[i-1,6] and move[1]==[i-1,4]:
            return True
    return False

def useMidgameTacticToGenerateMove(boardLayout,previosMovesList):
    #check if the move is in the database
    #else
        return UseGenericTacticToGenerateMove(boardLayout,previosMovesList),True,1

def UseGenericTacticToGenerateMove(boardLayout,previosMovesList):
    wImportantPieces1,bImportantPieces1=findImportantPieces(boardLayout)
    moves=generateMovesUsingImportantPieces(boardLayout, bImportantPieces1, wImportantPieces1)
    pValues=[]
    for move in moves:
        pValues.append(rateMoveBasedOnWinProbability(move,0))
    moves=bubbleSort(moves,pValues)
    flag=True
    count=0
    for count in range(len(moves)):
        moveType,i=typeOfMove(boardLayout,move[count])
        if moveType==1:
            if castlingAllowed(previosMovesList)==True:
                return move[count]
            else:
                count+=1
        elif moveType==2:
            if enPassantAllowed(previosMovesList,i)==True:
                return move[count]
            else:
                count+=1
        else:
            return move[count], True
                