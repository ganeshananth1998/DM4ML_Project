# Task 3: Raw Data Storage
## Objective

The goal of this task is to store ingested data in a structured format using a local data lake approach. The storage system is designed to ensure scalability, traceability, and easy data retrieval.

## Storage Approach

We implemented raw data storage using the **local filesystem**, simulating a data lake architecture.

Data is stored in a hierarchical folder structure based on:

* **Source of data** (API / Local CSV)
* **Type of data** (Products / User Interactions)
* **Date of ingestion**
* **Time of ingestion**

This ensures proper organization and supports future scaling.


## Folder Structure

```text
data/
 └── raw/
      ├── api/
      │    └── products/
      │         └── YYYY-MM-DD/
      │              └── HH-MM-SS/
      │                   └── data.json
      │
      └── local/
           └── user_interactions/
                └── YYYY-MM-DD/
                     └── HH-MM-SS/
                          └── data.csv
```

## Explanation of Structure

| Level                        | Description                   |
| ---------------------------- | ----------------------------- |
| api / local                  | Data source (API or CSV file) |
| products / user_interactions | Type of data                  |
| YYYY-MM-DD                   | Date of ingestion             |
| HH-MM-SS                     | Time of ingestion             |
| data.json / data.csv         | Stored raw data file          |

## Implementation Details

* Data is saved using custom Python functions:

  * `save_json()` for API data
  * `save_csv()` for CSV data

* The system automatically:

  * Creates folders dynamically using timestamps
  * Stores files in the correct location
  * Ensures no overwriting of previous data

##  Technologies Used

* Python (`os`, `datetime`, `json`)
* Pandas (for CSV handling)
* Local filesystem (as data lake)

##  Key Features

* Structured data lake design
* Source-based partitioning
* Timestamp-based versioning
* Scalable and extendable
* Supports future cloud migration (e.g., AWS S3)

## Future Enhancements

* Integration with AWS S3 or MinIO
* Data version control improvements
* Partitioning by additional attributes (e.g., region, category)

## Conclusion

The raw data storage system is implemented successfully using a structured and scalable approach. It aligns with real-world data engineering practices and supports future pipeline expansion.