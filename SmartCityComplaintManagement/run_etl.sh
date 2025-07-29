#!/bin/sh
echo "Starting ETL process..."
python etl/fetch.py
python etl/transform.py
python etl/load.py
echo "ETL process complete."
