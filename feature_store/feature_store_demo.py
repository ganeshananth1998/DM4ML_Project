import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd
from feast import FeatureStore


def get_feature_store() -> FeatureStore:
    """Get the feature store instance."""
    repo_path = Path(__file__).resolve().parent
    return FeatureStore(repo_path=str(repo_path))


def run_training_demo() -> None:
    """Demonstrate historical feature retrieval for training."""
    print("\n🎓 TRAINING: Historical Feature Retrieval")
    print("=" * 50)
    
    store = get_feature_store()
    
    # Create entity dataframe for training data
    entity_df = pd.DataFrame(
        {
            "user_id": [1, 2, 3],
            "product_id": [1, 2, 1],
            "event_timestamp": [
                pd.Timestamp("2024-01-01 00:00:00"),
                pd.Timestamp("2024-01-02 00:00:00"),
                pd.Timestamp("2024-01-03 00:00:00"),
            ],
        }
    )
    
    feature_list = [
        "user_profile_v1:user_product_diversity",
        "user_profile_v1:user_rating",
        "product_profile_v1:price",
        "product_profile_v1:product_rating",
        "interaction_features_v1:user_product_interaction_count",
        "interaction_features_v1:interaction_type_encoded",
    ]
    
    try:
        training_df = store.get_historical_features(
            entity_df=entity_df,
            features=feature_list,
        ).to_df()
        
        print(f"✅ Retrieved {len(training_df)} training samples")
        print(f"\nFeature columns: {list(training_df.columns)}")
        print(f"\nFirst 3 rows:")
        print(training_df.head(3).to_string(index=False))
        
    except Exception as e:
        print(f"⚠️  Historical features not available yet (expected on first run): {e}")
        print("   Run setup_feature_store.py first to materialize features.")


def run_inference_demo() -> None:
    """Demonstrate online feature retrieval for inference."""
    print("\n🚀 INFERENCE: Online Feature Retrieval")
    print("=" * 50)
    
    store = get_feature_store()
    
    # Entity rows for inference
    entity_rows = [
        {"user_id": 1, "product_id": 1},
        {"user_id": 2, "product_id": 2},
    ]
    
    feature_list = [
        "user_profile_v1:user_product_diversity",
        "product_profile_v1:price",
        "interaction_features_v1:interaction_type_encoded",
    ]
    
    try:
        online_features = store.get_online_features(
            features=feature_list,
            entity_rows=entity_rows,
        ).to_dict()
        
        print(f"✅ Retrieved online features for {len(entity_rows)} entities")
        print(f"\nOnline features (dict format):")
        for key, values in online_features.items():
            print(f"  {key}: {values}")
            
    except Exception as e:
        print(f"⚠️  Online features not available yet (expected on first run): {e}")
        print("   Run setup_feature_store.py first to materialize features.")


if __name__ == "__main__":
    print("🎯 Feast Feature Store Demo")
    print("="*50)
    run_training_demo()
    run_inference_demo()
    print("\n✅ Demo complete!")
