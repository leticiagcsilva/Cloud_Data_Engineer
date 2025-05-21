# Word Count with PySpark on Local Hadoop (Dataproc Simulation)

This subproject demonstrates a distributed **word count** pipeline using **PySpark**, executed on a local Hadoop cluster with HDFS — simulating the behavior of Google Cloud Dataproc.

---

## Overview

This job:
- Reads a `.txt` file stored in **local HDFS**
- Splits text into words
- Counts the frequency of each word
- Sorts by frequency
- Writes the result back to HDFS

It uses PySpark transformations like `textFile`, `flatMap`, `map`, `reduceByKey`, `sortBy`, and `saveAsTextFile`. These operations are scalable and compatible with distributed processing.

---

## Project Structure

```
distributed-news-pipeline/
├── wordcount_hdfs.py           # Main PySpark job script
├── README.md                   # This documentation file
```

---

## Technologies Used

- PySpark
- Local Hadoop HDFS (Docker simulated)
- Docker Compose (Spark + HDFS)
- Optional Hive Metastore (for other processing layers)

---

## How to Run Locally

Make sure your Spark + HDFS cluster is running via Docker Compose, and that your input text file has been saved to HDFS:

### Example upload:
```bash
docker exec -it namenode hdfs dfs -put ./example.txt /data/input/book.txt
```

### Run the job:
```bash
spark-submit wordcount_hdfs.py \
  hdfs://namenode:8020/data/input/book.txt \
  hdfs://namenode:8020/data/output/wordcount_result
```

> Adjust paths as needed.

---

## Output

Files `part-0000x` will be created in the output folder `/data/output/wordcount_result` inside HDFS, containing:

```
(word, count)
```

You can view results with:
```bash
docker exec -it namenode hdfs dfs -cat /data/output/wordcount_result/part-00000
```

---

## Cloud Comparison

| Local (on-prem)     | GCP                         | AWS                   |
|---------------------|------------------------------|------------------------|
| Spark + Local HDFS  | Dataproc + Cloud Storage     | EMR + S3               |
| `spark-submit`      | `gcloud dataproc jobs submit`| AWS CLI / StepFn       |
| HDFS                | GCS                          | S3                    |

This project mirrors what you would run on Dataproc, but fully local and reproducible using Docker.
