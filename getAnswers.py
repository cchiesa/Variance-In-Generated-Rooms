import csv
import sqlite3
import numpy as np
from scipy.cluster.hierarchy import median

# get all comparions of bath-beds


#return value for answer
def getNum(answer):
    if(answer == 'extremelyDissimilar'):
        return 3
    elif(answer == 'dissimilar'):
        return 2
    elif(answer == 'similar'):
        return 1
    elif(answer == 'extremelySimilar'):
        return 0


def getList(roomType1,roomType2,writer):
    conn = sqlite3.connect('websiteDatabase.db')
    c = conn.cursor()
    rows = []
    room1_room2 = []
    for row in c.execute("SELECT  firstImage,secondImage,Answer from answer \
         WHERE (firstImage LIKE ? and secondImage LIKE ?) or (firstImage LIKE ? and secondImage LIKE ?) ",(roomType1,roomType2,roomType2,roomType1)):

        #print(row)
        rows.append([row[0],row[1],getNum(row[2])])
        room1_room2.append(getNum(row[2]))
    writer.writerows(rows)
    writer.writerow([""])
    writer.writerow([""])
    
    return room1_room2


with open('newResults.csv', mode='w') as file:
    writer = csv.writer(file)
    bed_bath = getList('%Bathroom%','%Bedroom%',writer)
    #print(bed_bath)
    #print(len(bed_bath))

    