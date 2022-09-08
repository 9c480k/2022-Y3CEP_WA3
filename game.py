#deck object made of tile objects 
#black and white pieces as objects 
#use 2d lists/dicts

from gameSave import saveStorer

class Tile():
    def __init__(self): 
        self.appearance = "|-|"
        self.occupied = False

    def assignPiece(self, pieceColour):
        if pieceColour == "black":
            self.appearance = "|●|"
        elif pieceColour == "white":
            self.appearance = "|○|"

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



class Deck:
    def __init__(self, gameController, size = 8,):
        self.gameController = gameController
        self.deck = []
        if self.gameController.ongoing == False:
            for i in range(size):
                self.deck.append([Tile() for j in range(size)])
        else: 
            self.deck = self.gameController.save            
        

    def retrieveTile(self, column, row):
        #returns the tile at the particular position on the board
        return self.deck[row][column]
        
    def placePiece(self, column, row, pieceColour):            
        selectedTile = self.retrieveTile(column, row)  
        if (selectedTile.occupied == True or validMoveCheck(self.deck, column, row) == False) and (self.gameController).turnCount != 1: #bug: does not work for first move  
            return False
        else: 
            selectedTile.assignPiece(pieceColour)
            self.gameController.changeTurn()

        leftCheck(self.deck, column, row, pieceColour)
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

class gameControl(saveStorer):
    def __init__(self, player1, player2):        
        if player1.turn == 1: 
            self.first = player1.username
            self.second = player2.username
        else: 
            self.first = player2.username  
            self.second = player1.username

        self.turnCount = 1

    def changeTurn(self):
        if (self.turnCount) % 2 == 1: 
            self.turn = self.second            
        else: 
            self.turn = self.first

        self.turnCount += 1 

    def retrieveGame(self): 
        if self.retrieveSave() == False: 
            return False 
        else: 
            print(self.output)
            self.turnCount = int(self.output[len(self.output)-1])
            self.first, self.second = (self.output[len(self.output)-2])[0], (self.output[len(self.output)-2])[1]            
            self.output = self.output[:len(self.output)-3]

            self.save = []
            row = []
            for i in self.output:
                if len(row) == 8: 
                    self.save.append(row)
                    row = []
                    
                if i == "|-|":
                    row.append(Tile())
                elif i == "|●|": 
                    x = Tile()
                    x.assignPiece('black')
                    row.append(x)
                
                elif i == "|○|":
                    x = Tile()
                    x.assignPiece('white')
                    row.append(x)
                    
            print(self.save)
            return self.save
        

    def save(self): 
        self.saveGame()

    def gameEnd(self): 
        pass
    

x = [Tile()]
print(x[0])
print(repr(x[0]) == "|-|")













