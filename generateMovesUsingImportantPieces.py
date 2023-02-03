from .createBoardLayout import *

def enPassantMoves(boardLayout,i,j):
    moves=[]
    if boardLayout[j][i][0]=='W':
        if j==3:
            if i<7 and boardLayout[3][i+1]=='BP':
                temp=i
                i+=1
                flag=False
                positionList=[]
                tempList=[]
                startSquare=[i,j]
                while i<7 and j>1 and flag==False:
                    j-=1
                    i+=1
                    flag=True
                    if boardLayout[j][i]=='BP':
                        flag=False
                        positionList.append([i,j])
                endSquare=[i,j-1]
                i=temp
                if j==1:
                    tempList.append('WQ')
                    tempList=tempList+positionList
                    moves.append([[i,j],tempList])
                    tempList=[]
                    tempList.append('WB')
                    tempList=tempList+positionList
                    moves.append([i,j,tempList])
                    tempList=[]
                    tempList.append('WN')
                    tempList=tempList+positionList
                    moves.append([i,j,tempList])
                    tempList=[]
                    tempList.append('WR')
                    tempList=tempList+positionList
                    moves.append([i,j,tempList])
                else:
                    moves.append([i,j,positionList])
            if i>0 and boardLayout[3][i+1]=='BP':
                temp=i
                i-=1
                flag=False
                positionList=[]
                tempList=[]
                startSquare=[i,j]
                while i<7 and j>1 and flag==False:
                    j-=1
                    i-=1
                    flag=True
                    if boardLayout[j][i]=='BP':
                        flag=False
                        positionList.append([i,j])
                endSquare=[i,j-1]
                i=temp
                if j==1:
                    tempList.append('WQ')
                    tempList=tempList+positionList
                    moves.append([i,j,tempList])
                    tempList=[]
                    tempList.append('WB')
                    tempList=tempList+positionList
                    moves.append([i,j,tempList])
                    tempList=[]
                    tempList.append('WN')
                    tempList=tempList+positionList
                    moves.append([i,j,tempList])
                    tempList=[]
                    tempList.append('WR')
                    tempList=tempList+positionList
                    moves.append([i,j,tempList])
                else:
                    moves.append([i,j,positionList])
    return moves
def castling(boardLayout,i,j):
    print('nbdgsijofkapd')
def pawnMoves(boardLayout,i,j):
    moves=[]
    if boardLayout[j][i][0]=='B':
        if j<6:
            if boardLayout[j+1][i]=='MT':
                moves.append([[i,j],[i,j+1]])
            if boardLayout[j+1][i+1][0]=='W':
                moves.append([[i,j],[i+1,j+1]])
            if boardLayout[j+1][i-1][0]=='W':
                moves.append([[i,j],[i-1,j+1]])
        if j==1:
            if boardLayout[2][i]=='MT':
                if boardLayout[3][i]=='MT' or boardLayout[3][i][0]=='W':
                    moves.append([[i,j],[i,3]])
    else:
        if j>1:
            if boardLayout[j-1][i]=='MT':
                moves.append([[i,j],[i,j-1]])
            if boardLayout[j-1][i+1][0]=='B':
                moves.append([[i,j],[i+1,j-1]])
            if boardLayout[j-1][i-1][0]=='B':
                moves.append([[i,j],[i-1,j-1]])
        if j==6:
            if boardLayout[5][i]=='MT':
                if boardLayout[4][i]=='MT' or boardLayout[4][i][0]=='B':
                    moves.append([[i,j],[i,4]])
    moves=moves+enPassantMoves(boardLayout,i,j)
    return moves

def kingMoves(boardLayout,i,j):
    print('sdfbuhio')

def generateMovesUsingImportantPieces(boardLayout,importantPieces):
    moves=[]
    for piece in importantPieces:
        vectors=generateMoves(boardLayout[piece[1]][piece[0]])
        if boardLayout[piece[1]][piece[0]][1]=='P':
            moves=moves+pawnMoves(boardLayout,piece[0],piece[1])
        elif boardLayout[piece[1]][piece[0]][1]=='K':
            moves=moves+kingMoves(boardLayout,piece[0],piece[1])
        elif boardLayout[piece[1]][piece[0]][1]=='R':
            moves=moves+castling(boardLayout,piece[0],piece[1])
            for direction in vectors:
                for vector in direction:
                    if not (boardLayout[piece[1]+vector[1]][piece[0]+vector[0]]=='MT'):
                        if (piece[0]+vector[0])>=0 and (piece[0]+vector[0])<8 and (piece[1]+vector[1])>=0 and (piece[1]+vector[1])<8:
                            if not (boardLayout[piece[1]][piece[0]][0]==boardLayout[piece[1]+vector[1]][piece[0]+vector[0]][0]):
                                moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])
        else:
            for direction in vectors:
                for vector in direction:
                    if not (boardLayout[piece[1]+vector[1]][piece[0]+vector[0]]=='MT'):
                        if (piece[0]+vector[0])>=0 and (piece[0]+vector[0])<8 and (piece[1]+vector[1])>=0 and (piece[1]+vector[1])<8:
                            if not (boardLayout[piece[1]][piece[0]][0]==boardLayout[piece[1]+vector[1]][piece[0]+vector[0]][0]):
                                moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])        
    return moves
