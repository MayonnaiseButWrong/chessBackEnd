from .createBoardLayout import *

def opponentMoves(boardLayout,importantPieces):
    moves=[]
    for piece in importantPieces:
        if boardLayout[piece[1]][piece[0]][1]=='K':
            continue
        if boardLayout[piece[1]][piece[0]][1]=='P':
            if (piece[1]==1 and boardLayout[piece[1]][piece[0]][1]=='W') or (piece[1]==6 and boardLayout[piece[1]][piece[0]][1]=='B'):
                moves.append(piece,[piece[0]+1,piece[1]+1])
                moves.append(piece,[piece[0]-1,piece[1]+1])
        else:
            for direction in vectors:
                for vector in direction:
                    if not (boardLayout[piece[1]+vector[1]][piece[0]+vector[0]]=='MT'):
                        if (piece[0]+vector[0])>=0 and (piece[0]+vector[0])<8 and (piece[1]+vector[1])>=0 and (piece[1]+vector[1])<8:
                            if not (boardLayout[piece[1]][piece[0]][0]==boardLayout[piece[1]+vector[1]][piece[0]+vector[0]][0]):
                                moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])        
    return moves

def enPassantMoves(boardLayout,i,j):
    moves=[]
    if boardLayout[j][i][0]=='W':
        if j==3:
            if i<7 and boardLayout[3][i+1]=='BP':
                temp=i
                startSquare=[i,j]
                i+=1
                flag=False
                positionList=[]
                tempList=[]
                while i<7 and j>0 and flag==False:
                    flag=True
                    if boardLayout[j][i]=='BP':
                        flag=False
                        positionList.append([i,j])
                    j-=1
                    i+=1
                endSquare=[i,j-1]
                i=temp
                if j==1:
                    tempList.append('WQ')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                    tempList=[]
                    tempList.append('WB')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                    tempList=[]
                    tempList.append('WN')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                    tempList=[]
                    tempList.append('WR')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                else:
                    moves.append([startSquare,endSquare,positionList])
            if i>0 and boardLayout[3][i+1]=='BP':
                startSquare=[i,j]
                temp=i
                i-=1
                flag=False
                positionList=[]
                tempList=[]
                while i<7 and j>0 and flag==False:
                    flag=True
                    if boardLayout[j][i]=='BP':
                        flag=False
                        positionList.append([i,j])
                    j-=1
                    i-=1
                endSquare=[i,j-1]
                i=temp
                if j==1:
                    tempList.append('WQ')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                    tempList=[]
                    tempList.append('WB')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                    tempList=[]
                    tempList.append('WN')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                    tempList=[]
                    tempList.append('WR')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                else:
                    moves.append([startSquare,endSquare,positionList])
    else:
        if j==4:
            if i<7 and boardLayout[3][i+1]=='WP':
                temp=i
                startSquare=[i,j]
                i+=1
                flag=False
                positionList=[]
                tempList=[]
                while i<7 and j<7 and flag==False:
                    flag=True
                    if boardLayout[j][i]=='WP':
                        flag=False
                        positionList.append([i,j])
                    j+=1
                    i+=1
                endSquare=[i,j+1]
                i=temp
                if j==6:
                    tempList.append('BQ')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                    tempList=[]
                    tempList.append('BB')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                    tempList=[]
                    tempList.append('BN')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                    tempList=[]
                    tempList.append('BR')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                else:
                    moves.append([startSquare,endSquare,positionList])
            if i>0 and boardLayout[3][i+1]=='WP':
                startSquare=[i,j]
                temp=i
                i-=1
                flag=False
                positionList=[]
                tempList=[]
                while i<7 and j<7 and flag==False:
                    flag=True
                    if boardLayout[j][i]=='WP':
                        flag=False
                        positionList.append([i,j])
                    j+=1
                    i-=1
                endSquare=[i,j-1]
                i=temp
                if j==1:
                    tempList.append('BQ')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                    tempList=[]
                    tempList.append('BB')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                    tempList=[]
                    tempList.append('BN')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                    tempList=[]
                    tempList.append('BR')
                    tempList=tempList+positionList
                    moves.append([startSquare,endSquare,tempList])
                else:
                    moves.append([startSquare,endSquare,positionList])
    return moves

def castling(boardLayout,i,j,opponentMoves):
    l,r=True,True
    moves=[]
    if boardLayout[j][i][0]=='W':
        for piece in opponentMoves:
            if piece[1]==0:
                if i>4:
                    r=False
                elif i<4:
                    l=False
                else:
                    l,r==False,False
        if l==True:
            moves.append([[4,0],[2,0]])
        if r==True:
            moves.append([[4,0],[6,0]])
    else:
        for piece in opponentMoves:
            if piece[1]==7:
                if i>4:
                    r=False
                elif i<4:
                    l=False
                else:
                    l,r==False,False
        if l==True:
            moves.append([[4,7],[2,7]])
        if r==True:
            moves.append([[4,7],[6,7]])
    return moves
            
    
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

def kingMoves(boardLayout,i,j,opponentMoves):
    moves=[]
    vectors=[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]
    for piece in opponentMoves:
        for vector in vectors:
            if not(((i+vector[0])==piece[0]) and ((j+vector[1])==piece[1])):
                moves.append([[i,j],[i+vector[0],j+vector[1]]])
    return moves

def generateMoves(boardLayout,importantPieces,opponentImportantPieces):
    moves=[]
    for piece in importantPieces:
        vectors=generateMoves(boardLayout[piece[1]][piece[0]])
        if boardLayout[piece[1]][piece[0]][1]=='P':
            moves=moves+pawnMoves(boardLayout,piece[0],piece[1])
        elif boardLayout[piece[1]][piece[0]][1]=='K':
            opponentMoves=opponentMoves(boardLayout,opponentImportantPieces)
            moves=moves+kingMoves(boardLayout,piece[0],piece[1],opponentMoves)
        elif boardLayout[piece[1]][piece[0]][1]=='R':
            opponentMoves=opponentMoves(boardLayout,opponentImportantPieces)
            moves=moves+castling(boardLayout,piece[0],piece[1],opponentMoves)
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

def generateBoardLayout(move,boardLayout):
    if len(move)==2:
        boardLayout[move[1][0]][move[1][1]]=boardLayout[move[0][0]][move[0][1]]
        boardLayout[move[0][0]][move[0][1]]='MT'
    elif move[2][0][0]=='W' or move[2][0][0]=='B':
        boardLayout[move[1][0]][move[1][1]]=move[2][0]
        boardLayout[move[0][0]][move[0][1]]='MT'
        if len(move[2])>1:
            for pos in range(1,move[2]):
                boardLayout[move[2][pos][1]][move[2][pos][0]]='MT'
    elif len(move[2])>1:
        for pos in range(1,move[2]):
            boardLayout[move[2][pos][1]][move[2][pos][0]]='MT'
    return boardLayout
            

def generateMovesUsingImportantPieces(boardLayout,importantPieces,opponentImportantPieces):
    moves=generateMoves(boardLayout,importantPieces,opponentImportantPieces)
    outputList=[]
    for move in moves:
        newLayout=generateBoardLayout(move,boardLayout)
        outptList.append(newLayout)
    return outputList