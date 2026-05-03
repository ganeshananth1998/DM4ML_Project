# Recommendation System Pipeline (DM4ML Project)

**Project Repository:** https://github.com/ganeshananth1998/DM4ML_Project

---

##  Team Members

| Student ID  | Name               |
| ----------- | ------------------ |
| 2025AE05551 | Ashish Raj         |
| 2025AE05455 | Ganesh A           |
| 2025AF05149 | P. Hemanth Bhargav |
| 2025AF05127 | Praveen            |

---

##  Overview

This project implements an **end-to-end machine learning pipeline** for a recommendation system using modern MLOps practices.

The pipeline is orchestrated using **Prefect**, ensuring reliable workflow execution, monitoring, and reproducibility. It integrates:

* Data generation & ingestion
* Data transformation & validation
* Data profiling & exploratory data analysis (EDA)
* Feature engineering (via notebooks)
* Feature store integration (Feast)
* Model training & evaluation

---

##  Objectives

* Build an automated ML pipeline
* Ensure reproducibility across environments
* Maintain a modular and scalable architecture
* Integrate data processing, feature engineering, and modeling

---

##  Project Structure

```
DM4ML_Project/
│
├── pipeline/
│   └── prefect_flow.py
│
├── processing/
│   ├── generate_interactions.py
│   ├── transform_data.py
│   ├── check_duplicates.py
│   └── predict.py
│
├── notebooks/
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
├── models/
├── logs/
├── docs/
├── requirements.txt
└── README.md
```

---

##  Pipeline Workflow

```
Data Generation
   ↓
Data Transformation
   ↓
Data Validation
   ↓
Data Profiling
   ↓
Data Preparation
   ↓
EDA & Visualization
   ↓
Feature Engineering
   ↓
Feature Store
   ↓
Model Training & Evaluation
```

---

##  Technologies Used

* Python
* Prefect (workflow orchestration & monitoring)
* Pandas (data processing)
* Scikit-learn (model training)
* Papermill (notebook execution automation)
* Joblib (model serialization)
* Feast (feature store)

---

##  Key Data Sources

* User interaction data
* Product metadata
* Processed dataset

---

##  Setup & Execution

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ganeshananth1998/DM4ML_Project
cd DM4ML_Project
```

---

### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
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

This executes the complete end-to-end pipeline using **Prefect orchestration**, enabling task-level execution tracking and reproducibility.

---

##  Feature Store Integration (Feast)

This project integrates a **Feast-based feature store** located in:

```
feature_store/
```

It ensures **consistent feature access across training and inference pipelines**, a key requirement for production ML systems.

---

### ▶ Initialize and Materialize Feature Store

```bash
python feature_store/setup_feature_store.py
```

---

### ▶ Run Feature Store Demo

```bash
python feature_store/feature_store_demo.py
```

This demonstrates feature retrieval for both training and inference scenarios.

---

###  Inspect Feature Store

```bash
# Initialize feature store
python -c "from feature_store.feature_store import setup_feature_store; fs = setup_feature_store(); print('Feature store initialized successfully')"

# List feature views
python -c "from feature_store.feature_store import setup_feature_store; fs = setup_feature_store(); print(fs.list_feature_views())"

# Get feature view details
python -c "from feature_store.feature_store import setup_feature_store; fs = setup_feature_store(); fv = fs.get_feature_view('user_profile_v1'); print(fv)"
```

---

## Prediction (Optional)

After training, predictions can be generated using:

```bash
python processing/predict.py
```

---

##  Outputs

The pipeline generates the following artifacts:

* **Processed Dataset**

  ```
  data/processed/final_dataset.csv
  ```

* **Feature Store Data**
  Managed using Feast for consistent feature access during training and inference

* **Trained Model**

  ```
  models/
  ```

* **Executed Notebook Outputs**

  ```
  logs/
  ```

---

### Notes

* Dataset is generated dynamically
* Not stored in Git repository
* Each pipeline run appends new data

---

## Results

* Dataset processed: ~600,000 records
* Duplicate records removed
* Features generated successfully
* Model trained with high accuracy
* Pipeline executed successfully using Prefect flow orchestration

---

##  Execution Workflow (Step-by-Step)

1. **Data Generation**
   `processing/generate_interactions.py`

2. **Data Transformation**
   `processing/transform_data.py`

3. **Data Validation**
   `processing/check_duplicates.py`

4. **Data Quality & Profiling**
   `notebooks/Data Quality & Profiling.ipynb`

5. **Data Preparation**
   `notebooks/Data-Preparation.ipynb`

6. **EDA & Visualization**
   `notebooks/EDA And Visualization.ipynb`

7. **Feature Engineering**
   `notebooks/Feature-Engineering And Transformation.ipynb`

8. **Feature Store Setup & Demo**
   `feature_store/`

9. **Model Training & Evaluation**
   `notebooks/Model Building & Evaluation.ipynb`

---

##  Deliverables

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
