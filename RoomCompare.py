import os
allObjectsByRoomType = [] #list of list of objects by room type
allRoomsByRoomType = [] #list of list of rooms by room type
for filename in os.listdir("FisherRooms"): #for each set of rooms in FisherRooms
    print(filename)
    file = open("FisherRooms/" + filename,"r") #open up set of rooms
    objectsLine = file.readline() #read line of objects
    objectsLine = objectsLine[0 : len(objectsLine)-1] #remove '\n' at end of string
    objects = objectsLine.split(',') #seperate objects by comma
    
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
    allRoomsByRoomType.append(rooms) #add list of rooms to overall list of rooms, needed for later
    file.close()
    #break #DELETE only for testing, only does first file

print("Amount of Room Types: ")
print(len(allObjectsByRoomType))


