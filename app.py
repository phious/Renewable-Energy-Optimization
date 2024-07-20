# app.py
#Flask App for Model Deployment

from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

def load_model(filename='energy_demand_model.pkl'):
    with open(filename, 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
