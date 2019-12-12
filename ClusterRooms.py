# Cluster All Rooms from Fisher
import numpy as np 
import pandas as pd 
import os
import matplotlib.pyplot as plt
import numpy as np
import re
#from pandas import ExcelWriter
#from pandas import ExcelFile

from kmodes.kmodes import KModes
#compares room and center for finding room type
def compare(room, center):
    for i in range(0,len(room)):
        r = np.int64(room[i])
        if(r != center[i]):
            #print(type(room[i]),type(center[i]))
            #print(room[i],center[i])
            return False
    return True

df = pd.read_csv('GenRoomsCSV.csv')
# make data frame
print(df)

file = open("GenRoomsRoomType.txt","r") #open up indexes
roomType = []
while True: #read in roomtypes until end of file
    roomLine = file.readline() #room type in qoutes
    roomLine = roomLine[0 : len(roomLine)-1] #remove '\n' at end of string
    if not roomLine: #end of file
        break
    roomLine = roomLine.replace('"',"") #remove double qoutes from room types
    roomType.append(roomLine)
#print(roomType)
file.close()

#read in rooms for checking the center index later
f = open("GenRoomsSUNCGObjects.txt")
rooms = []
object = f.readline()
while True: #read in rooms until end of file
    roomLine = f.readline() #room ex: 1,1,0,0 ...
    roomLine = roomLine[0 : len(roomLine)-1] #remove '\n' at end of string
    if not roomLine: #end of file
        break
    r = roomLine.split(',') #split 0s and 1s into list
    room = np.array(r)
    rooms.append(room) #add room list to rooms

file.close()

data = df.sample(frac = 0.003)

km = KModes(n_clusters=2, init='random', n_init=1, verbose=1)


clusters = km.fit(data)
print(clusters)

# Print the cluster centroids
#print(km.cluster_centroids_)

file = open("out.txt","w") 
print("CENTERS")
for i in km.cluster_centroids_:
    for j in i:
        #print j, 
        file.write(str(j))  
    print(" ")
    file.write("\n")


print('Final training cost: {}'.format(km.cost_))
print('Training iterations: {}'.format(km.n_iter_))
#print df.loc[354]
indices = []
for center in km.cluster_centroids_:
 #   print "1"
    index = 0
    for room in rooms:
        #print index, " "
        #print(row)
        
        #print("room: ",type(room))
        #print("center: ", type(center))
        if (compare(room,center)):
            print(index)
            indices.append(index)
        index = index + 1
            
#print indices
#print indicies[0]
############add 1 to indices in excel file to find room
f = open("indices.txt","w")
for i in indices:
    f.write(str(i))
    f.write("\n")



