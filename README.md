# DM4ML Project – Data Pipeline

##  Overview

This project implements an end-to-end data pipeline for a product recommendation system.

It includes:

* Data ingestion (API + CSV)
* Raw data storage (structured data lake)
* Data transformation and merging
* Incremental pipeline with append support
* Synthetic data generation for scalability

---

## Setup Instructions

### 1. Clone repository

```bash
git clone <repo_url>
cd DM4ML_PROJECT
```

---

### 2. Create virtual environment (Python 3.9+ recommended)

```bash
python -m venv venv
```

Activate:

* Mac/Linux:

```bash
source venv/bin/activate
```

* Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Input Data

Ensure the following file exists:

```text
data/source/user_interactions.csv
```
 This file is used for ingestion (Task 2)

python processing/generate_interactions.py

---

##  How to Run the Pipeline

### Step 1: Run ingestion

```bash
python run_pipeline.py
```

 This will:

* Fetch product data from API
* Load user interactions CSV
* Store raw data in:

  ```
  data/raw/
  ```

---

### Step 2: Run transformation

```bash
python processing/transform_data.py
```

 This will:

* Convert JSON → DataFrame
* Merge with user interaction data
* Save final dataset

---

##  Feature Store Integration

This repository now includes a Feast-based feature store implementation under `feature_store/`.

To initialize and materialize the feature catalog:

```bash
pip install -r requirements.txt
python feature_store/setup_feature_store.py
```

To run a sample training and inference feature retrieval demo:

```bash
python feature_store/feature_store_demo.py
```

### How to Check and Inspect the Feature Store

To explicitly check the feature store status and view registered features:

```bash
# Check feature store status
python -c "from feature_store.feature_store import setup_feature_store; fs = setup_feature_store(); print('Feature store initialized successfully')"

# List all feature views
python -c "from feature_store.feature_store import setup_feature_store; fs = setup_feature_store(); print(fs.list_feature_views())"

# Get feature view details
python -c "from feature_store.feature_store import setup_feature_store; fs = setup_feature_store(); fv = fs.get_feature_view('user_profile_v1'); print(fv)"
```

---

##  Execution Workflow

Follow this step-by-step flow to run the complete data pipeline:

1. **Data Quality Notebook** (`analysis dev/Data-Quality.ipynb`)
   - Run data quality checks and validation
   - Identify and handle missing values, outliers, and data inconsistencies

2. **Data Preparation** (`analysis dev/Data-Preperation.ipynb`)
   - Clean and preprocess raw data
   - Handle data transformations and normalization

3. **EDA and Visualization** (`analysis dev/EDA And Visualization.ipynb`)
   - Perform exploratory data analysis
   - Generate visualizations and insights
   - Understand data distributions and relationships

4. **Feature Engineering and Transformation**
   - Create new features from existing data
   - Apply transformations and scaling
   - Prepare features for modeling

5. **Feature Store** (`feature_store/`)
   - Initialize and populate the feature store
   - Register feature views and entities
   - Enable feature serving for training and inference

6. **Model Building and Evaluations**
   - Train machine learning models
   - Evaluate model performance
   - Compare different algorithms and configurations

---

##  Output

Final dataset will be generated at:

```text
data/processed/final_dataset.csv
```

 Notes:

* File is **not included in Git**
* It is generated dynamically
* Each run **appends new data**

---

##  Project Structure

```text
data/
 ├── raw/        # ingested data (timestamp-based)
 ├── processed/  # final dataset
 ├── source/     # input CSV

analysis dev/    # notebooks for data quality, preparation, EDA, feature engineering, and model evaluation
feature_store/   # Feast feature store definitions and demo
ingestion/       # API & CSV ingestion
processing/      # transformation logic
logs/            # execution logs
pipeline/        # orchestration (future use)
```

---

## Pipeline Behavior

* Raw data is stored with timestamps (no overwrite)
* Final dataset uses **append mode**
* Supports large-scale data generation (15K+ per run)

---

##  Notes

* Large datasets are excluded via `.gitignore`
* Use pipeline to regenerate data locally
* VS Code may disable formatting for very large files (expected behavior)


## Note for General:
Clone the project, set up the virtual environment, and run the following commands:
python processing/generate_interactions.py
python run_pipeline.py
python processing/transform_data.py


How to Run the Project
1. Setup environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
2. Run full pipeline
python run_sequence.py
Notes
Data is generated dynamically (not stored in Git)
Final dataset will be created at:
data/processed/final_dataset.csv
Duplicate handling is implemented

Do one clean run:
rm -rf data/processed/*
python run_sequence.py
python check_duplicates.py