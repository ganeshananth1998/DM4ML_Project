from ingestion.fetch_api import fetch_products
from ingestion.fetch_csv import fetch_csv
from ingestion.save_data import save_json, save_csv

def run_pipeline():
    print("Starting data ingestion pipeline...")

    # API
    api_data = fetch_products()
    if api_data is not None:
        save_json(api_data, "api", "products")

    # CSV
    csv_data = fetch_csv()
    if csv_data is not None:
        save_csv(csv_data, "local", "user_interactions")

    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()