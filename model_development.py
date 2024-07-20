# model_development.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_energy_demand_model(filename='cleaned_weather_data.csv'):
    df = pd.read_csv(filename)
    
    # Example feature and target selection:
    features = ['temperature', 'humidity', 'wind_speed']
    target = 'energy_demand'
    
    X = df[features]
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
    
    return model

if __name__ == "__main__":
    model = train_energy_demand_model()
