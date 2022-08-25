#https://medium.com/daily-python/python-script-to-edit-google-sheets-daily-python-7-aadce27846c0 used this tutorial as reference 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = 'client_key.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)

client = gspread.authorize(credentials)

sheet = client.open('Othello Playerbase Log').sheet1
python_sheet = sheet.get_all_records()
pp = pprint.PrettyPrinter()
pp.pprint(python_sheet)
