class saveStorer:               

    def saveGame(self, deck, user1, user2, turn, turnCount):   #for storing local save 
        self.deck = []     
        for i in deck: #for loop stores the repr() of the tiles so that it can be reassembled using the repr value 
            for j in i: 
                if repr(j) == "|○|":
                    self.deck.append("X") #it didnt like it when i tried to encode the special characters so we convert them to encode friendly formats
                elif repr(j) == "|●|":
                    self.deck.append("O")
                else: 
                    self.deck.append(repr(j)) #storing repr value of tile 

        self.deck = ",".join(self.deck) #makes the list of tiles into a string 
        

        with open("save.txt", "w") as file:             
            file.write(self.deck + "\n") #stores the whole deck as one long string 
            file.write(f"{user1},{user2},{turn}\n") #stores other important information (1st user, 2nd user, which user's turn it is)
            file.write(str(turnCount)) #stores turnCount (important)

              


    def retrieveSave(self):  #for retrieving local save

        with open("save.txt", "r") as file: 
            lines = file.readlines() #retrieves list of lines 

            if lines == []: #checks if save.txt is blank (meaning there is no save stored)
                return False 
    
            self.output = [line.rstrip() for line in lines]  #removes right trailing whitespaces               

        return True 


    def clearSave(self):
        with open("save.txt", "w") as file: #deletes the save by making save.txt blank. This makes sure that the same game cannot be called up twice as a save
            file.write("")

    