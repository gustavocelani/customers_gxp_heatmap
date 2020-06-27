###############################################################################
#
#       Filename:  dataset_parser.py
#
#    Description:  Generic run script.
#          Usage:  python3 dateset_parser.py --dataset <dataset> --output <output>
#
#        Version:  1.0
#        Created:  25/06/2020 09:51:44 AM
#       Revision:  1
#
#         Author:  Gustavo P de O Celani
#
################################################################################

# Import
from progress.bar import IncrementalBar
from geopy.geocoders import Nominatim
from html.parser import HTMLParser
import argparse
import time
import json
import os

# HTML Parser Class
class TableHtmlParser(HTMLParser):
    def __init__(self, **kwargs):
        super().__init__()
        self.data = ''

    def handle_data(self, data):
        if data.strip():
            self.data = data

# HTML Parser Object
htmlParser = TableHtmlParser()

# Argument Parser
argumentParser = argparse.ArgumentParser()
argumentParser.add_argument("-d", "--dataset", required = True, help = "path to input dataset")
argumentParser.add_argument("-o", "--output",  required = True, help = "path to output dataset")
args = vars(argumentParser.parse_args())

# Console start header
os.system("figlet \"Dataset Parser\"")
print("Dataset path: ", args["dataset"])
print("Output  path: ", args["output"])

# Reading HTML dataset file
rawHtmlDataset = open(args["dataset"], "r", encoding = "latin-1")
rawHtmlLines = rawHtmlDataset.readlines()

# Removing first lines until table starts
i = 1
for line in rawHtmlLines:
    i += 1
    if "<table" in line:
        break
del rawHtmlLines[:i]

# Parsing HTML table content data
print()
htmlParsingProgressBar = IncrementalBar('Parsing HTML Table   ', max = len(rawHtmlLines))
tableLines = []
auxLine = []
for i in range(len(rawHtmlLines)):
    htmlParsingProgressBar.next()
    if "<tr " in rawHtmlLines[i]:
        tableLines.append(auxLine)
        auxLine = []
    else:
        htmlParser.data = ''
        htmlParser.feed(rawHtmlLines[i])
        auxLine.append(htmlParser.data)
htmlParsingProgressBar.finish()

# Closing raw dataset HTML file
rawHtmlDataset.close()

# Table to JSON object
print()
jsonParsingProgressBar = IncrementalBar('Building JSON Dataset', max = len(tableLines) - 1)
customers = []
for j in range(1, len(tableLines)):
    jsonParsingProgressBar.next()
    parsedLine = {}
    for i in range(len(tableLines[0])):
        parsedLine[tableLines[0][i]] = tableLines[j][i]
    customer = json.dumps(parsedLine, ensure_ascii = False)
    customers.append(customer)
jsonParsingProgressBar.finish()

# Acquiring customers lat/long
print()
customersLocationProgressBar = IncrementalBar('Acquiring Geolocation', max = len(customers))
geolocator = Nominatim(user_agent = "Mozilla")
for i in range(len(customers)):
    customersLocationProgressBar.next()
    customerJson = json.loads(customers[i])
    address = "%s %s, %s, %s" % (customerJson["Tipo"], customerJson["Logradouro"], customerJson["Nº"], customerJson["Município"])
    location = geolocator.geocode(address, timeout = 20)
    if location:
        customerJson['Endereço']  = location.address
        customerJson['Latitude']  = location.latitude
        customerJson['Longitude'] = location.longitude
    else:
        customerJson['Endereço']  = address
        customerJson['Latitude']  = ''
        customerJson['Longitude'] = ''
    customers[i] = customerJson
customersLocationProgressBar.finish()

# Saving customers parsed data
os.makedirs(os.path.dirname(args["output"]), exist_ok = True)
with open(args["output"], 'w') as outfile:
    json.dump(customers, outfile)
print("\nParsed dataset saved successfully!")

print()
exit()
