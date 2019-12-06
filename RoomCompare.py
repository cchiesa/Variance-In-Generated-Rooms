import os
allObjectsByRoomType = [] #list of list of objects by room type
allRoomsByRoomType = [] #list of list of rooms by room type
roomTypeIndex = [] #keep track of what file is associated with each index

#Note: To find what a specific object correlates to a 0 or 1 in a specific room, we use its index and search for the object in the object array that correlates with it.

for filename in os.listdir("FisherRooms"): #for each set of rooms in FisherRooms
    print(filename)
    file = open("FisherRooms/" + filename,"r") #open up set of rooms
    objectsLine = file.readline() #read line of objects
    objectsLine = objectsLine[0 : len(objectsLine)-1] #remove '\n' at end of string
    objects = objectsLine.split(',') #seperate objects by comma
    
    roomTypeIndex.append(filename) #add room type to roomTypeIndex

    for i in range(0, len(objects)):
        objects[i] = objects[i].replace('"',"") #remove double qoutes from objects
    allObjectsByRoomType.append(objects) #add objects for specific room type to list, needed for global list later on

    rooms = []
    while True: #read in rooms until end of file
        roomLine = file.readline() #room ex: 1,1,0,0 ...
        roomLine = roomLine[0 : len(roomLine)-1] #remove '\n' at end of string
        if not roomLine: #end of file
            break
        room = roomLine.split(',') #split 0s and 1s into list
        rooms.append(room) #add room list to rooms (list of all rooms of certain room type)
        #print(rooms)
        #print(objects)
        #print("Room Size: ")
        #print(len(rooms[0]))
        #print("Objects Size: ")
        #print(len(objects))
    print("Amount of rooms in " + filename + ": ")
    print(len(rooms))
    allRoomsByRoomType.append(rooms) #add list of rooms to overall list of rooms, needed for global list later on
    file.close()

#at this point all text files have been read
print("Amount of Room Types: ")
print(len(allObjectsByRoomType))

#now create list of all objects from every room type, no overlap
globalObjectsList = []

for i in range(0, len(allObjectsByRoomType)): #go through each list of objects
    for o in allObjectsByRoomType[i]: #for all objects in allObjectsByRoomType at index i (room type)
        if o not in globalObjectsList: #if object not in globalObjectsList
            globalObjectsList.append(o) #add object to globalObjectsList
globalObjectsList.sort() #sort for organization purposes

#print("All Objects")
#print(globalObjectsList)
#print("globalObjectsList Size: ")
#print(len(globalObjectsList))

generalizedRooms = [] #we now want to recreate each of the rooms according to globalObjectsList

#print("TESTS:")
#print(allRoomsByRoomType[0]) #list of rooms for a certain roomtype
#print(allRoomsByRoomType[0][0]) #specific room, list of 0s/1s
#print(allRoomsByRoomType[0][0][2]) #0 or 1
#print(allObjectsByRoomType[0][0])
#print("index")
#print(globalObjectsList.index(allObjectsByRoomType[0][67]))

for i in range(0, len(allRoomsByRoomType)): #for each roomtype
    for x in range(0, len(allRoomsByRoomType[i])): #for each room in specific roomtype
        revisedRoom = [0] * len(globalObjectsList) #create new empty room
        #now we have a list of 0s, we now need to change present objects to 1
        for y in range(0, len(allRoomsByRoomType[i][x])): #y iterates through specific room, should be 0s and 1s
            curObjectIndex = globalObjectsList.index(allObjectsByRoomType[i][y]) #get object at current position of roomtype and find its index in globalObjectsList
            if allRoomsByRoomType[i][x][y] == 1: #if object is present in current room
                revisedRoom[curObjectIndex] == 1 #set object in revisedRoom to 1
        generalizedRooms.append(revisedRoom) #add revisedRoom to generalizedRooms

#write generalized rooms to file GeneralizedRooms.txt
file = open("GeneralizedRooms.txt","w")
#write objects first
for i in range(0, len(globalObjectsList) - 1):
    file.write("\"")
    file.write(globalObjectsList[i])
    file.write("\"")
    file.write(",")
file.write("\"")
file.write(globalObjectsList[len(globalObjectsList)-1])
file.write("\"")
file.write("\n")

#next write generalized rooms
for x in range(0, len(generalizedRooms)):
    for y in range(0, len(generalizedRooms[x]) - 1):
        temp = str(generalizedRooms[x][y]) + ","
        file.write(temp)
    file.write(str(generalizedRooms[x][y+1]))
    file.write("\n")

file.close()