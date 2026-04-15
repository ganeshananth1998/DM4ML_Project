import pandas as pd
import random
from datetime import datetime, timedelta


def generate_large_data(num_records=100000):
    data = []

    for _ in range(num_records):
        row = {
            "user_id": random.randint(1, 10000),  # many users
            "product_id": random.randint(1, 30),  # MUST match API
            "interaction_type": random.choice(["click", "view", "purchase"]),
            "rating": random.randint(1, 5),
            "timestamp": datetime.now() - timedelta(days=random.randint(0, 30))
        }
        data.append(row)

    df = pd.DataFrame(data)

    output_path = "data/source/user_interactions.csv"
    df.to_csv(output_path, index=False)

    print(f"Generated dataset with shape: {df.shape}")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    generate_large_data(15000)  # change to 1_000_000 later