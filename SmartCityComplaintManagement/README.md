# 🏙️ Smart City Complaint Management – ETL Pipeline

A lightweight and modular **ETL (Extract, Transform, Load)** pipeline built in **Python** to manage public complaints in a smart city initiative.  
Data is extracted from CSV, cleaned and transformed using `pandas`, and loaded into **MongoDB**.  
All steps are **Dockerized** for seamless deployment.

---

## 🚀 Features

- Extract raw complaints from a CSV file
- Clean and transform the data (datetime formatting, missing value handling)
- Load structured data into **MongoDB** or **SQLite**
- Fully automated via Docker
- Scalable and customizable ETL structure

---

## 🧱 Project Structure

SmartCityComplaintManagement/
├── data/
│ ├── raw_complaints_backup.csv # Extracted raw data
│ └── cleaned_complaints.csv # Transformed data (optional)
│
├── etl/
│ ├── fetch.py # Extraction logic
│ ├── transform.py # Data cleaning & transformation
│ └── load.py # Load to MongoDB
│
├── Dockerfile # Docker instructions
├── requirements.txt # Python dependencies
├── .gitignore # Files to ignore in Git
└── README.md # Project documentation


---

## ⚙️ Technologies Used

- Python 3
- pandas
- MongoDB (pymongo)
- Docker

---

## 🐳 Run Using Docker

> Ensure you have Docker installed and running.

### 🔧 1. Build Docker Image

```bash
docker build -t smartcity-etl .


---

### ✅ What You Should Do Next

1. Replace:
   - `viswasbvs`
   - `Viswa`
   - LinkedIn/GitHub links

2. Save this content as `README.md` in your project folder.

Let me know if you'd like me to include MongoDB Atlas cloud setup instructions too.
