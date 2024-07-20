# database_setup.py

from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Use SQLite for demonstration

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = "weather_data"
    
    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    wind_speed = Column(Float)
    energy_demand = Column(Float)

def create_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)

def main():
    create_database()

if __name__ == "__main__":
    main()
