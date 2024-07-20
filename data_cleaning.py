# data_cleaning.py

import pandas as pd

def clean_weather_data(filename='weather_data.csv'):
    df = pd.read_csv(filename)
    
    # Example cleaning steps:
    # - Drop columns that are not needed
    # - Handle missing values
    # - Convert data types if necessary

    # Dropping unnecessary columns (example)
    columns_to_drop = ['unused_column1', 'unused_column2']
    df.drop(columns=columns_to_drop, inplace=True)

    # Handling missing values
    df.fillna(method='ffill', inplace=True)

    # Convert timestamp to datetime
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')
    
    df.to_csv('cleaned_weather_data.csv', index=False)

if __name__ == "__main__":
    clean_weather_data()
