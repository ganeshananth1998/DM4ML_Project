import pandas as pd
import random
import os
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

    output_path = "data/source/user_interactions.csv"

    #  create folder if not exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_csv(output_path, index=False)

    print(f"Generated dataset with shape: {df.shape}")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    generate_large_data(15000)