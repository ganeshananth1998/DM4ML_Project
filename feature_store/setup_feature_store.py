import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from feast import FeatureStore
from feature_store.feature_views import ALL_ENTITIES, ALL_FEATURE_VIEWS


def setup_feature_store() -> None:
    """Setup and materialize the Feast feature store."""
    repo_path = Path(__file__).resolve().parent
    print(f"📁 Feature store repo path: {repo_path}")
    
    try:
        store = FeatureStore(repo_path=str(repo_path))
        
        print("✅ Feature store loaded successfully")
        print("📝 Registering entities and feature views...")
        
        store.apply(ALL_ENTITIES + ALL_FEATURE_VIEWS)
        print("✅ Entities and feature views registered")
        
        # Materialize for the last 30 days to online store
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        
        print(f"🔄 Materializing features from {start_date.date()} to {end_date.date()}...")
        store.materialize(start_date=start_date, end_date=end_date)
        print("✅ Materialization complete")
        
        # List registered objects
        print("\n📊 Registry Summary:")
        print(f"  Entities: {len(store.list_entities())}")
        print(f"  Feature views: {len(store.list_feature_views())}")
        
    except Exception as e:
        print(f"❌ Error setting up feature store: {e}")
        raise


if __name__ == "__main__":
    setup_feature_store()
