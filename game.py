#deck object made of tile objects 
#black and white pieces as objects 
#use 2d lists/dicts
import gameSave
from time import sleep

class Tile():
    def __init__(self): 
        self.appearance = "|-|"
        self.occupied = False

    def assignPiece(self, pieceColour):
        if pieceColour == "black":
            self.appearance = "|○|"
        elif pieceColour == "white":
            self.appearance = "|●|"

        self.colour = pieceColour
        self.occupied = True

    def __repr__(self):
        return self.appearance 

def isNextToTile(deck, column, row):
    if row == 0: #top row
        if column == 0 and ((deck[row+1][column]).occupied == True or (deck[row][column+1]).occupied == True or (deck[row+1][column+1]).occupied == True):
            return True 
        elif column == 7 and ((deck[row+1][column]).occupied == True or (deck[row][column-1]).occupied == True or (deck[row+1][column-1]).occupied == True):
            return True
        elif column != 0 and column != 7: 
            if ((deck[row][column-1]).occupied == True) or ((deck[row][column+1]).occupied == True): 
                return True

            for i in range(3):
                if ((deck[row+1][column-1+i]).occupied == True):
                    return True
            
    elif row == 7: #bottom row 
        if column == 0 and ((deck[row-1][column]).occupied == True or (deck[row][column+1]).occupied == True or deck[row-1][column+1].occupied == True):
            return True 
        elif column == 7 and ((deck[row-1][column]).occupied == True or (deck[row][column-1]).occupied == True or deck[row-1][column-1].occupied == True):
            return True
        elif column != 0 and column != 7: 

            if ((deck[row][column-1]).occupied == True) or ((deck[row][column+1]).occupied == True): 
                return True

            for i in range(3):
                if ((deck[row-1][column-1+i]).occupied == True):
                    return True

    elif column == 0: #left column
        if ((deck[row][column+1]).occupied == True): 
            return True

        for i in range(2):
            if ((deck[row-1][column+i]).occupied == True) or ((deck[row+1][column+i]).occupied == True): 
                return True

    elif column == 7: #right column
        if ((deck[row][column-1]).occupied == True): 
            return True

        for i in range(2):
            if ((deck[row-1][column-i]).occupied == True) or ((deck[row+1][column-i]).occupied == True): 
                return True
            

    else: 
        if ((deck[row][column-1]).occupied == True) or ((deck[row][column+1]).occupied == True): 
            return True

        for i in range(3):
            if ((deck[row-1][column-1+i]).occupied == True) or ((deck[row+1][column-1+i]).occupied == True): 
                return True

    return False
    

def implementer(selection, pieceColour, board):
    changeList = []
    for i in (selection):
        if (i.occupied == True):            
            if (i.colour == pieceColour)  and changeList != []:
                [j.assignPiece(pieceColour) for j in changeList]
                board.captured = True
                break
            elif i.colour == pieceColour: 
                break
            else: 
                changeList.append(i)
        else: 
            break   

def leftCheck(board, deck, column, row, pieceColour):
    selection = []
    for i in (deck[row][column-1::-1]):
        selection.append(i)

    implementer(selection, pieceColour, board)


def rightCheck(board, deck, column, row, pieceColour): 
    selection = []    
    for i in (deck[row][column+1:]):
        selection.append(i)

    implementer(selection, pieceColour, board)

def upCheck(board, deck, column, row, pieceColour):
    selection = []
   
    for i in (range(row)):
        if (row-1-i) == -1: 
            break
        else:
            selection.append(deck[row-1-i][column])
   
    implementer(selection, pieceColour, board)
    

def downCheck(board, deck, column, row, pieceColour, deckSize =8):
    selection = []
    
    for i in (range(deckSize - row-1)):
        if (row+1+1) > 7: 
            break
        else:
            selection.append(deck[row+1+i][column])   
        

    implementer(selection, pieceColour, board)


def topLeftDiagonalCheck(board, deck, column, row, pieceColour): 
    if column == 0 or column == 1: 
        return           
    else:
        selection = []
        for i in (range(row)):
            if (row-1-i) == -1 or (column-1-i) == -1:
                break
            else:
                selection.append(deck[row-1-i][column-1-i])

    
    implementer(selection, pieceColour, board)

def bottomRightDiagonalCheck(board, deck, column, row, pieceColour, deckSize = 8): 
    if column == deckSize-1 or column == deckSize -2 : 
        return     
    else:
        selection = []
        for i in (range(7-row)):
            if (row+1+i) > 7 or (column+1+i) > 7:
                break            
            else:
                selection.append(deck[row+1+i][column+1+i])
        

    implementer(selection, pieceColour, board)


def topRightDiagonalCheck(board, deck, column, row, pieceColour, deckSize = 8):     
    if column == 7 or column == 6: 
        return 
    
    else:
        selection = []
        for i in (range(row)):
            if (row-1-i) == -1 or (column+1+i) > 7:
                break
            else:
                selection.append(deck[row-1-i][column+1+i])

    implementer(selection, pieceColour, board)


def bottomLeftDiagonalCheck(board, deck, column, row, pieceColour, deckSize = 8):    
    if column == 0 or column == 1: 
        return     
    else:
        selection = []
        
        for i in (range(7-row)):
            if (row+1+i) > 7 or (column-1-i) == -1:
                break
            else:                
                selection.append(deck[row+1+i][column-1-i])           
        

    
    implementer(selection, pieceColour, board)



class Deck:
    def __init__(self, size = 8):        
        self.deck = []        
        for i in range(size):
            self.deck.append([Tile() for j in range(size)])

        self.retrieveTile(3, 4).assignPiece("black")
        self.retrieveTile(4, 3).assignPiece("black")
        self.retrieveTile(3, 3).assignPiece("white")
        self.retrieveTile(4, 4).assignPiece("white")
                  
        

    def retrieveTile(self, column, row):
        #returns the tile at the particular position on the board
        return self.deck[row][column]
        
    def placePiece(self, column, row, pieceColour):  
        self.captured = False          
        selectedTile = self.retrieveTile(column, row)  
        if (selectedTile.occupied == True or isNextToTile(self.deck, column, row) == False): #bug: does not work for first move  
            print(isNextToTile(self.deck, column, row) == False)
            return False
        else:         
            
            leftCheck(self,self.deck, column, row, pieceColour)
            rightCheck(self,self.deck, column, row, pieceColour)
            upCheck(self,self.deck, column, row, pieceColour)
            downCheck(self,self.deck, column, row, pieceColour)
            topLeftDiagonalCheck(self,self.deck, column, row, pieceColour)
            topRightDiagonalCheck(self,self.deck, column, row, pieceColour)
            bottomLeftDiagonalCheck(self,self.deck, column, row, pieceColour)
            bottomRightDiagonalCheck(self,self.deck, column, row, pieceColour)             
        
            if self.captured == False:                 
                return False
            else: 
                selectedTile.assignPiece(pieceColour)

        

    def __repr__(self): 
        count = 0
        print("| ||0||1||2||3||4||5||6||7|")      
        for i in self.deck:            
            print(f"|{str(count)}|" + "".join([repr(j) for j in i]))
            count += 1 
        return ""

class gameControl(gameSave.saveStorer):
    def __init__(self, player1, player2, deck):        
        self.board = deck
        self.skipTimes = 0
        self.skipTurn = []
        self.passEnd = False

        if player1.turn == 1: 
            self.first = player1.username
            self.second = player2.username
        else: 
            self.first = player2.username  
            self.second = player1.username

        self.turnCount = 1
        self.turn = self.first

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
            self.ongoing = True 
            self.turnCount = int(self.output[len(self.output)-1])
            dataList = self.output[len(self.output)-2].split(",")            
            self.first, self.second, self.turn = dataList[0], dataList[1], dataList[2]                  
            self.output = self.output[:len(self.output)-2]

            
            self.output = self.output[0]
            self.output = self.output.split(",")            
            self.save = []
            row = []

            for i in self.output:
                if len(row) == 8:                                        
                    self.save.append(row)                    
                    row = []
                    
                    
                if i == "|-|":
                    row.append(Tile())                    
                    
                elif i == "O": 
                    x = Tile()
                    x.assignPiece('white')
                    row.append(x)
                
                elif i == "X":
                    x = Tile()
                    x.assignPiece('black')
                    row.append(x)


            self.save.append(row)
            self.board.deck = self.save            
            print("Save retrieved.")
            sleep(2)


    def save(self): 
        self.saveGame(self.board.deck, self.first, self.second, self.turn, self.turnCount)

    def skip(self):
        self.skipTimes += 1
        self.skipTurn.append(self.turnCount)        

        if self.skipTimes == 2:
            if self.skipTurn[0] + 1 == self.skipTurn[1]:
                self.passEnd = True
                
            else: 
                self.skipTimes = 0 
                self.skipTurn = []

        


    def gameEnd(self): 
        self.user1Score = 0 
        self.user2Score = 0 
        self.winner = ""
        for i in self.board.deck:
            for j in i: 
                if repr(j) == "|-|":
                    pass
                elif repr(j) == "|○|":
                    self.user1Score += 1 
    
                elif repr(j) == "|●|": 
                    self.user2Score += 1 
                
        if self.user1Score > self.user2Score: 
            self.winner = self.first 
        elif self.user2Score > self.user1Score: 
            self.winner =  self.second 
        elif self.user2Score == self.user1Score: 
            self.winner = "draw"  


    def rules(self):
        print("\nIn Othello, black (|○|) goes first, followed by white (|●|)")
        sleep(2)
        print("If your piece surrounds a piece of the opposing colour, the piece will be flipped\n")
        sleep(2)
        print("Example:\n")        
        print("|○||●||●||-|")
        print("|○||○||○||○|")
        sleep(2)
        print("\nThis applies in all directions, including diagonals")
        print("\nIn addition, a move is only valid when it flips over one or more pieces of the opposing side")
        sleep(2)
        print("\nIf you are unable to move, you may pass.")
        print("However, the game will immediately end if a player chooses to pass right after the other player has done so.\n")
        sleep(2)
        
                


#rudimentary code to play the game (assuming you always give the correct inputs otherwise it crashes)
'''x = Deck()
y = gameControl()
y.first = "a"
y.second = "b"
y.board = x

for i in range(7): 

    if i%2 ==0: 
        colour = "black"
    else: 
        colour = "white"
    print(x)
    move = input("move")

    if x.placePiece(int(move[0]), int(move[1]), colour) == False: 
        print(x)
        print("no")
    else: 
        print((x.retrieveTile(int(move[0]), int(move[1]))).colour)

print(y.gameEnd())
print(y.user1Score)
print(y.user2Score)'''

'''
x = Deck()
y = gameControl()
y.first = "abc"
y.second = "bcd"
y.board = x
y.turn = "abc"
y.turnCount = 3

x.retrieveTile(2, 5).assignPiece("black")
x.retrieveTile(1, 6).assignPiece("black")
x.retrieveTile(5, 2).assignPiece("white")
x.retrieveTile(6, 1).assignPiece("black")
print(x)

x.placePiece(0, 7, "white")
print(x)
y.save()
y.retrieveSave()
print(x)
print(y.turn)
'''





