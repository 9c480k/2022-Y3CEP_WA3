
import game
import storage 





'''side note here
if all the imports are not working, using 'pip install gspread, gspread_dataframe, oauth2client, pandas' should work '''

def createAccount(): #function for creating account 
    while True: 
        try: 
            username = input("\nEnter the username you want to use (or type q to login):")
            if username == "q": #if the user gives q, directs them to login 
                return login()
            elif storage.checkUsername(username) == True: #checks if there is already a user with that username
                raise TypeError            
                
            
        except TypeError:
            print("Your username has already been registered. Type q to exit and login or try using a different username") 
        
        else: 
            break 

    #proceeds on to evaluate password
    while True: 
        try:
            password = input("\nEnter the password you want to use. Your password should be at least 8 letters long:")

            if password == "q": #if the user gives q, directs them to login 
                return login()

            elif (len(password) >= 8) == False: #checks length of password
                raise ValueError 
                    
        except ValueError:
            print("Your password needs to be at least 8 letters long. Please try again, or press q to login to an existing account")
                
        else: 
            break 

    #if both username and password are valid (no exceptions thrown), will end up here          

    storage.addUsername(username, password)
    return username


def login():   #handles user login 

    while True: 
        try: 
            username = input("\nWhat is your username? (type q to to make a new account)")

            if username == "q": #if the user gives q, directs them to create another account
                return createAccount() 
            elif storage.checkUsername(username) == False: #makes sure that the user already exists
                raise ValueError        
                

        except ValueError:
            print("Your username was not found. Plase try again, or press q to make a new account.")

        else: 
            break 

    #moves on to evaluate password
    while True:
        try: 
            password = input("\nWhat is your password? (type q to make a new account)") 

            if password == "q": #if the user gives q, directs them to create another account
                return createAccount()

            elif storage.checkPassword(username, password) == True: #makes sure that the password is correct
                print(f"\nSuccessfully logged in as {username}")

            else: #any other possible inputs the user gives is wrong
                raise TypeError

        except TypeError:
            print("Your password does not match this account. Please try again, or press q to make a new account")

        else: 
            break
        
    #any data that manages to make it out of both the loops is probably correct
    return username 

class Player(): #create new class player to store individual user data 
    def __init__(self, username, turn):
        self.username = username 
        self.turn = turn 

        if turn == 1: #if the player is going first, their pieces will be black 
            self.colour = "black"
        else: 
            self.colour = "white" #their pieces will be white otherwise
    

#loading relevant data and initialising variables
print("Loading game...\n")            
storage.refreshData() 
global player1
global player2
currentPlayers = []


print("Welcome to a game of Othello!")
print("\nVisit README.md at https://github.com/9c480k/2022-Y3CEP_WA3/blob/main/README.md for links to the playerbase log, as well as other useful information")
print("\nProceeding to user login and registration...\n")
for i in range(2):    #repeats twice for both players to login 
    while True: #checks whether user has an account
        try:
            accountCheck = input("Do you have an account? (y/n)").strip()
            if accountCheck not in ["y", "n"]: #exception handling for invalid inputs 
                raise ValueError

        except ValueError:
            print("Please try again.")

        else:
            break

    if accountCheck == "y": 
        while True: 
            try: 
                username = login()
                if username in currentPlayers: #makes sure that the same user cannot login twice and play against themselves
                    raise ValueError
                else: 
                    break

            except ValueError:
                print("Successful login rejected.") 
                print("The user is currently logged in. Sign in as another user")
    else: 
        username = createAccount() #proceeds to account creation if the user doesnt have an account

    if i == 0: 
        #asks the first player to sign in whether they would like to go first
        #second player doesnt get a choice 
        while True:
            try: 
                turnCheck = input("\nWould you like to go first? (y/n)").strip()
                if turnCheck == "y": 
                    player1 = Player(username, 1) #first player goes first
                    break
                elif turnCheck == "n": 
                    player1 = Player(username, 2) #first player goes second
                    break
                else: 
                    raise ValueError #exception handling

            except ValueError: 
                print("Please provide valid input") 

        currentPlayers.append(player1.username) 

        print("\nProceeding to login for second player.\n")


    else: #assigns second player their turn based on the choice of the first player
        if player1.turn == 1: 
            player2 = Player(username, 2)
        else: 
            player2 = Player(username, 1)

        currentPlayers.append(player2.username)

#initialisation
board = game.Deck()
gameController = game.gameControl(player1, player2, board)
print("Saving data...")
storage.saveData() #updates the google sheets with new account data 

gameController.rules() #prints rules
print("\n")
#automatically retrieves saves if there are any 
gameController.retrieveGame()

if gameController.first in currentPlayers and gameController.second in currentPlayers: #checks if the players currently playing are the same as the save stored
    gameController.clearSave()
else: 
    board = game.Deck() #reinitialises the variables so that it is a fresh board 
    gameController = game.gameControl(player1, player2, board) #makes sure that usernames are correct and not the ones from the save 




exit = False
#game loop 
for i in range(61):        
    if gameController.turnCount == 61 or gameController.passEnd == True: #checks if the board is already full (after 60 turns) or players have passed consecutively

        gameController.gameEnd()#triggers win determination 

        if gameController.winner == "draw": #handles situation of draw
            print("The game ended in a draw! Both players lose.")
            storage.changeStoredStats(gameController.first, "gl")
            storage.changeStoredStats(gameController.second, "gl")

        else:             
            print(f"The winner of this game is {gameController.winner}")
            storage.changeStoredStats(gameController.winner, "gw") #credits winner 

            if gameController.winner == gameController.first:                
                storage.changeStoredStats(gameController.second, "gl") #determines which of the players lost and credit loss 
            else:                 
                storage.changeStoredStats(gameController.first, "gl")

        print("Game ended. Updating database...")
        storage.saveData()
        break   #ends loop, which causes the file to finish running and stop

    
    currentUser = gameController.turn #obtains current user 

    if currentUser == player1.username: #determine the piece colour which should be used this round 
        
        currentColour = player1.colour 
    else:         
        currentColour = player2.colour

    print(f"\nIt is now {currentUser}'s turn!\n")

    while True: #try and except to obtain user input for move 
        try:             
            print(board)                       
            print("If you would like to quit and save your game, type q. If you would like to pass, press p")
            print("If you would like to revisit the rules, type r")
            move = input("\nPlease enter the column and row of your move in the format columnrow (e.g. 12):")  

            if move == "q": #causes user to exit try and except 
                exit = True                 
                break 
            elif move == "p": 
                gameController.skip() 
                break

            elif move == "r": #prints rules when it detects exception raised
                raise ValueError

            elif move.isnumeric() == False: #makes sure that the input is numeric only (does not contain letters or symbols)
                raise TypeError

            elif board.placePiece(int(move[0]), int(move[1]), currentColour) == False: #if it is not a valid move, raise exception. if it was a valid move, it would not return anything, and the try and except will end without exceptions
                raise Exception
             
            break        
                
        except ValueError:
            gameController.rules()           
        
        except TypeError: 
            print("\n\nPlease provide valid input.")

        except Exception: 
            print("\n\nTile not available. Try another move.")

    if exit == True: #continuation of quit 
        gameController.save() #stores save locally
        print("Game saved locally.")
        break #exits for loop 

    else:        
        gameController.changeTurn() #updates the gameController so that the users swap turns


   




    


            







    




