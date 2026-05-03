import pandas as pd

df = pd.read_csv("data/processed/final_dataset.csv")

print("Total rows:", len(df))
print("Duplicates:", df.duplicated(
    subset=["user_id","product_id","interaction_type","timestamp"]
).sum())