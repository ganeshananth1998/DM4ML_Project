import pandas as pd
from ingestion.save_data import save_csv
from ingestion.logger import get_logger

logger = get_logger()

def fetch_csv():
    file_path = "data/source/user_interactions.csv"
    
    try:
        df = pd.read_csv(file_path)
        
        print("CSV loaded successfully")
        print("Number of records:", len(df))
        print(df.head())

        logger.info("CSV loaded successfully")

        return df
    
    except Exception as e:
        print("Error reading CSV:", e)
        logger.error(f"Error reading CSV: {e}")
        return None


if __name__ == "__main__":
    df = fetch_csv()
    
    if df is not None:
        save_csv(df, "local", "user_interactions")