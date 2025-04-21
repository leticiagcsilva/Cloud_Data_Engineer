# Cloud Data Engineer — Project Repository

Welcome to the **Cloud Data Engineer** lab — a portfolio-style repository that showcases real-world data engineering and data science projects using modern cloud technologies such as AWS, GCP, and open public data.

This repository is structured to reflect professional development practices, with each subproject demonstrating specific cloud pipelines, automation techniques, and scalable architectures.

---

## Purpose

To consolidate hands-on cloud projects that:
- Showcase practical skills in data ingestion, transformation, and storage
- Leverage public APIs and cloud services (e.g., AWS S3, BigQuery, Cloud Functions, Dataproc)
- Apply best practices in modular development, reproducibility, and documentation
- Serve as a portfolio for recruiters and technical leads

---

## Subprojects

### 🔹 [ETL: ANEEL Complaint Data to AWS](./etl_ANEEL_AWS/)
> Extracts consumer complaint data from the ANEEL public API, transforms the dataset using Pandas, and uploads it to an AWS S3 bucket.

- **Technologies:** Python, AWS S3, Boto3, Poetry, Taskipy  
- **Focus:** REST API ingestion, transformation, cloud-native ETL pipeline  
- **Automation:** Run and deploy using `task run` and `task deploy`

---

### 🔹 [Hadoop Ecosystem — PySpark Word Count](./Ecossistema_Hadoop/)
> Runs a distributed word count job using PySpark on Google Cloud Dataproc, processing a text file stored on GCS and saving the sorted word frequencies.

- **Technologies:** PySpark, Google Cloud Dataproc, GCS  
- **Focus:** Big Data processing with Hadoop ecosystem  
- **Execution:** `gcloud dataproc jobs submit pyspark ...`

---

## Tools & Technologies

- **Cloud Platforms:** AWS (S3), GCP (Dataproc, GCS)
- **Languages & Frameworks:** Python, PySpark
- **Package & Task Management:** Poetry, Taskipy
- **Libraries:** Pandas, Requests, Boto3

---

## How to Use

Clone the repository:

```bash
git clone https://github.com/leticiagcsilva/Cloud_Data_Engineer.git
cd Cloud_Data_Engineer