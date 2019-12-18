import os
import json
import random

# Read in json file to get relationships (suncg_proximity)
allRoomTypes = []  # keep track of roomtype at index

objectsJSON = []
# index is id num, string at index position is associated with that id num
objectsJSONFrequencies = []
relationshipsJSON = []
relationshipsJSONFrequencies = []

allObjectsJSON = []
allObjectsFreqJSON = []
allRelationshipsJSON = []
allRelationshipsFreqJSON = []

RelationshipFrequenciesJSON = []
allRelationshipFrequenciesJSON = []
# multiple both object freq and relationship freq to get relationship existing freq

with open("suncg_proximity.json") as json_file:
    data = json.load(json_file)
    count = 0
    for rm in data["motifs"]:
        objectsJSON = []
        objectsJSONFrequencies = []
        relationshipsJSON = []
        relationshipsJSONFrequencies = []
        RelationshipFrequenciesJSON = []
        # holds overall rel freq (2 obj and rel freqs mult together)
        allRoomTypes.append(rm)
        # print(data["motifs"][rm])
        for v in data["motifs"][rm]["vertices"]:
            objectsJSON.append(v["name"])  # add object to ids list
            objectsJSONFrequencies.append(v["frequency"])
        # allObjectsJSON.append(objectsJSON)
        # allObjectsFreqJSON.append(objectsJSONFrequencies)
        for p in data["motifs"][rm]["probability"]:
            relationshipsJSONFrequencies.append(p["value"])
        # allRelationshipsFreqJSON.append(relationshipsJSONFrequencies)
        relCount = 0
        for r in data["motifs"][rm]["rules"]:
            relationshipString = (
                ""
                + objectsJSON[int(r["source"])]
                + "_"
                + r["factor"]
                + "_"
                + objectsJSON[int(r["target"])]
                + "_id_"
                + str(relCount)
            )
            relationshipsJSON.append(relationshipString)
            # print(objectsJSONFrequencies[(int(r["source"]))])
            relationshipChanceOfExisting = (
                objectsJSONFrequencies[(int(r["source"]))]
                * objectsJSONFrequencies[(int(r["target"]))]
                * relationshipsJSONFrequencies[(int(r["id"]))]
            )
            RelationshipFrequenciesJSON.append(
                relationshipChanceOfExisting
            )  # chance of a relationship existing per room of roomtype
            relCount = relCount + 1

        allRelationshipsJSON.append(relationshipsJSON)
        allRelationshipFrequenciesJSON.append(RelationshipFrequenciesJSON)
        # print(allRelationshipFrequenciesJSON[0])
        count = count + 1
json_file.close()

# print(allRoomTypes)

# print(allObjectsJSON)
# print(allObjectsFreqJSON)
# print(allRelationshipsJSON)
# print(allRelationshipsFreqJSON)

# print(allRelationshipFrequenciesJSON)
# print(allRelationshipsJSON[0])


allObjectsByRoomType = []  # list of list of objects by room type
allRoomsByRoomType = []  # list of list of rooms by room type
roomTypeIndex = []  # keep track of what file is associated with each index

# Note: To find what a specific object correlates to a 0 or 1 in a specific room, we use its index and search for the object in the object array that correlates with it.

fileCount = 0
relationshipsCreated = 0
for filename in os.listdir("FisherRooms"):  # for each set of rooms in FisherRooms
    file = open("FisherRooms/" + filename, "r")  # open up set of rooms
    objectsLine = file.readline()  # read line of objects
    objectsLine = objectsLine[0 : len(objectsLine) - 1]  # remove '\n' at end of string
    objects = objectsLine.split(",")  # seperate objects by comma

    roomTypeIndex.append(filename)  # add room type to roomTypeIndex

    for i in range(0, len(objects)):
        objects[i] = objects[i].replace('"', "")  # remove double qoutes from objects
    for i in range(0, len(allRelationshipsJSON[fileCount])):
        objects.append(allRelationshipsJSON[fileCount][i])
    allObjectsByRoomType.append(objects)
    # add objects for specific room type to list, needed for global list later on

    # print(objects)
    # exit()  # used for testing

    rooms = []
    while True:  # read in rooms until end of file
        roomLine = file.readline()  # room ex: 1,1,0,0 ...
        roomLine = roomLine[0 : len(roomLine) - 1]  # remove '\n' at end of string
        if not roomLine:  # end of file
            break
        room = roomLine.split(",")  # split 0s and 1s into list
        # print(room)
        # before appending room, add in relationship 1s and 0s by using overall relationship frequency
        for i in range(len(allRelationshipFrequenciesJSON[fileCount])):
            # for each object in
            chance = random.uniform(0, 1)
            # print(chance)
            if chance <= allRelationshipFrequenciesJSON[fileCount][i]:
                # if random number is <= to object frequnecy make 1, else 0
                room.append(1)
                relationshipsCreated = relationshipsCreated + 1
            else:
                room.append(0)
        rooms.append(room)
        # add room list to rooms (list of all rooms of certain room type)
    allRoomsByRoomType.append(rooms)
    # add list of rooms to overall list of rooms, needed for global list later on
    file.close()
print("Relationships Created: " + str(relationshipsCreated))
# at this point all text files have been read

# now create list of all objects from every room type, no overlap
globalObjectsList = []

for i in range(0, len(allObjectsByRoomType)):  # go through each list of objects
    for o in allObjectsByRoomType[i]:
        # for all objects in allObjectsByRoomType at index i (room type)
        if o not in globalObjectsList:  # if object not in globalObjectsList
            globalObjectsList.append(o)  # add object to globalObjectsList
globalObjectsList.sort()  # sort for organization purposes

generalizedRooms = []
# we now want to recreate each of the rooms according to globalObjectsList

print("Generalizing rooms, this may take a while...")

globalRoomTypeIndex = []
# this will keep track of what the original room type was for a room in generalizedRooms
# we will use this to keep track of what the original rooms were when we perform clustering on them to get a good picture of before and after


for i in range(0, len(allRoomsByRoomType)):  # for each roomtype
    curRoomType = roomTypeIndex[i]  # get current room type

    for x in range(0, len(allRoomsByRoomType[i])):  # for each room in specific roomtype
        globalRoomTypeIndex.append(curRoomType)
        # add current room type to list at index

        revisedRoom = [0] * len(globalObjectsList)  # create new empty room
        # now we have a list of 0s, we now need to change present objects to 1
        for y in range(0, len(allRoomsByRoomType[i][x])):
            # y iterates through specific room, should be 0s and 1s
            curObjectIndex = globalObjectsList.index(allObjectsByRoomType[i][y])
            # get object at current position of roomtype and find its index in globalObjectsList
            if allRoomsByRoomType[i][x][y] == "1":
                # if object is present in current room
                # print("if hit")
                revisedRoom[curObjectIndex] = 1  # set object in revisedRoom to 1
        generalizedRooms.append(revisedRoom)  # add revisedRoom to generalizedRooms

print("Creating GenRoomsFISHERObjectAndRelationshipsRoomTypeIndex.txt...")
# write global room type to its own file for later use
file = open("GenRoomsFISHERObjectAndRelationshipsRoomTypeIndex.txt", "w")
# write objects first
for i in range(0, len(globalRoomTypeIndex)):
    file.write('"')
    file.write(globalRoomTypeIndex[i])
    file.write('"')
    file.write("\n")
file.close()

# write generalized rooms to file GeneralizedRooms.txt
file = open("GenRoomsFISHERObjectsAndRelationships.txt", "w")
# write objects first
for i in range(0, len(globalObjectsList) - 1):
    file.write('"')
    file.write(globalObjectsList[i])
    file.write('"')
    file.write(",")
file.write('"')
file.write(globalObjectsList[len(globalObjectsList) - 1])
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
