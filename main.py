from generateAMoveToReturnToThePlayer import generateAMoveToReturnToThePlayer
from updateDatabase import database

class game:
    def __init__(self,StartingLayout,listOfMoves):
        self.StartingLayout=StartingLayout
        self.listOfMoves
        self.responseMove,self.newmove,self.gameProgress=generateAMoveToReturnToThePlayer(listOfMoves, StartingLayout)
    
    def DatabaseUpdate(self):
        if self.newmove==True:
            updateDatabase(self.StartingLayout,self.listOfMoves,self.newmove,self.gameProgress)
        
#gameObject=game(StartingLayout,listOfMoves)
#gameObject.DatabaseUpdate()
#del gameObject