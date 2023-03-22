from translations import *

defaultLayout=[['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']]
StartingLayout=defaultLayout

def makeMove(Layout,move):
    Layout[toTuple(move[1])[0]][toTuple(move[1])[1]]=Layout[toTuple(move[0])[0]][toTuple(move[0])[1]]
    if len(move)==3:
        if move[3][0][1]=='Q' or move[3][0][1]=='R'or move[3][0][1]=='N'or move[3][0][1]=='B':
            Layout[toTuple(move[1])[1]][toTuple(move[1])[0]]=move[3][0]
            Layout[toTuple(move[0])[1]][toTuple(move[0])[0]]='MT'
            for square in range(1,len(move[3])):
                currentPosition=toTuple(move[3][square])
                Layout[currentPosition[1]][currentPosition[0]]='MT'
        else:
            for square in range(0,len(move[3])):
                currentPosition=toTuple(move[3][square])
                Layout[currentPosition[1]][currentPosition[0]]='MT'
    else:
        Layout[toTuple(move[1])[1]][toTuple(move[1])[0]]=Layout[toTuple(move[0])[1]][toTuple(move[0])[0]]
        Layout[toTuple(move[0])[1]][toTuple(move[0])[0]]='MT'
    return Layout

def createBoardLayout(layout,previosMovesList):
    for move in previosMovesList:
        layout=makeMove(layout,move)
    return layout
    
        #each move is a list that has 3 components, from, to, and a tuple containing information about if its an enpassant, promotion or nothing. if the thid component is empt then its a normal move.
        #add castling
        #add enpassant
        #add promotion
        