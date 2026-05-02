## Task 8: Data Versioning and Lineage
## Overview

This task implements data versioning and lineage tracking for datasets used in the pipeline.
It ensures reproducibility, traceability, and efficient storage of data.

## Data Versioning using Git LFS

Git Large File Storage (Git LFS) is used to manage dataset files efficiently.

Large CSV files are tracked using Git LFS
Git stores lightweight pointers instead of full files
Each dataset update is committed as a new version

## Dataset Versions
Version 1: Initial dataset
Version 2: Regenerated dataset
Version 3: Updated dataset
Each version is tracked through Git commit history.

## Data Lineage Tracking

To track data lineage, metadata files are generated for each pipeline run.

Metadata files are stored in:

data/metadata/

Each metadata file contains:

run_id → Unique identifier for the run
source → Data source (synthetic generator)
records → Number of records
created_at → Timestamp
transformation → Applied transformations
file_path → Dataset location

This allows tracking:

When data was generated
How data was generated
Which version is used

## Repository Structure
data/
  ├── source/        # versioned dataset (Git LFS)
  ├── processed/     # processed data
  └── metadata/      # lineage metadata (JSON files)

## Benefits
Efficient storage using Git LFS
Clear dataset version history
Improved reproducibility
Full data lineage tracking

## Conclusion
By combining Git LFS and metadata tracking, the project ensures efficient data versioning and complete lineage visibility for all pipeline runs.