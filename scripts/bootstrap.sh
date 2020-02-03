#!/bin/bash

#
# This script installs/updates all dependencies
#
pipenv install --dev

pre-commit install
