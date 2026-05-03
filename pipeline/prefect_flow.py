from prefect import flow, task
import subprocess
import sys
import os

# ------------------------
# Safe paths (cross-platform)
# ------------------------

PYTHON_PATH = sys.executable
PAPERMILL_PATH = "papermill"

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# ------------------------
# Python script tasks
# ------------------------

@task
def generate_data():
    subprocess.run([PYTHON_PATH, "processing/generate_interactions.py"], check=True)


@task
def transform_data():
    subprocess.run([PYTHON_PATH, "processing/transform_data.py"], check=True)


@task
def check_duplicates():
    subprocess.run([PYTHON_PATH, "processing/check_duplicates.py"], check=True)


# ------------------------
# Notebook tasks (Papermill)
# ------------------------

PAPERMILL_COMMAND = [PYTHON_PATH, "-m", "papermill"]

@task
def data_profiling():
    subprocess.run([
        *PAPERMILL_COMMAND,
        "notebooks/Data Quality & Profiling.ipynb",
        "logs/profiling_output.ipynb"
    ], check=True)


@task
def data_preparation():
    subprocess.run([
        *PAPERMILL_COMMAND,
        "notebooks/Data-Preparation.ipynb",
        "logs/preparation_output.ipynb"
    ], check=True)


@task
def eda():
    subprocess.run([
        *PAPERMILL_COMMAND,
        "notebooks/EDA And Visualization.ipynb",
        "logs/eda_output.ipynb"
    ], check=True)


@task
def feature_engineering_nb():
    subprocess.run([
        *PAPERMILL_COMMAND,
        "notebooks/Feature-Engineering And Transformation.ipynb",
        "logs/feature_engineering_output.ipynb"
    ], check=True)


# ------------------------
# Feature Store tasks
# ------------------------

@task
def setup_feature_store():
    subprocess.run([
        PYTHON_PATH,
        "feature_store/setup_feature_store.py"
    ], check=True)


@task
def run_feature_store_demo():
    subprocess.run([
        PYTHON_PATH,
        "feature_store/feature_store_demo.py"
    ], check=True)


# ------------------------
# Model training notebook
# ------------------------

@task
def model_training():
    subprocess.run([
        PAPERMILL_PATH,
        "notebooks/Model Building & Evaluation.ipynb",
        "logs/model_output.ipynb"
    ], check=True)


# ------------------------
# Flow
# ------------------------

@flow
def pipeline_flow():
    print(" Prefect Pipeline Started")

    generate = generate_data()
    transform = transform_data()
    validate = check_duplicates()

    profiling = data_profiling()
    preparation = data_preparation()
    eda_task = eda()
    feature_nb = feature_engineering_nb()

    store_setup = setup_feature_store()
    store_demo = run_feature_store_demo()

    model = model_training()

    # DAG Order
    generate >> transform >> validate \
        >> profiling >> preparation >> eda_task \
        >> feature_nb >> store_setup >> store_demo >> model

    print(" Prefect Pipeline Completed")


if __name__ == "__main__":
    pipeline_flow()