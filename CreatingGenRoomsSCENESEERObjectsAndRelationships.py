import json
import os

allRoomTypes = []  # keep track of roomtype at index
allRoomDetails = []  # all room details in one list, index of room matches allRoomValues
allRoomValues = []  # all room values in one list, index of room matches allRoomDetails

for filename in os.listdir("SceneSeer"):  # for each room
    # add roomType to allRoomsByRoomType
    roomType = filename
    badChars = "_0123456789"
    for char in badChars:
        roomType = roomType.replace(char, "")
    allRoomTypes.append(roomType)

    ids = []  # index is id num, string at index position is associated with that id num
    roomDetails = []  # keeps track of what objects and relationships are in room
    roomValues = []  # keeps track of values, match index of roomDetails array
    with open("SceneSeer/" + filename) as json_file:
        data = json.load(json_file)
        objectCount = 0
        for v in data["vertices"]:
            ids.append(v["name"])  # + "_" + str(objectCount))  # add object to ids list
            roomDetails.append(v["name"])  # + "_" + str(objectCount))
            # add object to roomDetails
            roomValues.append(1)
        for r in data["rules"]:
            relationshipString = (
                ""
                + ids[int(r["source"])]
                + "_"
                + r["factor"]
                + "_"
                + ids[int(r["target"])]
            )
            roomDetails.append(relationshipString)
            roomValues.append(1)
    allRoomDetails.append(roomDetails)
    allRoomValues.append(roomValues)
    json_file.close()

print("Done making individual room details/values")

# print(allRoomTypes[10])
# print(allRoomDetails[10])
# print(allRoomValues[10])
# exit()

# now create list of all objects from every room type, no overlap
globalDetailsList = []

print(len(allRoomDetails))

for i in range(0, len(allRoomDetails)):  # go through list of all room details
    for o in allRoomDetails[i]:  # for all details in allRoomDetails at index i (room)
        if o not in globalDetailsList:  # if detail not in globalObjectsList
            globalDetailsList.append(o)  # add detail to globalObjectsList
    print(str(i) + "/2720")
globalDetailsList.sort()  # sort for organization purposes

print("globalDetailsList:")
print(globalDetailsList)

generalizedRooms = []
# we now want to recreate each of the rooms according to globalDetailsList

print("Generalizing rooms, this may take a while...")

for i in range(0, len(allRoomDetails)):  # for each room set of details
    revisedRoom = [0] * len(globalDetailsList)  # create new empty room
    # now we have a list of 0s, we now need to change present objects to 1 or respective value (like frequency)
    for y in range(0, len(allRoomValues[i])):
        # y iterates through specific room values, should be not 0
        curDetailIndex = globalDetailsList.index(allRoomDetails[i][y])
        # get detail at current position of room and find its index in globalDetailsList
        if str(allRoomValues[i][y]) == "1":  # if object is present in current room
            # print("if hit")
            revisedRoom[curDetailIndex] = 1  # set object in revisedRoom to 1
    generalizedRooms.append(revisedRoom)  # add revisedRoom to generalizedRooms

# print(generalizedRooms)

print("Creating GenRoomsSCENESEERObjectsAndRelationshipsRoomTypeIndex.txt...")
# write global room type to its own file for later use
file = open("GenRoomsSCENESEERObjectsAndRelationshipsRoomTypeIndex.txt", "w")
# write objects first
for i in range(0, len(allRoomTypes)):
    file.write(allRoomTypes[i])
    file.write("\n")
file.close()

# write generalized rooms to file GenRoomsKERMANIObjectsAndRelationships.txt
file = open("GenRoomsSCENESEERObjectsAndRelationships.txt", "w")
# write details first
for i in range(0, len(globalDetailsList) - 1):
    file.write('"')
    file.write(globalDetailsList[i])
    file.write('"')
    file.write(",")
file.write('"')
file.write(globalDetailsList[len(globalDetailsList) - 1])
file.write('"')
file.write("\n")

# next write generalized rooms
for x in range(0, len(generalizedRooms)):
    for y in range(0, len(generalizedRooms[x]) - 1):
        temp = str(generalizedRooms[x][y]) + ","
        file.write(temp)
    file.write(str(generalizedRooms[x][y + 1]))
    file.write("\n")

file.close()