import sys
from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: wordcount_hdfs.py <input_hdfs_path> <output_hdfs_path>", file=sys.stderr)
        sys.exit(-1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    sc = SparkContext(appName="PySpark Word Count - Local HDFS")
    words = sc.textFile(input_path).flatMap(lambda line: line.split(" "))
    
    # Map words to (word, 1), reduce by key, and sort
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    sortedCounts = wordCounts.sortBy(lambda a: a[1], ascending=False)

    sortedCounts.saveAsTextFile(output_path)

    sc.stop()
