# Hadoop Ecosystem — Word Count with PySpark on Dataproc

This subproject runs a classic word count job using **Apache Spark** on **Google Cloud Dataproc**, reading data from a GCS bucket and saving the output back to GCS.

## 📄 Script

- `wordcount_spark.py`: PySpark script that reads a `.txt` file from GCS, counts word frequencies, and saves results sorted by frequency.

## 🧪 How to Run on Dataproc

```bash
# Submit job to Dataproc
gcloud dataproc jobs submit pyspark wordcount_spark.py \
  --cluster=your-cluster-name \
  --region=your-region \
  -- gs://your-bucket/livro.txt gs://your-bucket/resultado
```

## 🧰 Requirements

- Google Cloud CLI configured
- A Dataproc cluster running
- Input file (e.g. `livro.txt`) uploaded to a GCS bucket

## ✅ Example

```bash
gcloud dataproc jobs submit pyspark wordcount_spark.py \
  --cluster=cluster-spark \
  --region=southamerica-east1 \
  -- gs://meu-bucket/livro.txt gs://meu-bucket/resultado
```

---

This is a fundamental demonstration of distributed computation using Spark and Hadoop ecosystem tools on the cloud.
