import pandas as pd
import os

def main():
    input_path = "data/processed/final_dataset.csv"
    output_path = "data/processed/features.csv"

    df = pd.read_csv(input_path)

    # use correct column name
    df["interaction_score"] = df["user_rating"] * 2

    # Encode interaction type (click/view/purchase)
    df["interaction_type_encoded"] = df["interaction_type"].astype("category").cat.codes

    # User-product interaction feature
    df["user_product_interaction"] = df["user_id"] * df["product_id"]

    # Optional: purchase flag (useful for ML)
    df["is_purchase"] = (df["interaction_type"] == "purchase").astype(int)

    # Optional: normalize price (if exists)
    if "price" in df.columns:
        df["price_scaled"] = (df["price"] - df["price"].mean()) / df["price"].std()

    # Save only relevant columns (clean output)
    feature_cols = [
        "user_id",
        "product_id",
        "interaction_score",
        "interaction_type_encoded",
        "user_product_interaction",
        "is_purchase"
    ]

    # Add optional column if present
    if "price_scaled" in df.columns:
        feature_cols.append("price_scaled")

    features = df[feature_cols]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    features.to_csv(output_path, index=False)

    print("Feature engineering completed")
    print(f"Feature shape: {features.shape}")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()