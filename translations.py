def isintager(x):
    try:
        x=int(x)
    except:
        return False
    else:
        return True


def to_xenonnumber(gamelist):

    primeNumbers=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283.293,307,311,313]
    Pieceslist=['00','WR','WN','WB','WQ','WK','WP','BR','BN','BB','BQ','BK','BP']
    xenonnumber=1
    n1=0                                                                                              #announcing variables
    n2=0
    n3=0

    for i in range(0,64):                                                                               #there is garunteed to be 36 items in the game list inputted and we need to translate all of them

        n1=int(primeNumbers[i])                                                                       #getting the actual numbers needed for the calculation from the list that they're in
        n2=int(Pieceslist.index(gamelist[i]))

        n3=n1**n2                                                                                     #the respective prime number to the power of the xenon number for the piece at the corresponding place, multiplied by all the others goves the unique xenon number for the frame
        xenonnumber=xenonnumber*n3
        print(i,n1,n2,n3,xenonnumber)

    return xenonnumber

def to_gamelist(xenonnumber):

    primeNumbers=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283.293,307,311,313]
    Pieceslist=['00','WR','WN','WB','WQ','WK','WP','BR','BN','BB','BQ','BK','BP']
    gamelist=[]                                                                                         #announcing the variables
    n2=0
    numcount=0
    Piece=''

    for i in range (64):

        n2=primeNumbers[i]                                                                              #getting the corresponging number reqired from a list

        numcount=0

        while xenonnumber%n2==0:                                                                         #finding out how many of these are in the xenon number

            numcount+=1                                                                                 #the prime factorisation of the xenon number corresponds to the piece at the square corresponding to the prime number used. the prime numbers are tested from smalled to lagest resulting in the pieces from A1 to H8 on the chess board in order
            xenonnumber=xenonnumber//n2
        Piece=Pieceslist[numcount]                                                                       #translating the piece xenon number to the piece it corresponds to
        gamelist.append(Piece)
    
    return gamelist

def toCoOrdinates(inputTuple):
    letters=[A,B,C,D,E,F,G,H]
    return letters[(inputTuple[0])]+str(8-inputTuple[1])

def toTuple(inputString):
    return [int(letters.index(InputCoOrdinates[0])),8-int(InputCoOrdinates[1])]