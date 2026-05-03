# Task 10 — Pipeline Orchestration

## Overview

In this task, we implemented an end-to-end data pipeline using **Prefect** to automate the workflow. The pipeline orchestrates multiple stages including data generation, validation, transformation, feature engineering, and model training.

The goal is to ensure the pipeline is:

* Automated
* Reproducible
* Monitored
* Scalable

---

## DAG Flow

The pipeline follows this structure:

```
Ingestion → Validation → Preparation → Transformation → Feature Engineering → Model Training
```

### Mapping to Implementation:

| Stage                        | Implementation             |
| ---------------------------- | -------------------------- |
| Ingestion                    | `generate_interactions.py` |
| Validation                   | `check_duplicates.py`      |
| Preparation + Transformation | `transform_data.py`        |
| Feature Engineering          | `feature_engineering.py`   |
| Model Training               | `train_model.py`           |

---

## Orchestration Tool: Prefect

We used **Prefect** to define and manage the pipeline.

### Key Features Used:

* `@flow` for defining the pipeline
* `@task` for individual steps
* Automatic logging and monitoring
* Task-level execution tracking
* Failure handling

---

## Pipeline Code

The orchestration logic is implemented in:

```
pipeline/prefect_flow.py
```

### Structure:

* Each pipeline step is defined as a Prefect task
* Tasks are executed sequentially within a flow
* Prefect manages execution, logging, and monitoring

---

## Execution

The pipeline is executed using:

```
python pipeline/prefect_flow.py
```

---

## Execution Results

The pipeline executed successfully with the following outputs:

* Dataset processed: **600,000 rows**
* Duplicate records removed
* Features generated and stored
* Model trained successfully
* Model accuracy: **1.00**
* Model saved in:

  ```
  models/model_<timestamp>.pkl
  ```

Prefect logs confirm:

* All tasks completed successfully
* Flow execution completed without errors

---

## Monitoring and Logging

Prefect provides detailed logs for each task:

* Task start and completion status
* Execution time
* Success/failure state

Example:

```
Task run 'train_model' - Finished in state Completed()
Flow run - Finished in state Completed()
```

---

## Deliverables

* Prefect orchestration code (`prefect_flow.py`)
* Pipeline execution logs
* Screenshot showing successful execution
* Trained model artifact

---

## Conclusion

The pipeline is fully automated using Prefect, enabling:

* End-to-end workflow execution
* Reproducibility of results
* Clear monitoring and logging
* Modular and scalable design

This implementation demonstrates a production-style data pipeline suitable for real-world machine learning workflows.

---
