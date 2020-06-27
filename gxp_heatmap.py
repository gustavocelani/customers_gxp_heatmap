###############################################################################
#
#       Filename:  gxp_heatmap.py
#
#    Description:  Build and show GXP customers location heatmap.
#          Usage:  python3 gxp_heatmap.py --customers <dataset>
#
#        Version:  1.0
#        Created:  25/06/2020 16:33:47 AM
#       Revision:  1
#
#         Author:  Gustavo P de O Celani
#
################################################################################

# Import
from progress.bar import IncrementalBar
import matplotlib.pyplot as plt
import argparse
import time
import json
import csv
import os

# Argument Parser
argumentParser = argparse.ArgumentParser()
argumentParser.add_argument("-c", "--customers", required = True, help = "path to input parsed customers dataset")
args = vars(argumentParser.parse_args())

# Console start header
os.system("figlet \"GXP Heatmap\"")
print("\nCustomers path: ", args["customers"])

# Reading parsed customers json file
customers = []
with open(args["customers"], "r", encoding = "latin-1") as customersJsonFile:
    customers = json.load(customersJsonFile)

# Reading GXP map
gxpMapImage = plt.imread('./maps/gxp_map.png')
gxpMapBorders = []
with open("./maps/gxp_map_borders.txt") as mapBorders:
    gxpMapBorders = mapBorders.read().split(",")
    for i in range(len(gxpMapBorders)):
        gxpMapBorders[i] = float(gxpMapBorders[i])

# GXP Map Limiters
gxpMinLon = gxpMapBorders[0]
gxpMaxLon = gxpMapBorders[1]
gxpMaxLat = gxpMapBorders[2]
gxpMinLat = gxpMapBorders[3]

# Filtering lat/lon
print()
progressBar = IncrementalBar('Latitude/Longitude Normalization', max = len(customers))
longitudeArray = []
latitudeArray = []
notFoundLocationsCount = 0
outOfGxpLocationCount = 0
for customer in customers:
    progressBar.next()
    lat = customer['Latitude']
    lon = customer['Longitude']
    if lat != '' and lon != '':
        if lon > gxpMinLon and lon < gxpMaxLon and lat > gxpMinLat and lat < gxpMaxLat:
            longitudeArray.append(lon)
            latitudeArray.append(lat)
        else:
            outOfGxpLocationCount += 1
    else:
        notFoundLocationsCount += 1
progressBar.finish()

# Building location metrics
print()
print("Total Customers.............. %4s [ %5s%% ]" % (len(customers), round(100, 2)))
print("Not Found Locations.......... %4s [ %5s%% ]" % (notFoundLocationsCount, round(notFoundLocationsCount/len(customers)*100, 2)))
print("Out of GXP Locations......... %4s [ %5s%% ]" % (outOfGxpLocationCount, round(outOfGxpLocationCount/len(customers)*100, 2)))
print("                              ---------------")
print("Total Locations Used......... %4s [ %5s%% ]" % ((len(customers)-notFoundLocationsCount-outOfGxpLocationCount), round((len(customers)-notFoundLocationsCount-outOfGxpLocationCount)/len(customers)*100, 2)))

# Plotting heatmap
input("\nPress ENTER to plot gxp heatmap...")
plt.scatter(x = longitudeArray, y = latitudeArray, zorder = 1, c = 'b', s = 10)
plt.title("Customers Heatmap")
plt.xlabel("Longitude", fontsize = 8)
plt.ylabel("Latitude", fontsize = 8)
plt.imshow(gxpMapImage, zorder = 0, extent = gxpMapBorders, aspect = 'equal')
plt.show()

print()
exit()
