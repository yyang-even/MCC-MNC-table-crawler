#!/bin/bash

#
# This script runs all tests
#
pipenv run python3 -m unittest discover -v --start-directory tests/ --pattern "*_test.py"
