from .findWeights import findWeights

def findImportantPieces(boardLayout):
    weights=[['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT']]
    for j in range(8):
        for i in range(8):
            if (not boardLayout[j][i]=='MT') and weights[j][i]=='MT':
                weights=findWeights(boardLayout, [i,j], weights)
    return weights