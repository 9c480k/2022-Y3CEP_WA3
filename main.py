
import game
import storage 





'''side note here
if all the imports are not working, using 'pip install gspread, gspread_dataframe, oauth2client, pandas' should work '''

def createAccount():

    while True: 
        try: 
            username = input("\nEnter the username you want to use (or type q to login):")
            if username == "q":
                return login()
            elif storage.checkUsername(username) == True: 
                raise TypeError            
                
            
        except TypeError:
            print("Your username has already been registered. Type q to exit and login or try using a different username") 
        
        else: 
            break 

    while True: 
        try:
            password = input("\nEnter the password you want to use. Your password should be at least 8 letters long:")
            if password == "q":
                return login()
            elif (len(password) >= 8) == False: 
                raise ValueError 
                    
        except ValueError:
            print("Your password needs to be at least 8 letters long. Please try again, or press q to login to an existing account")
                
        else: 
            break 
            


    storage.addUsername(username, password)
    return username


def login():   

    while True: 
        try: 
            username = input("\nWhat is your username? (type q to to make a new account)")
            if username == "q":
                return createAccount() 
            elif storage.checkUsername(username) == False: 
                raise ValueError        
                

        except ValueError:
            print("Your username was not found. Plase try again, or press q to make a new account.")

        else: 
            break 
    while True:
        try: 
            password = input("\nWhat is your password? (type q to make a new account)")
            if password == "q":
                return createAccount()
            elif storage.checkPassword(username, password) == True: 
                print(f"\nSuccessfully logged in as {username}")
            else: 
                raise TypeError

        except TypeError:
            print("Your password does not match this account. Please try again, or press q to make a new account")

        else: 
            break
        

    return username 

class Player():
    def __init__(self, username, turn):
        self.username = username 
        self.turn = turn 
        if turn == 1: 
            self.colour = "black"
        else: 
            self.colour = "white"
    

print("Loading game...\n")            
storage.refreshData()
global player1
global player2
currentPlayers = []


print("Welcome to a game of Othello!")
print("\nVisit README.md at https://github.com/9c480k/2022-Y3CEP_WA3/blob/main/documents/README.md for links to the playerbase log, as well as other useful information")
print("\nProceeding to user login and registration...\n")
for i in range(2):    
    while True:
        try:
            accountCheck = input("Do you have an account? (y/n)").strip()
            if accountCheck not in ["y", "n"]: 
                raise ValueError

        except ValueError:
            print("Please try again.")

        else:
            break

    if accountCheck == "y": 
        while True: 
            try: 
                username = login()
                if username in currentPlayers: 
                    raise ValueError
                else: 
                    break

            except ValueError:
                print("Successful login rejected.") 
                print("The user is currently logged in. Sign in as another user")
    else: 
        username = createAccount()

    if i == 0: 
        while True:
            try: 
                turnCheck = input("\nWould you like to go first? (y/n)").strip()
                if turnCheck == "y": 
                    player1 = Player(username, 1)
                    break
                elif turnCheck == "n": 
                    player1 = Player(username, 2)
                    break
                else: 
                    raise ValueError

            except ValueError: 
                print("Please provide valid input") 

        currentPlayers.append(player1.username)
        print("\nProceeding to login for second player.\n")


    else: 
        if player1.turn == 1: 
            player2 = Player(username, 2)
        else: 
            player2 = Player(username, 1)

        currentPlayers.append(player2.username)

#initialisation
board = game.Deck()
gameController = game.gameControl(player1, player2, board)
print("Saving data...")
storage.saveData()

gameController.rules()
print("\n")
#automatically retrieves saves if there are any 
gameController.retrieveGame()




exit = False
#game loop 
for i in range(61):        
    if gameController.turnCount == 61 or gameController.passEnd == True: 
        gameController.gameEnd()
        if gameController.winner == "draw": 
            print("The game ended in a draw! Both players lose.")
            storage.changeStoredStats(gameController.first, "gl")
            storage.changeStoredStats(gameController.second, "gl")

        else:             
            print(f"The winner of this game is {gameController.winner}")
            storage.changeStoredStats(gameController.winner, "gw")

            if gameController.winner == gameController.first:                
                storage.changeStoredStats(gameController.second, "gl") 
            else:                 
                storage.changeStoredStats(gameController.first, "gl")

        print("Game ended. Updating database...")
        storage.saveData()
        break   

    
    currentUser = gameController.turn

    if currentUser == player1.username: 
        
        currentColour = player1.colour
    else:         
        currentColour = player2.colour

    print(f"\nIt is now {currentUser}'s turn!\n")

    while True: 
        try:             
            print(board)                       
            print("If you would like to quit and save your game, type q. If you would like to pass, press p")
            print("If you would like to revisit the rules, type r")
            move = input("\nPlease enter the column and row of your move in the format columnrow (e.g. 12):")  

            if move == "q":                 
                exit = True                 
                break 
            elif move == "p": 
                gameController.skip()
                break
            elif move == "r":
                raise ValueError
            elif move.isnumeric() == False: 
                raise TypeError

            elif board.placePiece(int(move[0]), int(move[1]), currentColour) == False: 
                raise Exception
             
            break        
                
        except ValueError:
            gameController.rules()           
        
        except TypeError: 
            print("\n\nPlease provide valid input.")

        except Exception: 
            print("\n\nTile not available. Try another move.")

    if exit == True: 
        gameController.save()
        print("Game saved locally.")
        break
    else:        
        gameController.changeTurn()


   




    


            







    




