#!/bin/bash

#
# This script runs all tests
#
python3 -m unittest discover -v --start-directory tests/ --pattern "*_test.py"
