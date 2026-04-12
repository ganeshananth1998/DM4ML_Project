import os
import json
from datetime import datetime


def save_json(data, source, data_type):
    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create folder path
    folder_path = f"data/raw/{source}/{data_type}/{timestamp}"
    os.makedirs(folder_path, exist_ok=True)

    # File path
    file_path = os.path.join(folder_path, "data.json")

    # Save JSON
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"JSON saved at: {file_path}")


def save_csv(df, source, data_type):
    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create folder path
    folder_path = f"data/raw/{source}/{data_type}/{timestamp}"
    os.makedirs(folder_path, exist_ok=True)

    # File path
    file_path = os.path.join(folder_path, "data.csv")

    # Save CSV
    df.to_csv(file_path, index=False)

    print(f"CSV saved at: {file_path}")