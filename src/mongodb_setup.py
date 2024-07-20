# mongodb_setup.py

from pymongo import MongoClient

def insert_data(collection_name, data):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['energy_db']
    collection = db[collection_name]
    collection.insert_many(data)

def main():
    data = [{"temperature": 25, "humidity": 50, "wind_speed": 5, "energy_demand": 10}]
    insert_data('weather_data', data)

if __name__ == "__main__":
    main()
