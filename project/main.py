#deck object made of tile objects 
#black and white pieces as objects 
#use 2d lists/dicts


class Tile():
    def __init__(self):
        self.appearance = "|-|"
        self.occupied = False

    def assignPiece(self, pieceColour):
        if pieceColour == "black":
            self.appearance = "|X|"
        elif pieceColour == "white":
            self.appearance = "|O|"

        self.colour = pieceColour
        self.occupied = True

    def __repr__(self):
        return self.appearance 

def validMoveCheck(deck, column, row):
    if ((deck[row][column-1]).occupied == True) or ((deck[row+1][column+1]).occupied == True): 
            return True

    for i in range(3):
        if ((deck[row-1][column-1+i]).occupied == True) or ((deck[row+1][column-1+i]).occupied == True): 
            return True

    return False
    

def leftCheck(deck, column, row, pieceColour):
    changeList = []
    for i in (deck[row][column-1::-1]):
        if (i.occupied == True):            
            if (i.colour == pieceColour):
                [j.assignPiece(pieceColour) for j in changeList]
            else: 
                changeList.append(i)
        else: 
            break        

def rightCheck(deck, column, row, pieceColour): 
    changeList = []
    for i in (deck[row][column+1:]):
        if (i.occupied == True):            
            if (i.colour == pieceColour):
                [j.assignPiece(pieceColour) for j in changeList]
            else: 
                changeList.append(i)
        else: 
            break 

def upCheck(deck, column, row, pieceColour):
    selection = []
    for i in (range(row)):
        selection.append(deck[row-1-i][column])

    changeList = []
    for i in (selection):
        if (i.occupied == True):            
            if (i.colour == pieceColour):
                [j.assignPiece(pieceColour) for j in changeList]
            else: 
                changeList.append(i)
        else: 
            break   
    

def downCheck(deck, column, row, pieceColour, deckSize =8):
    selection = []
    for i in (range(deckSize - row-1)):
        selection.append(deck[row+1+i][column])
        

    changeList = []
    for i in (selection):
        if (i.occupied == True):            
            if (i.colour == pieceColour):
                [j.assignPiece(pieceColour) for j in changeList]
            else: 
                changeList.append(i)
        else: 
            break   

def topLeftDiagonalCheck(deck, column, row, pieceColour): 
    if column == 0 or column == 1: 
        return           
    else:
        selection = []
        for i in (range(row)):
            selection.append(deck[row-1-i][column-1-i])

    changeList = []
    for i in (selection):
        if (i.occupied == True):            
            if (i.colour == pieceColour):
                [j.assignPiece(pieceColour) for j in changeList]
            else: 
                changeList.append(i)
        else: 
            break   

def bottomRightDiagonalCheck(deck, column, row, pieceColour, deckSize = 8): 
    if column == deckSize-1 or column == deckSize -2 : 
        return     
    else:
        selection = []
        for i in (range(row)):
            selection.append(deck[row+1+i][column+1+i])

    changeList = []
    for i in (selection):
        if (i.occupied == True):            
            if (i.colour == pieceColour):
                [j.assignPiece(pieceColour) for j in changeList]
            else: 
                changeList.append(i)
        else: 
            break   

def topRightDiagonalCheck(deck, column, row, pieceColour, deckSize = 8):     
    if column == deckSize-1 or column == deckSize - 2: 
        return 
    
    else:
        selection = []
        for i in (range(row)):
            selection.append(deck[row-1-i][column+1+i])

    changeList = []
    for i in (selection):
        if (i.occupied == True):            
            if (i.colour == pieceColour):
                [j.assignPiece(pieceColour) for j in changeList]
            else: 
                changeList.append(i)
        else: 
            break   

def bottomLeftDiagonalCheck(deck, column, row, pieceColour, deckSize = 8):    
    if column == 0 or column == 1: 
        return     
    else:
        selection = []
        for i in (range(row)):
            selection.append(deck[row+1+i][column-1-i])

    changeList = []
    for i in (selection):
        if (i.occupied == True):            
            if (i.colour == pieceColour):
                [j.assignPiece(pieceColour) for j in changeList]
            else: 
                changeList.append(i)
        else: 
            break   

class Deck():
    def __init__(self, size = 8):
        self.deck = []
        for i in range(size):
            self.deck.append([Tile() for j in range(size)])
        

    def retrieveTile(self, column, row):
        #returns the tile at the particular position on the board
        return self.deck[row][column]
        
    def placePiece(self, column, row, pieceColour):     
        selectedTile = self.retrieveTile(column, row)
        if selectedTile.occupied == True or validMoveCheck(self.deck, column, row) == False: 
            return
        else: 
            selectedTile.assignPiece(pieceColour)

        rightCheck(self.deck, column, row, pieceColour)
        upCheck(self.deck, column, row, pieceColour)
        downCheck(self.deck, column, row, pieceColour)
        topLeftDiagonalCheck(self.deck, column, row, pieceColour)
        topRightDiagonalCheck(self.deck, column, row, pieceColour)
        bottomLeftDiagonalCheck(self.deck, column, row, pieceColour)
        bottomRightDiagonalCheck(self.deck, column, row, pieceColour)             
        
        print(self)       

        

    def __repr__(self):
        for i in self.deck:
            print(i)
        return ""

    



   


x = Deck()
x.placePiece(1, 2, "black")
x.placePiece(2, 2, "white")
x.placePiece(3, 2, "black")
x.placePiece(3, 3, "white")
x.placePiece(3, 1, "white")
x.placePiece(2, 1, "black")
x.placePiece(4, 3, "black")
x.placePiece(0, 2, "white")
x.placePiece(4, 2, "white")







