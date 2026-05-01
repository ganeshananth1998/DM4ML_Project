import subprocess
import sys
import os

PROJECT_DIR = os.getcwd()
num_iterations = 33

for i in range(1, num_iterations + 1):
    print(f"\n{'='*60}")
    print(f"Iteration {i} of {num_iterations}")
    print(f"{'='*60}\n")

    try:
        # Run ingestion pipeline
        print("Running run_pipeline.py...")
        subprocess.run(
            [sys.executable, "run_pipeline.py"],
            cwd=PROJECT_DIR,
            check=True
        )

        # Run transformation
        print("\nRunning processing/transform_data.py...")
        subprocess.run(
            [sys.executable, "processing/transform_data.py"],
            cwd=PROJECT_DIR,
            check=True
        )

        print(f"\nIteration {i} completed successfully\n")

    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error in iteration {i}: {e}")
        break

print(f"\n{'='*60}")
print("Pipeline execution completed!")
print(f"{'='*60}")