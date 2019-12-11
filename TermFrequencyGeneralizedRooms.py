#OLD CODE AS OF 12/11/19, use as reference code

#using GeneralizedRooms.txt, create objects list and rooms list, then use term freqeuncy

objects = [] #all objects
rooms = [] #all rooms

file = open("GeneralizedRooms.txt","r")
objectsLine = file.readline() #read line of objects
objectsLine = objectsLine[0 : len(objectsLine)-1] #remove '\n' at end of string
objects = objectsLine.split(',') #seperate objects by comma
for i in range(0, len(objects)):
    objects[i] = objects[i].replace('"',"") #remove double qoutes from objects
    print(objects[i])
SystemExit()

while True: #read in rooms until end of file
    roomLine = file.readline() #room ex: 1,1,0,0 ...
    roomLine = roomLine[0 : len(roomLine)-1] #remove '\n' at end of string
    if not roomLine: #end of file
        break
    room = roomLine.split(',') #split 0s and 1s into list
    rooms.append(room) #add room list to rooms

file.close()

#at this point we should have objects and room in a generalized form
print(objects)
print(rooms[0])
