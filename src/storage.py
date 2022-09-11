#https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/? used this tutorial as reference 
import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd 
from math import floor 





#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = './y3cep-wa3-othello-playerbase-b3b68340ee0c.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)

client = gspread.authorize(credentials)

#extracting data and converting to dataframe (this is the function that takes a lot of time to load because it needs to connect to google)
def refreshData():
    global accountDf
    global dataDf
    global statSheet
    global passwordSheet
    

    
    statSheet = client.open('Othello Playerbase Log').sheet1
        
    dataDf = pd.DataFrame.from_dict(statSheet.get_all_records())
    global usernameList 
    usernameList =  dataDf.Username.values.tolist()   #obtains all usernames before they are set as index and are unretrievable (so that we can check if a person's username exist)
    
    dataDf = dataDf.set_index("Username")#sets username as index so that dataframe can be searched by user 


    passwordSheet = client.open('Othello Passwords').sheet1
        
    accountDf = pd.DataFrame.from_dict(passwordSheet.get_all_records())
    accountDf = accountDf.set_index("Username") #sets username as index so that dataframe can be searched by user 


def checkUsername(username):
    if username == '' or username not in usernameList: #if the username is blank or doesnt exist yet, it throws back false
        return False 
    else: 
        return True 

def addUsername(username, password): #creates a new user, with all values initialised to 0 
    accountDf.loc[username] = password 
    dataDf.loc[username] = [0, 0, 0, 0]

def checkPassword(username, password): 
    correctPassword = accountDf.loc[username, "Password"] #retrieves password stored under that username

    if password != correctPassword: #checks whether user input and stored password are the same 
        return False 
    else: 
        return True 

def changeStoredStats(username, value):
    global dataDf
    global accountDf
    global statSheet
    global passwordSheet

    dataDf.loc[username, "Games Played"] += 1   #increments user's games played by 1 
    
    #note: no try and except because user isnt interacting directly with this function
    if value == "gw":
        dataDf.loc[username, "Games Won"] += 1   #if gw is passed through, credit user with a win     

    elif value == "gl":
        dataDf.loc[username, "Games Lost"] += 1 #if gl is passed through, credit user with a win 

    
    dataDf.loc[username, "Winrate(%)"] = floor((dataDf.loc[username, "Games Won"] / dataDf.loc[username, "Games Played"]) * 100) #calculates user's current winrate (games won divided by games played), and stores it 
   


def saveData(): #to update google sheets (all the changes the functions make have no effect on the google sheets, until this function is called)
    global dataDf
    global accountDf
    global statSheet
    global passwordSheet

   
    dataDf = dataDf.sort_values(by = 'Winrate(%)', ascending = False)   #sorts all entries in the playerbase log by winrate, in descending order

    dataDf = dataDf.reset_index() #removes index so that it is displayed well in google sheets
    accountDf = accountDf.reset_index()    

    set_with_dataframe(statSheet, dataDf, row = 1, col = 1, resize = True) #overwrites the data in the google sheets with updated data 
    set_with_dataframe(passwordSheet, accountDf, row = 1, col = 1, resize = True)
    refreshData() #retrieves updated data to use locally (otherwise it will continue to use outdated data)








    

        




