import logging

from transformations_basic import hello_spark

if __name__ == '__main__':
    LOG_FILENAME = 'project.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    hello_spark.run()
