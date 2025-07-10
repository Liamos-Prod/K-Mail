import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



utilities_folder = "utilities"

current_directory = os.path.dirname(os.path.realpath(__file__))
repath_directory = current_directory.removesuffix("contact_functions")
utilities_path = os.path.join(repath_directory, utilities_folder)

print(utilities_path)

utilities_paths = {
    "credentials" : os.path.join( utilities_path, "credentials.json"),
    "token" : os.path.join( utilities_path, "token.json"),
}

print(utilities_paths)

scopes = ['https://www.googleapis.com/auth/spreadsheets']
spreadsheet_id = "yourSheet_id"


credentials = None
if os.path.exists(utilities_paths["token"]) :
    credentials = Credentials.from_authorized_user_file(utilities_paths["token"],scopes)
if not credentials or not credentials.valid :
    if credentials and credentials.expired and credentials.refresh_token :
        credentials.refresh(Request())
    else :
        flow = InstalledAppFlow.from_client_secrets_file(utilities_paths["credentials"],scopes)
        credentials = flow.run_local_server(port=0)
    with open(utilities_paths["token"],"w") as token :
        token.write(credentials.to_json())
client = gspread.authorize(credentials)


def get_sheet_names():
    try:
        spreadsheet = client.open_by_key(spreadsheet_id)
        sheet_list = spreadsheet.worksheets()
        sheet_names = [sheet.title for sheet in sheet_list]
        return sheet_names
    except gspread.exceptions.SpreadsheetNotFound as e:
        print(f"Spreadsheet not found: {e}")
        return []
    

def get_data_dict(receiver_group):
    sheet_names = get_sheet_names()
    data_dict = {}

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()
        for sheet_name in sheet_names:
            if receiver_group == sheet_name:
                if sheet_name == "RADIOS" or sheet_name == "TV" :
                    column_pronouns = sheets.values().get(spreadsheetId=spreadsheet_id, range=f"{sheet_name}!C4:C").execute()
                    column_name_events = sheets.values().get(spreadsheetId=spreadsheet_id, range=f"{sheet_name}!D4:D").execute()
                    column_fornames = sheets.values().get(spreadsheetId=spreadsheet_id, range=f"{sheet_name}!F4:F").execute()
                    column_emails = sheets.values().get(spreadsheetId=spreadsheet_id, range=f"{sheet_name}!E4:E").execute()
                    pronouns = column_pronouns.get('values', [])
                    emails = column_emails.get('values', [])
                    fornames = column_fornames.get('values', [])
                    name_events = column_name_events.get('values', [])
                else :
                    column_pronouns = sheets.values().get(spreadsheetId=spreadsheet_id, range=f"{sheet_name}!D4:D").execute()
                    column_name_events = sheets.values().get(spreadsheetId=spreadsheet_id, range=f"{sheet_name}!E4:E").execute()
                    column_fornames = sheets.values().get(spreadsheetId=spreadsheet_id, range=f"{sheet_name}!G4:G").execute()
                    column_emails = sheets.values().get(spreadsheetId=spreadsheet_id, range=f"{sheet_name}!I4:I").execute()
                    pronouns = column_pronouns.get('values', [])
                    emails = column_emails.get('values', [])
                    fornames = column_fornames.get('values', [])
                    name_events = column_name_events.get('values', [])                    
                
                for email, forname, pronoun, name_event in zip(emails, fornames, pronouns, name_events):
                    print(email, forname, pronoun, name_event)
                    if email:
                        if forname[0] == "___":
                                if pronoun[0] == "___":
                                    data_dict[email[0]] = " à toute l'équipe de programmation"
                                else :
                                    data_dict[email[0]] = f" à toute l'équipe de programmation {pronoun[0]} {name_event[0]}"
                                    
                        else:
                            data_dict[email[0]] = forname[0]
                    else : 
                        pass

        data_dict_good_format = {email: value.capitalize() for email, value in data_dict.items()}
        print(data_dict_good_format)
        print(len(data_dict_good_format))
        return data_dict_good_format
    
    except HttpError as error: 
        print(error)

get_data_dict("RADIOS")

