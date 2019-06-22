import random
def askForParam(ask):
    a=int(input("How long would you like the " + ask +"?"))
    return a
    
def createBoard(length, width, cell):
    lengthAr=[]     
    for j in range(length):
        widthAr=[]
        for i in range(width):
            widthAr.append(cell)
        lengthAr.append(widthAr)       
    return lengthAr
def printBoardFancy(ar):
    for r in range(len(ar)):
        line=ar[r]
        for c in range (len(line)):
            print (str(line[c]) + "  ", end = "")
        print ("")
def plantBombs(ar):
    for r in range(len(ar)):
        line=ar[r]
        for c in range (len(line)):
            line[c]=random.choice([0,0,0,0,0,0,0,0,0,9])
def calculateBomb(ar,r,c,maxR,maxC):
    if(r<0 or r>=maxR or c<0 or c>=maxC):
        return 0
    if(ar[r][c]==9):
        return 1
    return 0
    
def calculateBombs(ar):
    maxR=len(ar)
    for r in range(maxR):
        line=ar[r]
        maxC=len(line)
        for c in range (maxC):
            if (ar[r][c]!=9):              
                bombs=0
                bombs=bombs+calculateBomb(ar,r-1,c-1,maxR,maxC)
                bombs=bombs+calculateBomb(ar,r-1,c,maxR,maxC)
                bombs=bombs+calculateBomb(ar,r-1,c+1,maxR,maxC)
                bombs=bombs+calculateBomb(ar,r,c-1,maxR,maxC)
                bombs=bombs+calculateBomb(ar,r,c+1,maxR,maxC)
                bombs=bombs+calculateBomb(ar,r+1,c-1,maxR,maxC)
                bombs=bombs+calculateBomb(ar,r+1,c,maxR,maxC)
                bombs=bombs+calculateBomb(ar,r+1,c+1,maxR,maxC)
                ar[r][c]=bombs

def openSpace(name):
    spaceCheck= int(input(name))-1
    return spaceCheck
    
def loseCheck(ar,blankAr,row,column):
    if(ar[row][column]==9):
        return True
    else:
        return False
def winCheck(ar,blankAr):
    global length
    global width
    for i in range(length):
        for j in range(width):
            if(ar[i][j]!=9 and blankAr[i][j]=="#"):
                return False
    return True
def openSpaces(ar,blankAr,row,column,maxR,maxC):
    if(row<0 or row>=maxR or column<0 or column>=maxC):
        return
    if(blankAr[row][column]!="#"):
        return
    blankAr[row][column]=ar[row][column]
    if(ar[row][column]!=0):
        return
    
    else:  
        openSpaces(ar,blankAr,row-1,column-1,maxR,maxC)
        openSpaces(ar,blankAr,row-1,column,maxR,maxC)
        openSpaces(ar,blankAr,row-1,column+1,maxR,maxC)
        openSpaces(ar,blankAr,row,column-1,maxR,maxC)
        openSpaces(ar,blankAr,row,column+1,maxR,maxC)
        openSpaces(ar,blankAr,row+1,column-1,maxR,maxC)
        openSpaces(ar,blankAr,row+1,column,maxR,maxC)
        openSpaces(ar,blankAr,row+1,column+1,maxR,maxC)
    
    
                
    
        
 
def game(board,blankBoard):
    win=False
    lose=False
    while(True):
        rowCheck=openSpace("row")
        columnCheck=openSpace("column")
        if(loseCheck(board,blankBoard,rowCheck,columnCheck)==True):
            print("lose")
            break
        maxR=len(board)
        maxC=len(board[0])
        openSpaces(board,blankBoard,rowCheck,columnCheck,maxR,maxC)
        if(winCheck(board,blankBoard)==True):
            print("")
            printBoardFancy(blankBoard)
            print("win")
            break
        
        print("")
        printBoardFancy(blankBoard)
    printBoardFancy(board)
         
        
        
        
        
        
        
        
length=askForParam("length")
width=askForParam("Width")
board=createBoard(length,width,0 )
plantBombs(board)
calculateBombs(board)
blankBoard=createBoard(length,width,"#")
printBoardFancy(blankBoard)
game(board,blankBoard)
