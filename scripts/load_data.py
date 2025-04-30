import pandas as pd
from sqlalchemy import create_engine

# Define the list of cryptocurrencies and their corresponding CSV file paths
crypto_files = {
    "BTC": "/Users/blairjdaniel/fintech_fraud/data/archive (15)/BTCUSDT/BTCUSDT.csv",
    "ETH": "/Users/blairjdaniel/fintech_fraud/data/archive (15)/ETHUSDT/ETHUSDT.csv",
    "SOL": "/Users/blairjdaniel/fintech_fraud/data/archive (15)/SOLUSDT/SOLUSDT.csv"
}

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:apple@localhost:5433/CryptoCurrency Price Predictions')

# Loop through each cryptocurrency and load its data into separate tables
for symbol, file_path in crypto_files.items():
    # Load CSV
    df = pd.read_csv(file_path)
    
    # Rename columns to match the database schema if necessary
    df.columns = [
        "timestamp", "open", "high", "low", "close", "volume", 
        "close_time", "quote_asset_volume", "number_of_trades", 
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
    ]
    
    # Check if 'timestamp' is already in datetime format
    if not pd.api.types.is_datetime64_any_dtype(df['timestamp']):
        df['timestamp'] = pd.to_datetime(df['timestamp'])  # Convert to datetime if not already
    
    # Check if 'close_time' is already in datetime format
    if not pd.api.types.is_datetime64_any_dtype(df['close_time']):
        try:
            # Attempt to convert from milliseconds
            df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
        except ValueError:
            # If already in datetime string format, convert directly
            df['close_time'] = pd.to_datetime(df['close_time'])
    
    # Insert data into a table named after the cryptocurrency (e.g., btc_prices, eth_prices, sol_prices)
    table_name = f"{symbol.lower()}_prices"  # e.g., btc_prices, eth_prices, sol_prices
    df.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"Data loaded successfully into table: {table_name}")