#!/bin/bash

set -euo pipefail

#
# This script installs required dependencies.
#

sudo apt update

sudo apt-get --yes install pipx
pipx install pipenv
pipenv install --dev
