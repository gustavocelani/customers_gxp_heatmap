#!/bin/bash

###############################################################################
#
#       Filename:  full_run.sh
#
#    Description:  Generic run script.
#
#        Version:  1.0
#        Created:  26/06/2020 20:07:12 PM
#       Revision:  1
#
#         Author:  Gustavo P de O Celani
#
################################################################################

# Raw dataset path
DATASET_PATH="./dataset/example_dataset.html"
# Parsed customers path
CUSTOMERS_PATH="./out/example_customers.txt"

# Clearing console to start
clear

################################################################################
# Parsing raw dataset
################################################################################
if [[ ! -f "${CUSTOMERS_PATH}" ]]; then
    python3 dataset_parser.py --dataset ${DATASET_PATH} --output ${CUSTOMERS_PATH}

    if [[ ! -f "${CUSTOMERS_PATH}" ]]; then
        exit
    fi
fi

################################################################################
# Customers Analysis
################################################################################
python3 analyze.py --customers ${CUSTOMERS_PATH}

################################################################################
# Customers Gxp Heatmap
################################################################################
python3 gxp_heatmap.py --customers ${CUSTOMERS_PATH}

