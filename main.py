#!/usr/bin/env python

import sys, os
import logging, argparse, configparser

from logging.config import fileConfig
from utils import *


def main():

    fileConfig('logger.ini')
    logger = logging.getLogger('main')
    logger.info("Executing " + __name__)

    # Arguments passed to the analysis
    parser = argparse.ArgumentParser(description='Simple test application')
    parser.add_argument('-p','--path', required=False)
    parser.add_argument('-e','--export', required=False, default=False)
    parser.add_argument('-t','--type', required=False, choices=["USER", "WORD", "DOW", "*"], default="*")
    args = parser.parse_args()

    for value in vars(args):
        print(value)

    # Configuration file
    config = configparser.ConfigParser(allow_no_value=True)
    config.read('config.ini')

    string = config.get('DEFAULT', 'string')
    write(string)

    sys.exit(0)

if __name__ == "__main__":
    main()
