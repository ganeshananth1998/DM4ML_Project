# Recommendation System Pipeline (DM4ML Project)

**Project Repository:** https://github.com/ganeshananth1998/DM4ML_Project/tree/main

## Team Members

| Student ID  | Name               |
| ----------- | ------------------ |
| 2025AE05551 | Ashish Raj         |
| 2025AE05455 | Ganesh A           |
| 2025AF05149 | P. Hemanth Bhargav |
| 2025AF05127 | Praveen            |

---

## Overview

This project implements an **end-to-end machine learning pipeline** for a recommendation system using modern MLOps practices.

The pipeline is fully orchestrated using **Prefect** and integrates:

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
* Integrate **data processing, feature engineering, and model training**

---

## Project Structure

```text id="2dj3hp"
DM4ML_Project/
│
├── pipeline/
│   └── prefect_flow.py          # Main orchestration pipeline
│
├── processing/
│   ├── generate_interactions.py
│   ├── transform_data.py
│   └── check_duplicates.py
│
├── analysis_dev/                # Jupyter notebooks
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

```text id="rfz8i7"
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

```bash id="o1h7al"
git clone https://github.com/<your-username>/<repo-name>
cd DM4ML_Project
```

---

### 2️⃣ Create virtual environment

```bash id="1a0ecp"
python3 -m venv venv
source venv/bin/activate     # Mac/Linux
```

---

### 3️⃣ Install dependencies

```bash id="2q79h2"
pip install -r requirements.txt
```

---

### 4️⃣ Run the pipeline

```bash id="e8t2lb"
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

```text id="k5bd8c"
models/model_<timestamp>.pkl
```

---

## Results

* Dataset processed: ~600,000 records
* Duplicate records removed
* Features successfully generated
* Model trained and evaluated with high accuracy

---

## Key Features

* Fully automated pipeline using Prefect
* Integration of Python scripts and Jupyter notebooks
* Feature store implementation
* Cross-platform compatibility
* Modular and scalable design

---

## Monitoring & Logging

Prefect provides:

* Task-level execution logs
* Runtime monitoring
* Failure tracking

Example:

```text id="c2d74n"
Task run 'model_training' - Finished in state Completed()
Flow run - Finished in state Completed()
```

---

## Deliverables

* Prefect orchestration pipeline
* Jupyter notebooks
* Feature store implementation
* Trained model artifact
* Documentation (docs/)

---

## Conclusion

This project demonstrates a **production-style ML pipeline** that integrates all stages of the machine learning lifecycle.

It ensures:

* Automation
* Reproducibility
* Scalability

and reflects real-world **MLOps practices**.
