from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database_setup import WeatherData

DATABASE_URL = "sqlite:///./test.db"  # Match with database_setup.py
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

def add_weather_data(data):
    for entry in data:
        db.add(WeatherData(**entry))
    db.commit()
