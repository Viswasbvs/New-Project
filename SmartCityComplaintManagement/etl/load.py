import pandas as pd
from pymongo import MongoClient

# Load CSV
df = pd.read_csv('data/cleaned_complaints.csv')
print(f"Loaded {len(df)} records from CSV")
print(df.head())

# Convert timestamp columns
df["timestamp"] = pd.to_datetime(df["timestamp"], errors='coerce')
df["complaint_date"] = pd.to_datetime(df["complaint_date"], errors='coerce')

print("After datetime conversion:")
print(df[["timestamp", "complaint_date"]].head())

# Connect to MongoDB
client = MongoClient('mongodb://host.docker.internal:27017/')
db = client['smartcity']
collection = db['complaints']
print(f"Connected to database: {db.name}, collection: {collection.name}")

# Insert into MongoDB
data_dict = df.to_dict(orient="records")
if data_dict:
    try:
        collection.insert_many(data_dict)
        print("Data inserted into MongoDB successfully.")
    except Exception as e:
        print("Error during insert:", e)
else:
    print("No data to insert.")
