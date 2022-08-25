import main.py as main

print("Welcome to a game of Othello!")
usernameList = ["username"]
while True:
    try:
        accountCheck = bool(input("Do you have an account? True/False"))
    except ValueError:
        print("Please try again. Enter True/False (capital letter included")
    else:
        break
if accountCheck == True:
    while True:
        try:
            username = input("please enter your username")
            username in usernameList
        except ValueError:
            print("please try again")
        else:
            break
    while True:
        try:
            password = input("please enter your password")
            password in passwordList
            #make sure that usernames and passwords are matching 
        except ValueError:
            print("please try again")
        else:
            break
else:
    while True:
        try:
            username = input("enter your username")
            if username in usernameList:
                raise TypeError()
            elif str(username) != True:
                raise ValueError()
        except ValueError:
            print("your usernmae is not valid. Please try again")
        except TypeError:
            print("your username is already linked to an account.")
        else:
            break
            






class Player():
    pass

    



   
y = Player()
z = Player()
gameController = gameControl(y, z)
x = Deck(gameController)
x.placePiece(1, 2, "black")
x.placePiece(2, 2, "white")
x.placePiece(3, 2, "black")
x.placePiece(3, 3, "white")
x.placePiece(3, 1, "white")
x.placePiece(2, 1, "black")
x.placePiece(4, 3, "black")
x.placePiece(0, 2, "white")
x.placePiece(4, 2, "white")