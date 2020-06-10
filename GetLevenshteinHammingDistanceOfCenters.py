from Levenshtein import *
from warnings import warn

# TEMPLATE
# result = []
# result.append(hamming("000010","100010"))
# result.append(hamming("100100","011011"))
# print(result)

# read in centers into list
# file = open("FisherCentersObjectPresence.txt","r") #change file name for centers you want to measure
file = open("KermaniSceneSeerObjectPresenceBedroomsBathroomsLivingRooms9CentersSUNRGBD.txt", "r")
centers = []

while True:  # read in centers until end of file
    centerLine = file.readline()
    centerLine = centerLine[0 : len(centerLine) - 1]  # remove '\n' at end of string
    if not centerLine:  # end of file
        break
    centers.append(centerLine)

file.close()

# print(len(centers))

hammingDistances = (
    []
)  # outer list is each center by index (0-72), each inner list is the list of hamming distances of that index center
# each inner list should be 1 smaller in length since not comparing to every other center to prevent redundancy

# now run hamming distance on every center against every other center
centerPos = 0  # keep track of what center you are on in list
totalComparisons = 0
for i in range(
    len(centers)
):  # cycles through every center, outer list in hammingDistances
    distances = []  # new hamming distances
    for d in range(centerPos, len(centers)):
        if i != d:  # make sure not to compare a center to itself
            distances.append(hamming(centers[i], centers[d]))
            totalComparisons = totalComparisons + 1
            # print(str(i) +" and "+str(d))
    hammingDistances.append(distances)
    print(len(hammingDistances[i]))
    centerPos = centerPos + 1

print("Total Comparisons: " + str(totalComparisons))
print(hammingDistances)
# print(len(hammingDistances))

# now conduct an overall average distance
# first get average for each center
centerAvgDists = []
for i in range(len(centers)):
    centerTotalDist = 0  # avg for distances
    for d in range(len(centers[i])):
        centerTotalDist = centerTotalDist + int(centers[i][d])
    print("Center " + str(i) + ": " + str(centerTotalDist / len(centers[i])))
    centerAvgDists.append(centerTotalDist / len(centers[i]))

# print(centerAvgDists)
# print(len(centerAvgDists))

# now get final avg dist
allCenterAvgDist = 0
for i in range(len(centerAvgDists)):
    allCenterAvgDist = allCenterAvgDist + centerAvgDists[i]
finalAvgDist = allCenterAvgDist / len(centerAvgDists)
print("Final Average Distance: " + str(finalAvgDist))
