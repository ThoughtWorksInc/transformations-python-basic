import unittest
from pyspark.sql import SparkSession


class HelloSparkTest(unittest.TestCase):

    def test_true_should_be_true(self):
        self.assertEqual(True, True)

    def test_spark_can_be_run(self):
        self.spark = SparkSession.builder.appName("Test Spark Session").getOrCreate()
        self.assertEqual(self.spark.sparkContext.appName, "Test Spark Session")
        self.spark.stop()


if __name__ == '__main__':
    unittest.main()
