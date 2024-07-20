# model_testing.py

import pandas as pd
import pickle

def load_model(filename='energy_demand_model.pkl'):
    with open(filename, 'rb') as f:
        model = pickle.load(f)
    return model

def predict_energy_demand(model, new_data):
    prediction = model.predict(new_data)
    return prediction

if __name__ == "__main__":
    model = load_model()
    
    new_data = pd.DataFrame({
        'temp': [25],
        'humidity': [50],
        'wind_speed': [5]
    })
    
    prediction = predict_energy_demand(model, new_data)
    print(f'Predicted Energy Demand: {prediction[0]}')
