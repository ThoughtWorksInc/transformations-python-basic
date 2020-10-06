from pyspark.sql import SparkSession


def test_spark_can_be_run():
    spark = SparkSession.builder.appName("Test Spark Session").getOrCreate()
    assert "Test Spark Session" == spark.sparkContext.appName
