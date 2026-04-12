import requests
import time
from ingestion.save_data import save_json
from ingestion.logger import get_logger

logger = get_logger()

def fetch_products():
    url = "https://dummyjson.com/products"
    max_retries = 3

    for attempt in range(max_retries):
        try:
            logger.info(f"Attempt {attempt + 1} to fetch API")

            response = requests.get(url)
            response.raise_for_status()
            
            data = response.json()
            
            print("API fetch successful")
            print("Number of products:", len(data["products"]))
            print(data["products"][0])

            logger.info("API fetch successful")

            return data
        
        except Exception as e:
            print(f"Attempt {attempt + 1} failed:", e)
            logger.error(f"Attempt {attempt + 1} failed: {e}")

            if attempt < max_retries - 1:
                print("Retrying in 2 seconds...")
                logger.info("Retrying after 2 seconds")
                time.sleep(2)
            else:
                print("All retries failed")
                logger.error("All retries failed")

    return None


if __name__ == "__main__":
    data = fetch_products()
    
    if data is not None:
        save_json(data, "api", "products")