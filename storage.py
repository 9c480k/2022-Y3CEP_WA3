#https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/? used this tutorial as reference 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd 



#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = './y3cep-wa3-othello-playerbase-b3b68340ee0c.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)

client = gspread.authorize(credentials)

sheet = client.open('Othello Playerbase Log').sheet1
python_sheet = sheet.get_all_records()
data_df = pd.DataFrame.from_dict(python_sheet)
print(data_df)
