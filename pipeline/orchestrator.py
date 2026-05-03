import subprocess
import sys
import logging
import os

# create logs folder if not exists
os.makedirs("logs", exist_ok=True)

# configure logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_step(step_name, command):
    print(f"\n🔹 Starting: {step_name}")
    logging.info(f"Starting: {step_name}")

    try:
        subprocess.run(command, check=True)
        print(f" Completed: {step_name}")
        logging.info(f"Completed: {step_name}")
    except subprocess.CalledProcessError:
        print(f" Failed: {step_name}")
        logging.error(f"Failed: {step_name}")
        sys.exit(1)


def main():
    print("\n Pipeline Started\n")
    logging.info("Pipeline Started")

    run_step("Generate Data", ["python", "processing/generate_interactions.py"])
    run_step("Transform Data", ["python", "processing/transform_data.py"])
    run_step("Check Duplicates", ["python", "check_duplicates.py"])

    print("\n Pipeline Completed Successfully\n")
    logging.info("Pipeline Completed Successfully")


if __name__ == "__main__":
    main()