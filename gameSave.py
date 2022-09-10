class saveStorer:               

    def saveGame(self, deck, user1, user2, turn, turnCount):   
        self.deck = []     
        for i in deck: 
            for j in i: 
                if repr(j) == "|○|":
                    self.deck.append("X")
                elif repr(j) == "|●|":
                    self.deck.append("O")
                else: 
                    self.deck.append(repr(j))

        self.deck = ",".join(self.deck)
        

        with open("save.txt", "w") as file:             
            file.write(self.deck + "\n") 
            file.write(f"{[user1, user2, turn]}\n")
            file.write(str(turnCount))

              


    def retrieveSave(self): 
        with open("save.txt", "r") as file: 
            lines = file.readlines()

            if lines == []: 
                return False 
    
            self.output = [line.rstrip() for line in lines]
            

        with open("save.txt", "w") as file: 
            file.write("")


        
        return True 


    