#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = "C:/Users/Reliance/Desktop/pfa/green-tract-425606-v9-3937cf909a0c.json"
credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)
client = gspread.authorize(credentials)
spreadsheet_id = "1NyUstsBU27DJaUDQjS-H9a8GofhDzbOvtfM6you26p4"  
spreadsheet = client.open_by_key(spreadsheet_id)
worksheet = spreadsheet.sheet1
input_number = int(worksheet.cell(1, 2).value.replace(',', ''))  
net_premium = int(worksheet.cell(2, 2).value.replace(',', ''))   
if net_premium > input_number:
    print(f"Net Premium (Rs. {net_premium:,.2f}) is greater than the Input Number (Rs. {input_number:,.2f})")
elif net_premium < input_number:
    print(f"Net Premium (Rs. {net_premium:,.2f}) is less than the Input Number (Rs. {input_number:,.2f})")
else:
    print(f"Net Premium (Rs. {net_premium:,.2f}) is equal to the Input Number (Rs. {input_number:,.2f})")


# In[ ]:




