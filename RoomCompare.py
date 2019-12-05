import os
for filename in os.listdir("FisherRooms"): #for each set of rooms in FisherRooms
    print(filename)
    file = open("FisherRooms/" + filename,"r") #open up set of rooms
    objectsLine = file.readline() #read line of objects
    max = len(objectsLine)-1
    objectsLine = objectsLine[0 : max]
    objects = objectsLine.split(',')
    
    for i in range(0, len(objects)):
        objects[i] = objects[i].replace('"',"")
            
    
    print(objects)

    file.close()
    break#DELETE only for testing


