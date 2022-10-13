'''
    This file uploads the attendance to the Google Spreadsheet.
    In order to run this, it requires some libraries that have to be installed.
    This works with Google Spreadsheet API, so you need to make a service 
    account and download its key in .json format.

    For more detailed information about the working of Google Spreadsheet 
        API watch this video: https://youtu.be/4ssigWmExak

    For more information check the README.md file

'''

from googleapiclient.discovery import build
from google.oauth2 import service_account

# Initializing the key file for the Service account
SERVICE_ACCOUNT_FILE = 'your_key.json' # your key..
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Initializing the Spreadsheet
SAMPLE_SPREADSHEET_ID = 'your_spreadsheet_id' # your spreadsheet id...
#Building service
service = build('sheets', 'v4', credentials=creds)
# Defining the sheet
sheet = service.spreadsheets()


'''
This function checks for the last blank row in the Spreadsheet, so that 
the values can be inserted below the values that have been inserted before
'''
def last_row():
    i = 1
    val = []
    while val != None:
        a = str(i)
        res = sheet.values().get(spreadsheetId = SAMPLE_SPREADSHEET_ID,
                            range = f"sheet1!A{a}:A{a}").execute()
        val = res.get('values', None)
        i += 1
    row = str(i-1)
    return row

# This is the function that uploads the attendance to the Google Spreadsheet
def mark_attendance(attendance):
    # Checks for the last row
    row = last_row()
    # Uploading...
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                range=f"sheet1!A{row}", valueInputOption="USER_ENTERED", 
                                body={"values":attendance}).execute()
    # Returns True
    return True
