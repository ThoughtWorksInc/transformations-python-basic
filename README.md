# Basic Repo for working with Pyspark
The purpose of this repo is to make sure you have everything set up to build and run a pyspark project locally.

## Pre-requisites
Please make sure you have the following installed and can run them
* Python 3.9 or later
* pipenv
* Java 8 or later

## Set up virtual environment
To set up the virtual environment and to install all dependencies run
```bash
pipenv install --dev
```

## Run tests
```bash
pipenv run pytest
```

Please confirm that all of the tests pass.

## Setup for local run with pyspark
To run the spark job locally, first package it:
```bash
pipenv run packager
```

Then you can submit the spark job with (note that the python version in the file name
should match the version in your environment):
```bash
pipenv run spark-submit \
    --master local \
    --py-files dist/transformations_basic-0.1.0-py3.9.egg \
    jobs/hello_spark.py
```

Confirm that you see "Hello Spark" in the output log file (`./project.log`).

If all the test passed locally and "Hello Spark" was in the output log file than your environment is set up and ready for a TW Data Engineering coding interview.
