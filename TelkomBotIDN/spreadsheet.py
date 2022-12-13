import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def readMyGsheet():
    alamatURL = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    kredensial = ServiceAccountCredentials.from_json_keyfile_name('ISI JSON KEY FILE DISINI', alamatURL)
    client = gspread.authorize(kredensial)

    # Membaca Sheet1 pada Google Spreadsheets untuk file TelkomBotIDN:
    sheet = client.open('TelkomBotIDN').sheet1
    telkombotidn_data = sheet.get_all_records()
   
    # Konvert menjadi DataFrame  
    df = pd.DataFrame(telkombotidn_data) 
    
    # Seleksi columns label
    print(df[['Tiket', 'SESI', 'STATUS', 'HSI', 'HSIttl', 'VC', 'VCttl', 'Grandttl']]) 
readMyGsheet()