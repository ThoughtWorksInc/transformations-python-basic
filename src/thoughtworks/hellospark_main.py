import logging
from pyspark.sql import SparkSession


def main(args):
    spark = SparkSession.builder.appName("Hello Spark App").getOrCreate()
    logging.info("Hello Spark")
    spark.stop()
