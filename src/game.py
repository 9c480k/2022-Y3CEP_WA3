#deck object made of tile objects 
#black and white pieces as objects 
#use 2d lists/dicts
import gameSave
from time import sleep

class Tile(): 
    def __init__(self): 
        self.appearance = "|-|" #default unoccupied appearance + status
        self.occupied = False

    def assignPiece(self, pieceColour):
        if pieceColour == "black":  #determine its graphical representation based on its colour (black piece or white piece)
            self.appearance = "|○|"
        elif pieceColour == "white":
            self.appearance = "|●|"

        self.colour = pieceColour #stores its colour so that it is easily accessible by other methods
        self.occupied = True #change status to occupied

    def __repr__(self): #when the board with tiles is printed out, it will appear as a symbol instead of <main: classObject Tile> or something like that
        return self.appearance 

def isNextToTile(deck, column, row): #checks whether the position(column, row) is surrounded by at least one occupied tile

    #what this code does is basically run through all the tiles that surround a position, until it finds a occupied tile and returns true 
    #if nothing is triggered, it will ultimately return false, meaning placing a tile at the position is invalid
    '''
    |check||check||check|
    |check|position||check|
    |check||check||check|
    
    standard checking (different if position is on one of the four sides of the board)'''

    if row == 0: #top row
        if column == 0 and ((deck[row+1][column]).occupied == True or (deck[row][column+1]).occupied == True or (deck[row+1][column+1]).occupied == True): #top left corner
            return True 
        elif column == 7 and ((deck[row+1][column]).occupied == True or (deck[row][column-1]).occupied == True or (deck[row+1][column-1]).occupied == True): #top right corner
            return True
        elif column != 0 and column != 7: 
            if ((deck[row][column-1]).occupied == True) or ((deck[row][column+1]).occupied == True): #checks left and right of position 
                return True

            for i in range(3):
                if ((deck[row+1][column-1+i]).occupied == True):  #checks bottom three tiles in the row below position
                    return True
            
    elif row == 7: #bottom row 
        if column == 0 and ((deck[row-1][column]).occupied == True or (deck[row][column+1]).occupied == True or deck[row-1][column+1].occupied == True): #bottom left corner
            return True 
        elif column == 7 and ((deck[row-1][column]).occupied == True or (deck[row][column-1]).occupied == True or deck[row-1][column-1].occupied == True): #bottom right corner
            return True
        elif column != 0 and column != 7: 

            if ((deck[row][column-1]).occupied == True) or ((deck[row][column+1]).occupied == True): #checks left and right of position
                return True

            for i in range(3):
                if ((deck[row-1][column-1+i]).occupied == True): #checks top three tiles in the row above position
                    return True

    elif column == 0: #left column
        if ((deck[row][column+1]).occupied == True): #check right 
            return True

        for i in range(2):
            if ((deck[row-1][column+i]).occupied == True) or ((deck[row+1][column+i]).occupied == True): #checks top 2 and bottom 2 tiles 
                return True

    elif column == 7: #right column
        if ((deck[row][column-1]).occupied == True): #checks left
            return True

        for i in range(2):
            if ((deck[row-1][column-i]).occupied == True) or ((deck[row+1][column-i]).occupied == True): #checks top 2 and bottom 2 tiles 
                return True
            

    else:  #everything else 
        if ((deck[row][column-1]).occupied == True) or ((deck[row][column+1]).occupied == True): #left and right 
            return True

        for i in range(3):
            if ((deck[row-1][column-1+i]).occupied == True) or ((deck[row+1][column-1+i]).occupied == True): #top three tiles and bottom three tiles
                return True

    return False
    

def implementer(selection, pieceColour, board): #function to flip over the pieces necessary 
    changeList = []
    for i in (selection): 
        if (i.occupied == True):    #checks if the tile is already occupied         
            if (i.colour == pieceColour)  and changeList != []: 
                [j.assignPiece(pieceColour) for j in changeList] #flips all tiles in changeList to the opposing colour 

                board.captured = True #tells deck that this is a valid move as something would be captured
                break

            elif i.colour == pieceColour: #if there is a piece of the same colour next to the position, no capture is possible along that line
                break

            else: #to catch tiles of the opposing colour to be flipped
                changeList.append(i)

        else: #if the tile is not occupied, anything after it and itself can be disregarded, because 
            break   

def leftCheck(board, deck, column, row, pieceColour): #obtains all tiles to the left of the positon
    selection = []
    for i in (deck[row][column-1::-1]): 
        selection.append(i)

    implementer(selection, pieceColour, board)


def rightCheck(board, deck, column, row, pieceColour): #obtains all tiles to the right of the position 
    selection = []    
    for i in (deck[row][column+1:]):
        selection.append(i)

    implementer(selection, pieceColour, board)

def upCheck(board, deck, column, row, pieceColour): #obtains all tiles upwards of the position
    selection = []
   
    for i in (range(row)):
        if (row-1-i) == -1: #makes sure that the list doesnt go out of index just in case 
            break
        else:
            selection.append(deck[row-1-i][column])
   
    implementer(selection, pieceColour, board)
    

def downCheck(board, deck, column, row, pieceColour, deckSize =8): #obtains all tiles below the position
    selection = []
    
    for i in (range(deckSize - row-1)):
        if (row+1+1) > 7:  #makes sure that the list doesnt go out of index just in case 
            break
        else:
            selection.append(deck[row+1+i][column])   
        

    implementer(selection, pieceColour, board)


def topLeftDiagonalCheck(board, deck, column, row, pieceColour): #obtains all tiles upward and diagonally left of the position
    if column == 0 or column == 1: #no pieces can be captured on the left diagonal plane if position is too left 
        return           
    else:
        selection = []
        for i in (range(row)):
            if (row-1-i) == -1 or (column-1-i) == -1: #makes sure that the code terminates before it goes out of bounds 
                break
            else:
                selection.append(deck[row-1-i][column-1-i]) 

    
    implementer(selection, pieceColour, board)

def bottomRightDiagonalCheck(board, deck, column, row, pieceColour, deckSize = 8): #obtains all tiles below and diagonally right of position
    if column == deckSize-1 or column == deckSize -2 : #no pieces can be captured if position is too right 
        return     
    else:
        selection = []
        for i in (range(7-row)):
            if (row+1+i) > 7 or (column+1+i) > 7: #makes sure that code terminates before it goes out of bounds 
                break            
            else:
                selection.append(deck[row+1+i][column+1+i])
        

    implementer(selection, pieceColour, board)


def topRightDiagonalCheck(board, deck, column, row, pieceColour, deckSize = 8):   #obtains all tiles above and diagonally right of position  
    if column == 7 or column == 6: #no pieces can be captured if position is too right 
        return 
    
    else:
        selection = []
        for i in (range(row)):
            if (row-1-i) == -1 or (column+1+i) > 7: #makes sure that code terminates before it goes out of bounds 
                break
            else:
                selection.append(deck[row-1-i][column+1+i])

    implementer(selection, pieceColour, board)


def bottomLeftDiagonalCheck(board, deck, column, row, pieceColour, deckSize = 8):    #obtains all tiles below and diagonally left of position  
    if column == 0 or column == 1:  #no pieces can be captured if position is too left 
        return     
    else:
        selection = []
        
        for i in (range(7-row)):
            if (row+1+i) > 7 or (column-1-i) == -1: #makes sure that code terminates before it goes out of bounds 
                break
            else:                
                selection.append(deck[row+1+i][column-1-i])           
        

    
    implementer(selection, pieceColour, board)



class Deck:
    def __init__(self, size = 8):        
        self.deck = []        
        for row in range(size): #setting up a 2d list for the deck 
            self.deck.append([Tile() for column in range(size)])

        self.retrieveTile(3, 4).assignPiece("black") #setting up the starting pieces on the board 
        self.retrieveTile(4, 3).assignPiece("black")
        self.retrieveTile(3, 3).assignPiece("white")
        self.retrieveTile(4, 4).assignPiece("white")
                  
        

    def retrieveTile(self, column, row):
        #returns the tile at the particular position on the board
        return self.deck[row][column]
        
    def placePiece(self, column, row, pieceColour):  #places a piece on the board, returns False if invalid 
        self.captured = False          
        selectedTile = self.retrieveTile(column, row)  

        if (selectedTile.occupied == True or isNextToTile(self.deck, column, row) == False): #checks if it is placing on a occupied tile, or if there are no tiles next to the position            
            return False

        else:         
            #checks to see if anything needs to be flipped 
            leftCheck(self,self.deck, column, row, pieceColour)
            rightCheck(self,self.deck, column, row, pieceColour)
            upCheck(self,self.deck, column, row, pieceColour)
            downCheck(self,self.deck, column, row, pieceColour)
            topLeftDiagonalCheck(self,self.deck, column, row, pieceColour)
            topRightDiagonalCheck(self,self.deck, column, row, pieceColour)
            bottomLeftDiagonalCheck(self,self.deck, column, row, pieceColour)
            bottomRightDiagonalCheck(self,self.deck, column, row, pieceColour)             
        
            if self.captured == False:  #if nothing is flipped, it is an invalid move 
                return False
            else: 
                selectedTile.assignPiece(pieceColour) #finally changes colour of position

        

    def __repr__(self): #visual representation of board 
        count = 0
        print("| ||0||1||2||3||4||5||6||7|")      
        for i in self.deck:            
            print(f"|{str(count)}|" + "".join([repr(j) for j in i])) #removes the square brackets that printing a list would result in 
            count += 1 
        return ""

class gameControl(gameSave.saveStorer):
    def __init__(self, player1, player2, deck):        
        #initialising some variables
        self.board = deck 
        self.skipTimes = 0
        self.skipTurn = []
        self.passEnd = False
        self.turnCount = 1

        if player1.turn == 1: #checks if player 1 indicated they want to go first
            self.first = player1.username
            self.second = player2.username
        else: 
            self.first = player2.username  #i realise the names seem contradictory but it works i swear
            self.second = player1.username

        
        self.turn = self.first #first person's turn 
        #self.turn is a variable i use to keep track of whose turn it is 

    def changeTurn(self): #increments turn count, changes who is supposed to go next 
        if (self.turnCount) % 2 == 1: #flips turn 
            self.turn = self.second            
        else: 
            self.turn = self.first

        self.turnCount += 1 

    def retrieveGame(self): 

        if self.retrieveSave() == False: #no save detected
            return False 
        else:           
            #extracting data from save
            self.turnCount = int(self.output[len(self.output)-1])
            dataList = self.output[len(self.output)-2].split(",")            
            self.first, self.second, self.turn = dataList[0], dataList[1], dataList[2]                  
            self.output = self.output[:len(self.output)-2]

            
            self.output = self.output[0]
            self.output = self.output.split(",")            
            self.save = []
            row = []

            for i in self.output: #converts deck to the 2d list of tiles again, and assigns pieces 

                if len(row) == 8: #checks if a row has been filled                                       
                    self.save.append(row) #adds the row to the deck                    
                    row = [] #begins filling up a new row 
                    
                    
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


            self.save.append(row) #the for loop doesnt run enough times to increment the last row 

            self.board.deck = self.save  #the saved deck is now the current deck in play           
            print("Save retrieved.")
            sleep(2)


    def save(self): #saves current game 
        self.saveGame(self.board.deck, self.first, self.second, self.turn, self.turnCount) #calls save function 

    def skip(self): #passing feature 
        self.skipTimes += 1
        self.skipTurn.append(self.turnCount)        

        if self.skipTimes == 2: #a skip has been triggered twice 
            if self.skipTurn[0] + 1 == self.skipTurn[1]: #checks if it was caused by both players (ie if it was successive passes)
                self.passEnd = True
                
            else: 
                self.skipTimes = 0 #resets the trigger
                self.skipTurn = []

        


    def gameEnd(self): #function to calculate winner 
        self.user1Score = 0 #for the first player (black)
        self.user2Score = 0 #for the second player(white)
        self.winner = ""
        for i in self.board.deck:
            for j in i: 
                if repr(j) == "|-|":
                    pass
                elif repr(j) == "|○|": #black score increment 
                    self.user1Score += 1 
    
                elif repr(j) == "|●|": #white score increment 
                    self.user2Score += 1 
                
        if self.user1Score > self.user2Score: #black > white
            self.winner = self.first 
        elif self.user2Score > self.user1Score: #white > black 
            self.winner =  self.second 
        elif self.user2Score == self.user1Score: #equal scores
            self.winner = "draw"  


    def rules(self): #prints out the rules
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
        
                


