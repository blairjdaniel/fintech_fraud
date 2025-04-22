import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_data(file_path):
    return pd.read_csv(file_path)

def train_model(X, y):
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def main():
    # Load processed data
    data = load_data('../data/processed/processed_data.csv')
    X = data.drop('target', axis=1)
    y = data['target']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Save the trained model
    joblib.dump(model, '../models/model.pkl')

if __name__ == "__main__":
    main()