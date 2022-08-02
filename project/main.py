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
            self.appearance = "|Y|"
            
        self.colour = pieceColour
        self.occupied = True


    def __repr__(self):
        return self.appearance 


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
        selectedTile.assignPiece(pieceColour)

    def __repr__(self):
        for i in self.deck:
            print(i)
        return ""



   


x = Deck()
