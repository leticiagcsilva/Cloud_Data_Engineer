# Cloud Data Projects — Documentation Index

Welcome to the documentation hub for the **Cloud_Data_Engineer** project repository.

This space indexes all subprojects and cloud-based solutions, offering detailed insight into architecture, technology choices, and use cases.

---

## 🔍 Project Index

### 1. [ETL: ANEEL Complaint Data to AWS](./etl_ANEEL_AWS/README.md)
**Description:**  
Extracts consumer complaint data from the Brazilian electricity regulator (ANEEL), cleans the data with Pandas, and loads it into an AWS S3 bucket.

- **Focus:** Cloud-native ETL pipeline
- **Stack:** Python, Pandas, Boto3, AWS S3
- **Automation:** Poetry + Taskipy

---

### 2. [Hadoop Ecosystem — PySpark Word Count](./Ecossistema_Hadoop/README.md)
**Description:**  
A distributed word count job using PySpark on Google Cloud Dataproc, reading from GCS and saving sorted word frequencies back to GCS.

- **Focus:** Big Data, Hadoop ecosystem
- **Stack:** PySpark, Dataproc, GCS

---

## About this Documentation

This documentation is generated using [**MkDocs**](https://www.mkdocs.org/), a static site generator for project documentation written in Markdown.

To start the local documentation server:

```bash
# Install MkDocs if not installed
pip install mkdocs

# Launch documentation site locally
mkdocs serve
```

To build the static site:

```bash
mkdocs build
```

---
For more projects and updates, explore the full repository or contact the maintainer.
