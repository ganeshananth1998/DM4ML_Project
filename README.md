# Recommendation System Pipeline (DM4ML Project)

**Project Repository:** https://github.com/ganeshananth1998/DM4ML_Project


## Team Members

| Student ID  | Name               |
| ----------- | ------------------ |
| 2025AE05551 | Ashish Raj         |
| 2025AE05455 | Ganesh A           |
| 2025AF05149 | P. Hemanth Bhargav |
| 2025AF05127 | Praveen            |

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



## Setup & Execution

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ganeshananth1998/DM4ML_Project
cd DM4ML_Project
```

---

### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate     # Mac/Linux
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the pipeline

```bash
python pipeline/prefect_flow.py
```

---

## Outputs

The pipeline generates:

* Processed dataset
* Feature dataset
* Executed notebooks (stored in `logs/`)
* Feature store artifacts
* Trained model

Example:

```
models/model_<timestamp>.pkl
```
Final dataset will be generated at:

```text
data/processed/final_dataset.csv
```

 Notes:

* File is **not included in Git**
* It is generated dynamically
* Each run **appends new data**

---

---

## Results

* Dataset processed: ~600,000 records
* Duplicate records removed
* Features successfully generated
* Model trained and evaluated with high accuracy

---

## Prediction (Optional)

After training, predictions can be generated using:

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


## Deliverables

* Prefect orchestration pipeline
* Jupyter notebooks
* Feature store implementation
* Trained model artifact
* Documentation (docs/)

---

## Conclusion

This project demonstrates a **production-style ML pipeline** integrating all stages of the machine learning lifecycle.

It ensures:

* Automation
* Reproducibility
* Scalability

and reflects real-world **MLOps practices**.
