import os
import pandas as pd
import json


# 🔹 Get latest folder helper
def get_latest_folder(path):
    folders = sorted(os.listdir(path))
    return os.path.join(path, folders[-1])


# 🔹 Get latest file path
def get_latest_file(base_path):
    date_folder = get_latest_folder(base_path)
    time_folder = get_latest_folder(date_folder)
    return os.path.join(time_folder)


# 🔹 Load latest API JSON
def load_latest_json():
    base_path = "data/raw/api/products"
    latest_path = get_latest_file(base_path)
    
    file_path = os.path.join(latest_path, "data.json")
    
    with open(file_path, "r") as f:
        data = json.load(f)
    
    print(f"Loaded JSON from: {file_path}")
    return data


# 🔹 Load latest CSV
def load_latest_csv():
    base_path = "data/raw/local/user_interactions"
    latest_path = get_latest_file(base_path)
    
    file_path = os.path.join(latest_path, "data.csv")
    
    df = pd.read_csv(file_path)
    
    print(f"Loaded CSV from: {file_path}")
    return df

# 🔹 Convert JSON to DataFrame
def convert_json_to_df(json_data):
    products = json_data["products"]
    
    df = pd.DataFrame(products)
    
    print("\nConverted JSON to DataFrame:")
    print(df.head())
    
    return df

def merge_data(products_df, interactions_df):

    merged_df = pd.merge(
        interactions_df,
        products_df,
        left_on="product_id",
        right_on="id",
        how="left"
    )

    print("\nMerged Data:")
    print(merged_df.head())

    return merged_df

def save_final_data(df):
    output_path = "data/processed/final_dataset.csv"

    os.makedirs("data/processed", exist_ok=True)

    # ✅ Check if file exists
    if os.path.exists(output_path):
        df.to_csv(output_path, mode='a', header=False, index=False)
        print("Data appended to existing file")
    else:
        df.to_csv(output_path, index=False)
        print("New file created")

    print(f"Final dataset saved at: {output_path}")

if __name__ == "__main__":
    json_data = load_latest_json()
    csv_data = load_latest_csv()

    products_df = convert_json_to_df(json_data)

    merged_df = merge_data(products_df, csv_data)

    save_final_data(merged_df)

    print("\nFinal merged shape:", merged_df.shape)