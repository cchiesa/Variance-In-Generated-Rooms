file = open("GeneralizedRoomsRoomTypeIndex.txt","r") #open up room types

rooms = []
while True: #read in roomtypes until end of file
    roomLine = file.readline() #room type in qoutes
    roomLine = roomLine[0 : len(roomLine)-1] #remove '\n' at end of string
    if not roomLine: #end of file
        break
    roomLine = roomLine.replace('"',"") #remove double qoutes from room types
    rooms.append(roomLine)

file.close()

file = open("indices.txt","r") #open up indexes

indexes = []
while True: #read in roomtypes until end of file
    indexLine = file.readline() #room type in qoutes
    indexLine = indexLine[0 : len(roomLine)-1] #remove '\n' at end of string
    if not indexLine: #end of file
        break
    indexes.append(indexLine)

file.close()

file = open("FisherResultCenters.txt","w")
for i in range(0, len(indexes)):
    file.write(rooms[indexes[i]])
    file.write("\n")
file.close()