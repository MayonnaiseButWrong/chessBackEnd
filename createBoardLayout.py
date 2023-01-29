import translations

defaultLayout=[['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']]
StartingLayout=defaultLayout

class piece:
    def __init__(self,t):
        self.team=t
        self.vectors=[]
        self.name=''
        
class pawn(piece):
    def __init__(self,t):
        super().__init__(t)
        self.vectors=[[[0,1]]]
        self.name=self.team+'P'

class rook(piece):
    def __init__(self, t):
        super().__init__(t)
        self.vectors=generateRmoves()
        self.name=self.team+'R'
    
    def generateRmoves(self):
        move=[]
        direction=[]
        
        for i in range(10):
            direction.append([i,0])
        move.append(direction)
        direction,i=[],0
        
        for i in range(10):
            direction.append([0,i])
        move.append(direction)
        direction,i=[],0
        
        for i in range(10):
            direction.append([-i,0])
        move.append(direction)
        direction,i=[],0
        
        for i in range(10):
            direction.append([0,-i])
        move.append(direction)
        
        return moves
    
class knight(piece):
    def __init__(self, t):
        super().__init__(t)
        self.vectors=[[[2,1]],[[1,2]],[[-1,2]],[[-2,1]],[[-2,-1]],[[-1,-2]],[[1,-2]],[[2,-1]]]
        self.name=self.team+'N'
        
class bishop(piece):
    def __init__(self, t):
        super().__init__(t)
        self.vectors=generateBmoves()
        self.name=self.team+'B'
        
    def generateBmoves():
        move=[]
        direction=[]
        
        for i in range(10):
            direction.append([i,0])
        move.append(direction)
        direction,i=[],0
        
        for i in range(10):
            direction.append([0,i])
        move.append(direction)
        direction,i=[],0
        
        for i in range(10):
            direction.append([-i,0])
        move.append(direction)
        direction,i=[],0
        
        for i in range(10):
            direction.append([0,-i])
        move.append(direction)
        
        for i in range(10):
            direction.append([i,i])
        move.append(direction)
        direction,i=[],0
        
        for i in range(10):
            direction.append([-i,i])
        move.append(direction)
        direction,i=[],0
        
        for i in range(10):
            direction.append([-i,-i])
        move.append(direction)
        direction,i=[],0
        
        for i in range(10):
            direction.append([i,-i])
        move.append(direction)
        
        return moves

class queen(piece):
    def __init__(self, t):
        super().__init__(t)
        self.vectors=generateQmoves()
        self.name=self.team+'Q'
    
    def generateQmoves():
        move=[]
        direction=[]
        
        for i in range(10):
            direction.append([i,i])
        move.append(direction)
        direction,i=[],0
        
        for i in range(10):
            direction.append([-i,i])
        move.append(direction)
        direction,i=[],0
        
        for i in range(10):
            direction.append([-i,-i])
        move.append(direction)
        direction,i=[],0
        
        for i in range(10):
            direction.append([i,-i])
        move.append(direction)
        
        return moves
    
class king(piece):
    def __init__(self, t):
        super().__init__(t)
        self.vectors=[[[1,0]],[[1,1]],[[0,1]],[[-1,1]],[[-1,0]],[[-1,-1]],[[0,-1]],[[0,-1]]]
        self.name=self.team+'K'
    
    def Castling(position):
        #add actling
        print('dhbvkjnsl')

def createBoardLayout(currentLayout):
    outputList=[[],[],[],[],[],[],[],[]]
    for j in range(len(currentLayout)):
        for i in range(len(currentLayout[j])):
            if currentLayout[j][i][1]=='P':
                outputList[j].append(pawn(currentLayout[j][i][0]))
            elif currentLayout[j][i][1]=='R':
                outputList[j].append(rook(currentLayout[j][i][0]))
            elif currentLayout[j][i][1]=='N':
                outputList[j].append(knight(currentLayout[j][i][0]))
            elif currentLayout[j][i][1]=='B':
                outputList[j].append(bishop(currentLayout[j][i][0]))
            elif currentLayout[j][i][1]=='Q':
                outputList[j].append(queen(currentLayout[j][i][0]))
            elif currentLayout[j][i][1]=='K':
                outputList[j].append(king(currentLayout[j][i][0]))

def followMovesToGenerateCurrentLayout(listOfMoves,StartingLayout):
    currentLayout=StartingLayout
    for moves in listOfMoves:
        i=toTuple(move[0])[0]
        j=toTuple(move[0])[1]
        temp=currentLayout[j][i]
        currentLayout[j][i]='MT'
        i=toTuple(move[1])[0]
        j=toTuple(move[1])[1]
        currentLayout[j][i]=temp
        #each move is a list that has 3 components, from, to, and a tuple containing information about if its an enpassant, promotion or nothing. if the thid component is empt then its a normal move.
        #add castling
        #add enpassant
        #add promotion
        