from prefect import flow, task
import subprocess


@task
def generate_data():
    subprocess.run(["python", "processing/generate_interactions.py"], check=True)


@task
def transform_data():
    subprocess.run(["python", "processing/transform_data.py"], check=True)


@task
def check_duplicates():
    subprocess.run(["python", "check_duplicates.py"], check=True)


@task
def feature_engineering():
    subprocess.run(["python", "processing/feature_engineering.py"], check=True)


@task
def train_model():
    subprocess.run(["python", "processing/train_model.py"], check=True)


@flow
def pipeline_flow():
    print("🚀 Prefect Pipeline Started")

    generate_data()
    transform_data()
    check_duplicates()
    feature_engineering()
    train_model()

    print("🎉 Prefect Pipeline Completed")


if __name__ == "__main__":
    pipeline_flow()