###############################################################################
#
#       Filename:  analyze.py
#
#    Description:  Parsed customers analysis.
#          Usage:  python3 analyze.py --customers <dataset>
#
#        Version:  1.0
#        Created:  25/06/2020 10:28:31 AM
#       Revision:  1
#
#         Author:  Gustavo P de O Celani
#
################################################################################

# Import
from progress.bar import IncrementalBar
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse
import time
import json
import os

# Argument Parser
argumentParser = argparse.ArgumentParser()
argumentParser.add_argument("-c", "--customers", required = True, help = "path to input parsed customers dataset")
args = vars(argumentParser.parse_args())

# Console start header
os.system("figlet \"Data Analysis\"")
print("\nCustomers path: ", args["customers"])

# Reading parsed customers json file
customers = []
with open(args["customers"], "r", encoding = "latin-1") as customersJsonFile:
    customers = json.load(customersJsonFile)

# Attributes usage analysis
print()
customerJsonKeys = list(customers[0].keys())
customerJsonKeysUsageCount = [0] * len(customerJsonKeys)
progressBar = IncrementalBar('Attributes Usage Analysis', max = len(customers))
for i in range(len(customers)):
    progressBar.next()
    for j in range(len(customers[0])):
        if customers[i][customerJsonKeys[j]] != '':
            customerJsonKeysUsageCount[j] += 1
progressBar.finish()

# Attibutes percent usage
print()
customerJsonKeysUsagePercent = [0] * len(customerJsonKeys)
progressBar = IncrementalBar('Attributes Percent Usage ', max = len(customerJsonKeys))
for i in range(len(customerJsonKeys)):
    progressBar.next()
    customerJsonKeysUsagePercent[i] = (customerJsonKeysUsageCount[i] / len(customers)) * 100
progressBar.finish()

# Building attribute usage tables
fullUsageTable = PrettyTable(['Attribute', 'Count', 'Usage [%]'])
allUsageTable  = PrettyTable(['Attribute'])
anyUsageTable  = PrettyTable(['Attribute'])
for i in range(len(customerJsonKeys)):
    fullUsageTable.add_row([customerJsonKeys[i], customerJsonKeysUsageCount[i], round(customerJsonKeysUsagePercent[i], 2)])
    if customerJsonKeysUsagePercent[i] == 100:
        allUsageTable.add_row([customerJsonKeys[i]])
    if customerJsonKeysUsagePercent[i] == 0:
        anyUsageTable.add_row([customerJsonKeys[i]])

# Printing attributes usage tables
print("\n%s" % fullUsageTable)
print("\n100%% Customers Usage Attibutes\n%s" % allUsageTable)
print("\n0%% Customers Usage Attibutes\n%s" % anyUsageTable)

# Plotting attributes usage analysis
input("\nPress ENTER to plot attributes usage graph...")
index = np.arange(len(customerJsonKeys))
plt.bar(index, customerJsonKeysUsageCount)
plt.title('Customer Enrollment Attibutes Usage')
plt.xlabel('Customer Enrollment Attibute', fontsize = 8)
plt.ylabel('Usage Count', fontsize = 8)
plt.xticks(index, customerJsonKeys, fontsize = 8, rotation = 90)
plt.show()

print()
exit()
