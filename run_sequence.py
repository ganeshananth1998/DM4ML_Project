import subprocess
import sys

# Run the pipeline sequence 33 times
num_iterations = 33

for i in range(1, num_iterations + 1):
    print(f"\n{'='*60}")
    print(f"Iteration {i} of {num_iterations}")
    print(f"{'='*60}\n")
    
    # Run run_pipeline.py
    print("Running run_pipeline.py...")
    result1 = subprocess.run([sys.executable, "run_pipeline.py"], cwd="e:\\dm4ml project")
    if result1.returncode != 0:
        print(f"Warning: run_pipeline.py failed with return code {result1.returncode}")
    
    # Run processing/transform_data.py
    print("\nRunning processing/transform_data.py...")
    result2 = subprocess.run([sys.executable, "processing/transform_data.py"], cwd="e:\\dm4ml project")
    if result2.returncode != 0:
        print(f"Warning: processing/transform_data.py failed with return code {result2.returncode}")
    
    print(f"\nIteration {i} completed\n")

print(f"\n{'='*60}")
print("All 33 iterations completed!")
print(f"{'='*60}")
