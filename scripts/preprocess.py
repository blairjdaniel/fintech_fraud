import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def load_data(file_path):
    """Load raw data from a specified file path."""
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """Clean the data by handling missing values and duplicates."""
    data = data.dropna()  # Remove missing values
    data = data.drop_duplicates()  # Remove duplicate rows
    return data

def transform_data(data):
    """Transform the data as needed for analysis or modeling."""
    # Example transformation: Convert categorical variables to dummy variables
    data = pd.get_dummies(data, drop_first=True)
    return data

def save_processed_data(data, output_path):
    """Save the processed data to a specified output path."""
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    # Example usage
    raw_data_path = 'data/raw/data.csv'  # Update with actual raw data path
    processed_data_path = 'data/processed/cleaned_data.csv'  # Update with desired output path

    raw_data = load_data(raw_data_path)
    cleaned_data = clean_data(raw_data)
    transformed_data = transform_data(cleaned_data)
    save_processed_data(transformed_data, processed_data_path)