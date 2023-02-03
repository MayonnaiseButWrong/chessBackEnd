from .findWeights import findWeights

def bubbleSortPieces(pieces,weights):
    flag=True
    while flag==True:
        flag=False
        for count in range(1,len(weights)):
            if weights[count-1]>weights[count]:
                temp1=weights[count-1]
                temp2=pieces[count-1]
                weights[count-1]=weights[count]
                pieces[count-1]=pieces[count]
                weights[count]=temp1
                pieces[count]=temp2
                flag=True
    return pieces

def findImportantPieces(boardLayout):
    weights=[['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT']]
    for j in range(8):
        for i in range(8):
            if (not boardLayout[j][i]=='MT') and weights[j][i]=='MT':
                weights=findWeights(boardLayout, [i,j], weights)
    i,j=0,0
    listOfPieces=[]
    listOfWeights=[]
    for j in range(8):
        for i in range(8):
                if (not boardLayout[j][i]=='MT'):
                    listOfPieces.append([i,j])
                    listOfWeights.append(weights[j][i])
    sortedList=bubbleSortPieces(listOfPieces,listOfWeights)
    wImportantPieces=[]
    bImportantPieces=[]
    wCount,bCount,pieces=0,0,0
    while (wCount+bCount)<17:
        if boardLayout[sortedList[pieces][1]][sortedList[pieces][0]][0]=='W'and wCount<9:
            wImportantPieces.append(sortedList[pieces])
            wCount+=1
        elif bCount<9:
            bImportantPieces.append(sortedList[pieces])
            bCount+=1
        pieces+=1
    return [wImportantPieces,bImportantPieces]
            
                    