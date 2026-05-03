# Feast Feature Store Metadata

## Overview
This feature store is implemented using Feast with a local provider. It stores feature definitions and metadata separately from model training code, and enables versioned retrieval for both training and inference.

## Feature Store Files
- `feature_store/feature_store.yaml`: Feast repository configuration
- `feature_store/feature_views.py`: Entity and feature view definitions
- `feature_store/setup_feature_store.py`: Registry application and materialization script
- `feature_store/feature_store_demo.py`: Example retrieval for training and inference

## Source Data
- Source file: `data/processed/final_dataset_eda.csv`
- Feature source: Feast `FileSource` reading the engineered dataset
- Timestamp column: `timestamp`
- Online store: `feature_store/online_store.db`
- Offline store: `feature_store/offline_store`

## Entities
- `user_id`: User identifier for personalization
- `product_id`: Product identifier for item-level features

## Feature Views and Versioning
The feature store uses explicit versioned names so you can retrieve the correct version for training and inference.

### `user_profile_v1`
- `user_product_diversity` — number of unique products a user interacted with
- `has_purchase` — binary purchase indicator
- `has_cart` — binary cart indicator
- `has_view` — binary view indicator
- `interaction_type_encoded` — encoded interaction type
- `user_rating` — raw user rating
- `user_rating_normalized` — normalized user rating
- `user_engagement_level` — interaction-level engagement bucket

### `product_profile_v1`
- `product_rating` — product average rating
- `price` — current product price
- `discountPercentage` — product discount percent
- `stock` — stock count
- `product_user_diversity` — number of unique users interacting with product
- `product_rating_normalized` — normalized rating
- `discount_normalized` — normalized discount
- `price_category` — categorized price bucket
- `discount_category` — categorized discount band
- `product_rating_category` — rating bucket
- `stock_category` — stock quantity bucket
- `product_engagement_level` — product popularity bucket

### `interaction_features_v1`
- `user_product_interaction_count` — interactions per user-product pair
- `cart_to_view_ratio` — conversion ratio from cart to view
- `purchase_to_cart_ratio` — conversion ratio from purchase to cart
- `day_of_week` — interaction weekday
- `is_weekend` — weekend indicator
- `day_period` — part of day for interaction
- `price` — product price at interaction time
- `discountPercentage` — discount at interaction time
- `category` — product category
- `interaction_type_encoded` — encoded interaction type
- `has_purchase` — purchase indicator
- `has_cart` — cart indicator

## Training vs Inference
- Training retrieval: use `get_historical_features(...)` with an entity DataFrame and timestamp column
- Inference retrieval: use `get_online_features(...)` after materializing the feature store

## Versioned Retrieval
- Current feature version suffix: `_v1`
- To update features, add a new view such as `user_profile_v2` or `interaction_features_v2`
- During model training or inference, request the exact view name for stable behavior

## Integration Point
Implement this after the feature engineering stage and before model training.

Recommended placement:
- In `analysis dev/Feature-Engineering And Transformation.ipynb`, add a final cell that imports and executes `feature_store/setup_feature_store.py`
- In the model notebook, load features from Feast for training and inference instead of directly reading the CSV or SQLite feature table

## Example commands
```bash
pip install -r requirements.txt
python feature_store/setup_feature_store.py
python feature_store/feature_store_demo.py
```
