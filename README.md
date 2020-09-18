# Basic Repo for working with Pyspark
The purpose of this repo is to make sure you have everything set up to build and run a pyspark project locally.

## Pre-requisites
Please make sure you have the following installed and can run them
* Python 3.6 or later
* PySpark (`pip install pyspark`)
* PyCharm IDE

## Setup for local building and testing
* Clone the repo
* cd project/src
* Test: `python3 -m unittest`

Please confirm that all of the tests pass.

## Setup for local run with pyspark
To run the spark job locally:
```
spark-submit --master local job_runner.py
```

Confirm that you see "Hello Spark" in the output log file .

If all the test passed locally and "Hello Spark" was in the output log file than your environment is set up and ready for a TW Data Engineering coding interview.
