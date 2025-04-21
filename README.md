# Cloud Data Engineer — Project Repository

Welcome to the **Cloud Data Engineer** lab — a portfolio-style repository that showcases real-world data engineering and data science projects using modern cloud technologies such as AWS, GCP, and open public data.

This repository is structured to reflect professional development practices, with each subproject demonstrating specific cloud pipelines, automation techniques, and scalable architectures.

---

## Purpose

To consolidate hands-on cloud projects that:
- Showcase practical skills in data ingestion, transformation, and storage
- Leverage public APIs and cloud services (e.g., AWS S3, BigQuery, Cloud Functions)
- Apply best practices in modular development, reproducibility, and documentation
- Serve as a portfolio for recruiters and technical leads

---

## Subprojects

### [ETL: ANEEL Complaint Data to AWS](./etl_ANEEL_AWS/)
> Extracts consumer complaint data from the ANEEL public API, transforms the dataset using Pandas, and uploads it to an AWS S3 bucket.

- Technologies: Python, AWS S3, Boto3, Poetry, Taskipy
- Focus: REST API ingestion, transformation, cloud-native ETL pipeline
- Automation: Run and deploy using `task run` and `task deploy`

---

## Tools & Technologies

- **AWS (S3, CLI, boto3)**
- **Python (3.9+)**
- **Poetry** – Dependency management
- **Taskipy** – Automation with `task run`, `task deploy`
- **Pandas, Requests** – Data handling and HTTP access

---

## How to Use

Clone the repository:

```bash
git clone https://github.com/leticiagcsilva/Cloud_Data_Engineer.git
cd Cloud_Data_Engineer
```

Install dependencies and run projects using:

```bash
poetry install
poetry run task run
```

---

Feel free to explore each project — they’re designed to be insightful, modular, and production-ready.
