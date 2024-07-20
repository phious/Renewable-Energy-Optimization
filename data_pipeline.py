# data_pipeline.py

import subprocess

def run_data_pipeline():
    # Step 1: Collect data
    subprocess.run(["python", "data_collection.py"])

    # Step 2: Clean data
    subprocess.run(["python", "data_cleaning.py"])

    # Step 3: Train model
    subprocess.run(["python", "model_development.py"])

if __name__ == "__main__":
    run_data_pipeline()
