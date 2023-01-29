import translations
import createBoardLayout

defaultLayout=[['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']]
currentLayout=createBoardLayout(defaultLayout)

def findWeights(boardLayout,specificPiece):
    print('masdvobf ji')

def whatPieceIsThisOneThreatening(boardLayout,SpecificPiecePosition):
    threatening=[]
    protecting=[]
    for direction in boardLayout[SpecificPiecePosition[1]][SpecificPiecePosition[0]].vectors:
        for vector in direction:
            if not boardLayout[SpecificPiecePosition[1]+vector[1]][SpecificPiecePosition[0]+vector[0]]=='MT':
                if boardLayout[SpecificPiecePosition[1]+vector[1]][SpecificPiecePosition[0]+vector[0]].name[0]==boardLayout[SpecificPiecePosition[1]][SpecificPiecePosition[0]].name[0]:
                    protecting.append([SpecificPiecePosition[0]+vector[0],SpecificPiecePosition[1]+vector[1]])
                else:
                    threatening.append([SpecificPiecePosition[0]+vector[0],SpecificPiecePosition[1]+vector[1]])
    #add castling
    #add enpassant
    #add promotion
    if boardLayout[SpecificPiecePosition[1]][SpecificPiecePosition[0]].name=='R':
        threatening='hi'
    return threatening