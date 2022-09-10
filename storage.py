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

#extracting data and converting to dataframe
def refreshData():
    global accountDf
    global dataDf
    global statSheet
    global passwordSheet
    

    
    statSheet = client.open('Othello Playerbase Log').sheet1
        
    dataDf = pd.DataFrame.from_dict(statSheet.get_all_records())
    global usernameList 
    usernameList =  dataDf.Username.values.tolist()    
    dataDf = dataDf.set_index("Username")


    passwordSheet = client.open('Othello Passwords').sheet1
        
    accountDf = pd.DataFrame.from_dict(passwordSheet.get_all_records())
    accountDf = accountDf.set_index("Username") 


def checkUsername(username):
    if username == '' or username not in usernameList: 
        return False 
    else: 
        return True 

def addUsername(username, password):
    accountDf.loc[username] = password 
    dataDf.loc[username] = [0, 0, 0, 0]

def checkPassword(username, password):
    correctPassword = accountDf.loc[username, "Password"]
    if password != correctPassword: 
        return False 
    else: 
        return True 

def changeStoredStats(username, value):
    global dataDf
    global accountDf
    global statSheet
    global passwordSheet

    dataDf.loc[username, "Games Played"] += 1   
    

    if value == "gw":
        dataDf.loc[username, "Games Won"] += 1       

    elif value == "gl":
        dataDf.loc[username, "Games Lost"] += 1 

    
    dataDf.loc[username, "Winrate(%)"] = floor((dataDf.loc[username, "Games Won"] / dataDf.loc[username, "Games Played"]) * 100)
   


def saveData():
    global dataDf
    global accountDf
    global statSheet
    global passwordSheet

   
    dataDf = dataDf.sort_values(by = 'Winrate(%)', ascending = False)    
    dataDf = dataDf.reset_index()
    accountDf = accountDf.reset_index()    
    set_with_dataframe(statSheet, dataDf, row = 1, col = 1, resize = True)
    set_with_dataframe(passwordSheet, accountDf, row = 1, col = 1, resize = True)
    refreshData()








    

        




