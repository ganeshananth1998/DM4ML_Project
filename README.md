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