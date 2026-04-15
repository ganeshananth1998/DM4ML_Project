import os
import json
from datetime import datetime


def save_json(data, source, data_type):
    # Create date & time separately
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H-%M-%S")

    # Create folder path
    folder_path = f"data/raw/{source}/{data_type}/{date}/{time}"
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, "data.json")

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"JSON saved at: {file_path}")


def save_csv(df, source, data_type):
    # Create date & time separately
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H-%M-%S")

    # Create folder path
    folder_path = f"data/raw/{source}/{data_type}/{date}/{time}"
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, "data.csv")

    df.to_csv(file_path, index=False)

    print(f"CSV saved at: {file_path}")