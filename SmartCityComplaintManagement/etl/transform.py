import pandas as pd
import os

# Define paths
input_path = os.path.join("data", "raw_complaints_backup.csv")
output_path = os.path.join("data", "cleaned_complaints.csv")

# Load the CSV
df = pd.read_csv(input_path)

# Strip whitespace from string columns
for col in df.select_dtypes(include='object'):
    df[col] = df[col].str.strip()

# Drop rows where critical fields are missing
df = df.dropna(subset=[
    'Timestamp',
    'Complaint Category',
    'Complaint Description',
    'Location / Ward',
    'Complaint Date'
])

# Rename columns for easier downstream processing
df = df.rename(columns={
    'Timestamp': 'timestamp',
    'Complaint Category': 'complaint_type',
    'Complaint Description': 'complaint_description',
    'Location / Ward': 'location',
    'Complaint Date': 'complaint_date'
})

# Save cleaned data
df.to_csv(output_path, index=False)

print("✅ Transformation complete. Cleaned data saved to:", output_path)
