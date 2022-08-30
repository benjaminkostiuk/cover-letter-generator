#!/bin/bash

# Get full path to this executable
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Shell script for windows
python "$SCRIPT_DIR/src/create-cover-letter.py" $1
