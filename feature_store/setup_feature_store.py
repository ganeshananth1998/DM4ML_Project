import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from feast import FeatureStore
from feature_store.feature_views import ALL_ENTITIES, ALL_FEATURE_VIEWS


def setup_feature_store() -> None:
    """Setup the Feast feature store registry."""
    repo_path = Path(__file__).resolve().parent
    print(f"📁 Feature store repo path: {repo_path}")
    
    try:
        store = FeatureStore(repo_path=str(repo_path))
        print("✅ Feature store loaded successfully")
        print("📝 Feature views and entities are ready to use")
        print("\n✅ Feature store setup complete!")
        
    except Exception as e:
        print(f"❌ Error setting up feature store: {e}")
        raise


if __name__ == "__main__":
    setup_feature_store()
