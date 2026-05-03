from pathlib import Path
from feast import Entity, FeatureView, Field
from feast.infra.offline_stores.file_source import FileSource
from feast.types import Int64, Float32, Float64, String
from feast.value_type import ValueType

PROJECT_ROOT = Path(__file__).resolve().parents[1]
FEATURE_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "final_dataset_eda.csv"

interaction_source = FileSource(
    path=str(FEATURE_DATA_PATH),
    event_timestamp_column="timestamp",
)

# Define entities with join keys
user_entity = Entity(
    name="user_id",
    join_keys=["user_id"],
    value_type=ValueType.INT64,
    description="User identifier"
)

product_entity = Entity(
    name="product_id",
    join_keys=["product_id"],
    value_type=ValueType.INT64,
    description="Product identifier"
)

# User profile features
user_profile_v1 = FeatureView(
    name="user_profile_v1",
    entities=[user_entity],
    ttl=None,
    source=interaction_source,
    online=True,
    schema=[
        Field(name="user_id", dtype=Int64),
        Field(name="user_product_diversity", dtype=Int64),
        Field(name="has_purchase", dtype=Int64),
        Field(name="has_cart", dtype=Int64),
        Field(name="has_view", dtype=Int64),
        Field(name="interaction_type_encoded", dtype=Int64),
        Field(name="user_rating", dtype=Int64),
        Field(name="user_rating_normalized", dtype=Float32),
        Field(name="user_engagement_level", dtype=String),
    ],
    tags={"version": "v1", "team": "data-science"},
)

# Product profile features
product_profile_v1 = FeatureView(
    name="product_profile_v1",
    entities=[product_entity],
    ttl=None,
    source=interaction_source,
    online=True,
    schema=[
        Field(name="product_id", dtype=Int64),
        Field(name="product_rating", dtype=Float32),
        Field(name="price", dtype=Float32),
        Field(name="discountPercentage", dtype=Float32),
        Field(name="stock", dtype=Int64),
        Field(name="product_user_diversity", dtype=Int64),
        Field(name="product_rating_normalized", dtype=Float32),
        Field(name="discount_normalized", dtype=Float32),
        Field(name="price_category", dtype=String),
        Field(name="discount_category", dtype=String),
        Field(name="product_rating_category", dtype=String),
        Field(name="stock_category", dtype=String),
        Field(name="product_engagement_level", dtype=String),
    ],
    tags={"version": "v1", "team": "data-science"},
)

# Interaction features (multi-entity feature view)
interaction_features_v1 = FeatureView(
    name="interaction_features_v1",
    entities=[user_entity, product_entity],
    ttl=None,
    source=interaction_source,
    online=True,
    schema=[
        Field(name="user_id", dtype=Int64),
        Field(name="product_id", dtype=Int64),
        Field(name="user_product_interaction_count", dtype=Int64),
        Field(name="cart_to_view_ratio", dtype=Float32),
        Field(name="purchase_to_cart_ratio", dtype=Float32),
        Field(name="day_of_week", dtype=Int64),
        Field(name="is_weekend", dtype=Int64),
        Field(name="day_period", dtype=String),
        Field(name="price", dtype=Float32),
        Field(name="discountPercentage", dtype=Float32),
        Field(name="category", dtype=String),
        Field(name="interaction_type_encoded", dtype=Int64),
        Field(name="has_purchase", dtype=Int64),
        Field(name="has_cart", dtype=Int64),
    ],
    tags={"version": "v1", "team": "data-science"},
)

# Export for use in setup
ALL_ENTITIES = [user_entity, product_entity]
ALL_FEATURE_VIEWS = [user_profile_v1, product_profile_v1, interaction_features_v1]