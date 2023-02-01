import translations
import createBoardLayout

defaultLayout=[['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']]
currentLayout=createBoardLayout(defaultLayout)

def findWeights(boardLayout,specificPiece):
    print('masdvobf ji')

def whatPieceIsThisOneThreatening(boardLayout,SpecificPiecePosition):
    threatening=[]
    protecting=[]
    
    #add castling
    #add enpassant
    #add promotion
    if boardLayout[SpecificPiecePosition[1]][SpecificPiecePosition[0]].name=='R':
        threatening='hi'
    return threatening