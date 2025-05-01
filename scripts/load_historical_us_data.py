import pandas as pd
from sqlalchemy import create_engine

# Create a connection to your PostgreSQL database.
# Note: Adjust the connection string if needed.
engine = create_engine('postgresql://postgres:apple@localhost:5433/CryptoCurrency Price Predictions')

# Read the CSV file.
# The CSV file has headers: "date","price","open","high","low","volume.","change_percent"
csv_path = '/Users/blairjdaniel/fintech_fraud/data/us_dollar_historical_data.csv'
df = pd.read_csv(csv_path)

# Optionally, display the first few rows to verify the data
print(df.head())

# Load (or replace) the data into a table named 'bitcoin_historical_data'
df.to_sql('usd_historical_data', engine, if_exists='replace', index=False)

print("Data loaded successfully into table: usd_historical_data")