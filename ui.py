import game
import storage 





def createAccount():

    while True: 
        try: 
            username = input("Enter the username you want to use.")
            if username == "q":
                login()
            elif storage.checkUsername == True: 
                raise TypeError
            else: 
                try:
                    password = input("Enter the password you want to use. Your password should be at least 8 letters long")
                    if password == "q":
                        login()
                    elif len(password) >= 8 == False: 
                        raise ValueError 
                    
                except ValueError:
                    print("Your password needs to be at least 8 letters long. If you have forgotten your password, press q to make a new account")
                
                else: 
                    break 
            
            
        except TypeError:
            print("Your username has already been registered. Type q to exit and login or try using a different username") 
        
        else: 
            storage.addUsername(username, password)
            return username


def login():   

    while True: 
        try: 
            username = input("What is your username?")
            if username == "q":
                createAccount() 
            elif storage.checkUsername == False: 
                raise ValueError 
            else:
                try: 
                    password = input("What is your password?")
                    if password == "q":
                        createAccount()
                    elif storage.checkPassword == True: 
                        print(f"Successfully logged in as {username}")
                    else: 
                        raise TypeError

                except TypeError:
                    print("Your password does not match this account. Please try again, or press q to make a new account")

                else: 
                    break

        except ValueError:
            print("Your username was not found. Plase try again, or press q to make a new account.")

        else: 
            return username


class Player():
    def __init__(self, username, turn):
        self.username = username 
        self.turn = turn 
        if turn == 1: 
            self.colour = "white"
        else: 
            self.colour = "black"
    

            
storage.refreshData()
global player1
global player2


print("Welcome to a game of Othello!")

for i in range(2):    
    while True:
        try:
            accountCheck = bool(input("Do you have an account? True/False").strip())
        except ValueError:
            print("Please try again. Enter True/False (capital letter included)")
        else:
            break

    if accountCheck == True: 
        username = login()
    else: 
        username = createAccount()

    if i == 1: 
        try: 
            turnCheck = input("Would you like to go first? y/n")
            if turnCheck == "y": 
                player1 = Player(username, 1)
            elif turnCheck == "n": 
                player1 = Player(username, 2)
            else: 
                raise ValueError

        except ValueError: 
            print("Please provide valid input") 


    else: 
        if player1.turn == 1: 
            player2 = Player(username, 2)
        else: 
            player2 = Player(username, 1)

gameController = game.gameControl(player1, player2)
board = game.Deck
while True: 
    try: 
        input = input("There is a save loaded locally. Continue? (y/n)")
        if input == "n": 
            break 
        elif input == "y": 
            gameController.retrieveGame()
        else: 
            raise ValueError
    except ValueError: 
        print("Please provide valid input.")

for i in range(65):    
    if gameController.turnCount == 65: 
        gameController.gameEnd()
        if gameController.winner == "draw": 
            print("The game ended in a draw! Both players lose")
            storage.changeStoredStats(player1.username, "gl")
            storage.changeStoredStats(player2.username, "gl")

        else:             
            print(f"The winner of this game is {gameController.winner}")
            storage.changeStoredStats(gameController.winner, "gw")
            if gameController.winner == player1.username:                
                storage.changeStoredStats(player2.username, "gl") 
            else:                 
                storage.changeStoredStats(player1.username, "gl")

        break 

    if gameController.turn == player1.username: 
        currentUser = player1.username
        currentColour = "white"
    else: 
        currentUser = player2.username
        currentColour = "black"

    while True: 
        try: 
            print(f"It is now {currentUser}'s turn!")
            print("If you would like to quit and save your game, type q")
            input = input("Please enter the column and row of your move in the format columnrow (e.g. 12).")
            if input == "q": 
                pass
            elif input.isnumeric() == False: 
                raise ValueError
            else: 
                try: 
                    if board.placePiece(int(input[0]), int(input[1]), currentColour) == False: 
                        raise TypeError
                    else: 
                        break

                except TypeError: 
                    print("Tile not available. Try another move.")
        
        except ValueError: 
            print("Please provide valid input.")

   




    


            







    




