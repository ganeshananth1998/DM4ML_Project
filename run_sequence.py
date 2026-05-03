import subprocess
import sys
import os

<<<<<<< Updated upstream
PROJECT_DIR = os.getcwd()
num_iterations = 5
=======
# Run the pipeline sequence 33 times
num_iterations = 10
>>>>>>> Stashed changes

for i in range(1, num_iterations + 1):
    print(f"\n{'='*60}")
    print(f"Iteration {i} of {num_iterations}")
    print(f"{'='*60}\n")

    try:
        # 🔥 STEP 1: Generate new data
        print("Generating new interaction data...")
        subprocess.run(
            [sys.executable, "processing/generate_interactions.py"],
            cwd=PROJECT_DIR,
            check=True
        )

        # STEP 2: Run ingestion
        print("\nRunning run_pipeline.py...")
        subprocess.run(
            [sys.executable, "run_pipeline.py"],
            cwd=PROJECT_DIR,
            check=True
        )

        # STEP 3: Transform + append
        print("\nRunning processing/transform_data.py...")
        subprocess.run(
            [sys.executable, "processing/transform_data.py"],
            cwd=PROJECT_DIR,
            check=True
        )

        print(f"\nIteration {i} completed successfully\n")

    except subprocess.CalledProcessError as e:
        print(f"\nError in iteration {i}: {e}")
        break

print(f"\n{'='*60}")
print("Pipeline execution completed!")
print(f"{'='*60}")