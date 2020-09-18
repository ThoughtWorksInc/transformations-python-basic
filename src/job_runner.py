import sys
import logging
from thoughtworks import hellospark_main

if __name__ == '__main__':
    LOG_FILENAME = 'project.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    hellospark_main.main(sys.argv)
