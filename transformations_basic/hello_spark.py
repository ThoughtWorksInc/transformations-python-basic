import logging

from pyspark.sql import SparkSession


def run():
    spark = SparkSession.builder.appName("Hello Spark App").getOrCreate()
    logging.info("Hello Spark")
    spark.stop()
