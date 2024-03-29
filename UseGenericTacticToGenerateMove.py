import time
from concurrent.futures import ThreadPoolExecutor
from findImportantPieces import findImportantPieces,bubbleSort
from generateMovesUsingImportantPieces import generateMovesUsingImportantPieces
from rateMoveBasedOnWinProbability import rateMoveBasedOnWinProbability
from createBoardLayout import createBoardLayout
from translations import *

pool=ThreadPoolExecutor(2)

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
    return 0,None
                            
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
        return UseGenericTacticToGenerateMove(boardLayout,previosMovesList)

def UseGenericTacticToGenerateMove(boardLayout,previosMovesList):
    boardLayout=createBoardLayout(boardLayout, previosMovesList)
    wImportantPieces1,bImportantPieces1=findImportantPieces(boardLayout)
    m=pool.submit(generateMovesUsingImportantPieces,boardLayout, bImportantPieces1, wImportantPieces1)
    pValues=[]
    moves=m.result()
    print(m.done())
    if m.done():
        for a in moves:
            print('moves',toFEN(a))
        print(wImportantPieces1)
        print(bImportantPieces1)
        for move in moves:
            p,q=rateMoveBasedOnWinProbability(move,0)
            pValues.append(p*100000/q)
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
                return move[count]

if __name__=='__main__':
    defaultLayout=[
        ['BR','BN','BB','BQ','BK','BB','BN','BR'],
        ['BP','BP','BP','BP','BP','BP','BP','BP'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['WP','WP','WP','WP','WP','WP','WP','WP'],
        ['WR','WN','WB','WQ','WK','WB','WN','WR']]
    previosMovesList=[['E2','E3']]
    print(toFEN(defaultLayout))
    print('starting in')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('go')
    start_time = time.time()
    move=UseGenericTacticToGenerateMove(defaultLayout, previosMovesList)
    print(move)
    print('done')
    print("--- %s seconds ---" % (time.time() - start_time))