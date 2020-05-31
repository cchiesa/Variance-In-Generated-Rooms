import sqlite3
import numpy as np


def getAnswer(room1, room2, conn):
    c = conn.cursor()
    # find avg answer for room 1 and 2
    count = 0
    sum = 0
    for row in c.execute("select answer from Answer where (firstImage=? and secondImage=?) or (secondImage=? and firstImage=?)", (room1, room2, room1, room2)):
        # print(row)
        # 3 is extrDis, 2 diss, 1 sim, 0 extrSimm
        if(row[0] == 'extremelyDissimilar'):
            # print(3)
            count += 1
            sum = sum + 3
        elif(row[0] == 'dissimilar'):
            # print(2)
            count += 1
            sum = sum + 2
        elif(row[0] == 'similar'):
            count += 1
            sum = sum + 1
        elif(row[0] == 'extremelySimilar'):
            count += 1
            sum = sum + 0
    # print("TEST sql")
    # print(c.rowcount)
    if(count == 0):
         return -1
       #return count

    # return avg of 'distance'
    # returns float
    return sum/count
    #return count


conn = sqlite3.connect('websiteDatabase.db')
# get lsit of all images
c = conn.cursor()
# get firstIMages

bathrooms = []
for row in c.execute("SELECT DISTINCT firstImage,secondImage from answer WHERE firstImage LIKE '%Bathroom%'"):
    print(row)
    bathrooms.append(''.join(row[0]))
    bathrooms.append(''.join(row[1]))

customRooms = []
for row in c.execute("SELECT DISTINCT firstImage,secondImage from answer WHERE firstImage LIKE '%Custom%'"):
    print(row)
    customRooms.append(''.join(row[0]))
    customRooms.append(''.join(row[1]))

kermaniRooms = []
for row in c.execute("SELECT DISTINCT firstImage,secondImage from answer WHERE firstImage LIKE '%Kermani%'"):
    print(row)
    kermaniRooms.append(''.join(row[0]))
    kermaniRooms.append(''.join(row[1]))

sceneSeerRooms = []
for row in c.execute("SELECT DISTINCT firstImage,secondImage from answer WHERE firstImage LIKE '%SceneSeer%'"):
    print(row)
    sceneSeerRooms.append(''.join(row[0]))
    sceneSeerRooms.append(''.join(row[1]))

print(bathrooms)
