import translations
import __all__ from createBoardLayout

defaultLayout=[['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']]
currentLayout=createBoardLayout(defaultLayout)

def findWeights(boardLayout,specificPiece):
    print('masdvobf ji')

def generateMoves(piece):
    if piece[0]=='Q':
        return generateQMoves()
    if piece[0]=='K':
        return generateKMoves()
    if piece[0]=='B':
        return generateBMoves()
    if piece[0]=='R':
        return generateRMoves()
    if piece[0]=='N':
        return generateNMoves()

def enPassantMoves(boardLayout,i,j):
    threatening=[]
    if boardLayout[j][i][0]=='W':
        if j==3:
            if i<6 and boardLayout[3][i+1]=='BP':
                count=0
                flag=False
                temp=boardLayout
                threatening.append([i+1,3])
                while (i+count+1)<7 and (j-count)>1 and flag is False:
                    flag=True
                    count+=1
                    if boardLayout[j-count][i+count+1]=='BP':
                        threatening.append([i+count+1,j-count])
                        temp[j-count][i+count+1]='MT'
                if boardLayout[j-count-1][i+count+1][0]=='B':
                    threatening.append([i+count+1,j-count-1])
                if (j-count-1)<1:
                    temp[j][i]='MT'
                    temp[0][i+count+1]='WQ'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[i+count+1,0])
                    temp[0][i+count+1]='WR'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[i+count+1,0])
                    temp[0][i+count+1]='WB'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[i+count+1,0])
                    temp[0][i+count+1]='WN'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[i+count+1,0])
            if i>0 and boardLayout[3][i-1]=='BP':
                count=0
                flag=False
                temp=boardLayout
                threatening.append([i-1,3])
                while (i-count-1)>0 and (j-count)>1 and flag is False:
                    flag=True
                    count+=1
                    if boardLayout[j-count][i-count-1]=='BP':
                        threatening.append([i-count-1,j-count])
                        temp[j-count][i-count-1]='MT'
                if boardLayout[j-count-1][i-count-1][0]=='B':
                    threatening.append([i-count-1,j-count-1])
                if (j-count-1)<1:
                    temp[j][i]='MT'
                    temp[0][i-count-1]='WQ'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[i-count-1,0])
                    temp[0][i-count-1]='WR'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[i-count-1,0])
                    temp[0][i-count-1]='WB'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[i-count-1,0])
                    temp[0][i-count-1]='WN'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[i-count-1,0])
    


def whatPieceIsThisOneThreatening(boardLayout,SpecificPiecePosition):
    threatening=[]
    piece=boardLayout[SpecificPiecePosition[1]][SpecificPiecePosition[0]]
    if piece[1]=='P':
        if piece[0]=='W':
            if SpecificPiecePosition[0]<7 and boardLayout[SpecificPiecePosition[1]-1][SpecificPiecePosition[0]+1][0]=='B':
                threatening.append([SpecificPiecePosition[0]+1,SpecificPiecePosition[1]-1])
                if SpecificPiecePosition[1]==1:
                    temp=boardLayout
                    temp[1][SpecificPiecePosition[0]]='MT'
                    temp[0][SpecificPiecePosition[0]]='WQ'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                    temp[0][SpecificPiecePosition[0]]='WR'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                    temp[0][SpecificPiecePosition[0]]='WB'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                    temp[0][SpecificPiecePosition[0]]='WN'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
            if SpecificPiecePosition[0]>0 and boardLayout[SpecificPiecePosition[1]-1][SpecificPiecePosition[0]-1][0]=='B':
                threatening.append([SpecificPiecePosition[0]-1,SpecificPiecePosition[1]-1])
                if SpecificPiecePosition[1]==1:
                    temp=boardLayout
                    temp[1][SpecificPiecePosition[0]]='MT'
                    temp[0][SpecificPiecePosition[0]]='WQ'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                    temp[0][SpecificPiecePosition[0]]='WR'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                    temp[0][SpecificPiecePosition[0]]='WB'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                    temp[0][SpecificPiecePosition[0]]='WN'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
            if SpecificPiecePosition[1]==1:
                temp=boardLayout
                temp[1][SpecificPiecePosition[0]]='MT'
                temp[0][SpecificPiecePosition[0]]='WQ'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                temp[0][SpecificPiecePosition[0]]='WR'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                temp[0][SpecificPiecePosition[0]]='WB'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                temp[0][SpecificPiecePosition[0]]='WN'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
        else:
            if SpecificPiecePosition[0]<7 and boardLayout[SpecificPiecePosition[1]+1][SpecificPiecePosition[0]+1][0]=='B':
                threatening.append([SpecificPiecePosition[0]+1,SpecificPiecePosition[1]+1])
                if SpecificPiecePosition[1]==6:
                    temp=boardLayout
                    temp[6][SpecificPiecePosition[0]]='MT'
                    temp[7][SpecificPiecePosition[0]]='BQ'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                    temp[7][SpecificPiecePosition[0]]='BR'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                    temp[7][SpecificPiecePosition[0]]='BB'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                    temp[7][SpecificPiecePosition[0]]='BN'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
            if SpecificPiecePosition[0]>0 and boardLayout[SpecificPiecePosition[1]+1][SpecificPiecePosition[0]-1][0]=='B':
                threatening.append([SpecificPiecePosition[0]-1,SpecificPiecePosition[1]+1])
                if SpecificPiecePosition[1]==6:
                    temp=boardLayout
                    temp[6][SpecificPiecePosition[0]]='MT'
                    temp[7][SpecificPiecePosition[0]]='BQ'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                    temp[7][SpecificPiecePosition[0]]='BR'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                    temp[7][SpecificPiecePosition[0]]='BB'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                    temp[7][SpecificPiecePosition[0]]='BN'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
            if SpecificPiecePosition[1]==6:
                temp=boardLayout
                temp[6][SpecificPiecePosition[0]]='MT'
                temp[7][SpecificPiecePosition[0]]='BQ'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                temp[7][SpecificPiecePosition[0]]='BR'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                temp[7][SpecificPiecePosition[0]]='BB'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                temp[7][SpecificPiecePosition[0]]='BN'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                
        threatening=threatening+enPassantMoves(boardLayout,SpecificPiecePosition[0],SpecificPiecePosition[1])
                
        threatening=threatening.sort()
        for index in range(1,len(threatening)):
            if threatening[index-1]==threatening[index]:
                del threatening[index]
    else:
        moves=generateMoves(piece)
        for direction in moves:
            flag=False
            for vector in direction:
                if not boardLayout[SpecificPiecePosition[1]+vector[1]][SpecificPiecePosition[0]+vector[0]]=='MT':
                    if flag==False:
                        previosCheckedPiece=boardLayout[SpecificPiecePosition[1]+vector[1]][SpecificPiecePosition[0]+vector[0]]
                        threatening.append([SpecificPiecePosition[0]+vector[0],SpecificPiecePosition[1]+vector[1]])
                    elif (not previosCheckedPiece[0]==piece[0]) and (boardLayout[SpecificPiecePosition[1]+vector[1]][SpecificPiecePosition[0]+vector[0]][1]=='K'or boardLayout[SpecificPiecePosition[1]+vector[1]][SpecificPiecePosition[0]+vector[0]][1]=='Q'):
                        threatening.append([[SpecificPiecePosition[0]+vector[0],SpecificPiecePosition[1]+vector[1]]])
    #add enpassant
    #add promotion
    if boardLayout[SpecificPiecePosition[1]][SpecificPiecePosition[0]].name=='R':
        threatening='hi'
    return threatening