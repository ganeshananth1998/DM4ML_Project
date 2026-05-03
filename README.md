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

<<<<<<< Updated upstream
### 1. Clone repository
=======
| Student ID  | Name               |
| ----------- | ------------------ |
| 2025AE05551 | Ashish Raj         |
| 2025AE05455 | Ganesh A           |
| 2025AF05149 | P. Hemanth Bhargav |
| 2025AF05127 | Praveen            |

---

## Overview

This project implements an **end-to-end machine learning pipeline** for a recommendation system using modern MLOps practices.

The pipeline is orchestrated using **Prefect** and integrates:

* Data generation & ingestion
* Data transformation & validation
* Data profiling & exploratory data analysis (EDA)
* Feature engineering (via notebooks)
* Feature store integration
* Model training & evaluation

---

## Objectives

* Build an **automated ML pipeline**
* Ensure **reproducibility across environments**
* Maintain a **modular and scalable architecture**
* Integrate **data processing, feature engineering, and modeling**

---

## Project Structure

```text
DM4ML_Project/
│
├── pipeline/
│   └── prefect_flow.py          # Main orchestration pipeline
│
├── processing/
│   ├── generate_interactions.py
│   ├── transform_data.py
│   ├── check_duplicates.py
│   └── predict.py               # Inference script (optional)
│
├── notebooks/                   # Jupyter notebooks
│   ├── Data Quality & Profiling.ipynb
│   ├── Data-Preparation.ipynb
│   ├── EDA And Visualization.ipynb
│   ├── Feature-Engineering And Transformation.ipynb
│   └── Model Building & Evaluation.ipynb
│
├── feature_store/
│   ├── setup_feature_store.py
│   └── feature_store_demo.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── metadata/
│
├── models/                     # Trained model outputs
├── logs/                       # Notebook outputs (ignored in Git)
├── docs/                       # Task documentation
├── requirements.txt
└── README.md

---


```
##  Feature Store Integration

This repository now includes a Feast-based feature store implementation under `feature_store/`.

To initialize and materialize the feature catalog:

```bash
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

## Pipeline Workflow

```
Data Generation
   ↓
Data Transformation
   ↓
Data Validation
   ↓
Data Profiling (Notebook)
   ↓
Data Preparation (Notebook)
   ↓
EDA & Visualization
   ↓
Feature Engineering (Notebook)
   ↓
Feature Store
   ↓
Model Training & Evaluation (Notebook)
```

---

## Technologies Used

* Python
* Prefect (pipeline orchestration)
* Pandas (data processing)
* Scikit-learn (model training)
* Papermill (notebook execution)
* Joblib (model serialization)

---

## Key Data Sources

* **User Interaction Data**

  * user_id, product_id, interaction_type, rating, timestamp

* **Product Metadata**

  * product_id, category, price, brand, description

* **Processed Dataset**

  * cleaned and transformed dataset used for modeling

---

## Setup & Execution

### 1️⃣ Clone the repository
>>>>>>> Stashed changes

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