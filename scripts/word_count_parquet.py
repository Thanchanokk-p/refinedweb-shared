import re
from collections import Counter

from pyspark.sql.types import StructType, StructField, StringType, LongType
from pyspark.sql.functions import explode, split, lower, col, monotonically_increasing_id

from sparkcc import CCSparkJob 


class WordCountFromParquetJob(CCSparkJob):
    """
    Spark job to compute word count (TF) and document frequency (DF)
    from a Parquet file, e.g., `primark.parquet`, that has a text column "content".
    """

    name = "WordCountFromParquet"

    # Define schema for output: (word, {tf, df})
    output_schema = StructType([
        StructField("key", StringType(), True),
        StructField("val", StructType([
            StructField("tf", LongType(), True),
            StructField("df", LongType(), True)]), True)
    ])

    @staticmethod
    def reduce_by_key_func(a, b):
        # Reduce logic to combine term frequencies and doc frequencies
        return ((a[0] + b[0]), (a[1] + b[1]))

    def run_job(self, session):
        # Load Parquet input (e.g. --input filtered_data/primark.parquet)
        df = session.read.parquet(self.args.input)

        # Add a document ID to identify rows
        df = df.withColumn("doc_id", monotonically_increasing_id())

        # Tokenize the content into lowercase words using regex
        words_df = df.select(
            "doc_id",
            explode(split(lower(col("content")), r"\W+")).alias("word")
        ).filter(col("word") != "")  # Remove empty words

        # Calculate Term Frequency (TF): how often each word appears
        tf_df = words_df.groupBy("word").count().withColumnRenamed("count", "tf")

        # Calculate Document Frequency (DF): in how many documents each word appears
        df_df = words_df.dropDuplicates(["doc_id", "word"]) \
                        .groupBy("word").count().withColumnRenamed("count", "df")

        # Merge TF and DF on each word
        result_df = tf_df.join(df_df, on="word")

        # Convert to required output format
        final_rdd = result_df.rdd.map(lambda row: (
            row["word"],
            {"tf": row["tf"], "df": row["df"]}
        ))

        # Save output in Spark table or folder as defined by --output
        session.createDataFrame(final_rdd, schema=self.output_schema) \
            .coalesce(self.args.num_output_partitions) \
            .write \
            .format(self.args.output_format) \
            .option("compression", self.args.output_compression) \
            .options(**self.get_output_options()) \
            .saveAsTable(self.args.output)


# Run the job via CLI
if __name__ == "__main__":
    job = WordCountFromParquetJob()
    job.run()
