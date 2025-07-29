import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import os

# Step 1: Set up Google Sheets API credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials/credentials.json", scope)

# Step 2: Authorize client
client = gspread.authorize(credentials)

# Step 3: Open the spreadsheet
spreadsheet = client.open("raw_complaints")  # Replace with your actual Sheet name
worksheet = spreadsheet.sheet1  # First tab in the sheet

# Step 4: Fetch all records
records = worksheet.get_all_records()
df = pd.DataFrame(records)

# Step 5: Create 'data/' directory if not exists
os.makedirs("data", exist_ok=True)

# Step 6: Save the raw data as CSV
output_file = "data/raw_complaints_backup.csv"
df.to_csv(output_file, index=False)

print(f"✅ Data fetched and saved to: {output_file}")
