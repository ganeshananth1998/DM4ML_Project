import pandas as pd
import random
import os
import json
from datetime import datetime, timedelta


def generate_large_data(num_records=100000):
    data = []

    # unique run identifier
    run_id = datetime.now().strftime("%Y%m%d%H%M%S")

    for _ in range(num_records):
        row = {
            "user_id": random.randint(1, 10000),
            "product_id": random.randint(1, 30),
            "interaction_type": random.choice(["click", "view", "purchase"]),
            "rating": random.randint(1, 5),
            "timestamp": datetime.now() - timedelta(days=random.randint(0, 30)),
            "run_id": run_id
        }
        data.append(row)

    df = pd.DataFrame(data)

    # remove duplicates within this run
    df = df.drop_duplicates()

    # paths
    data_path = "data/source/user_interactions.csv"
    metadata_dir = "data/metadata"

    # create folders if not exist
    os.makedirs(os.path.dirname(data_path), exist_ok=True)
    os.makedirs(metadata_dir, exist_ok=True)

    # save dataset
    df.to_csv(data_path, index=False)

    # create metadata
    metadata = {
        "run_id": run_id,
        "source": "synthetic_generator",
        "records": len(df),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "transformation": "none",
        "file_path": data_path
    }

    # save metadata file
    metadata_path = os.path.join(metadata_dir, f"{run_id}.json")
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)

    print(f"Generated dataset with shape: {df.shape}")
    print(f"Saved dataset to: {data_path}")
    print(f"Saved metadata to: {metadata_path}")


if __name__ == "__main__":
    generate_large_data(15000)