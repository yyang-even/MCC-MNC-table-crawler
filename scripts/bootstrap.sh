#!/bin/bash

set -euo pipefail

#
# This script setup develop environment by installing required libraries
#

THIS_DIR=$(dirname "$0")

$THIS_DIR/dependencies.sh

source $THIS_DIR/utils.sh

PROJECT_ROOT_DIR=$(GetProjectRootDir)
INSTALLER_FILE=$PROJECT_ROOT_DIR/../config-sh/scripts/install_all_hooks.sh

if [ -f "$INSTALLER_FILE" ]; then
    $INSTALLER_FILE
else
    sudo apt-get --yes install pipx
    pipx install pre-commit
    pre-commit install
fi
