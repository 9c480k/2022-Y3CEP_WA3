class saveStorer:               
    def saveGame(self, deck, user1, user2, turnCount):   
        self.deck = []     
        for i in deck: 
            for j in i: 
                self.deck.append(repr(j))
        self.deck = self.deck.join("") 
        print(self.deck)

        with open("save.txt", "w") as file: 
            file.write(f"{self.deck}\n") 
            file.write(f"{[user1, user2]}\n")
            file.write(str(turnCount))


    def retrieveSave(self): 
        with open("save.txt", "r") as file: 
            lines = file.readlines()
            self.output = [line.rstrip() for line in lines]
            print(self.output)
            


        if self.output == "": 
            return False
        else: 
            return True 

x = "hello"
print(x[1])