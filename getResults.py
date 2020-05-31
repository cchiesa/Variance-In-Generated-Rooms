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
firsts = []
seconds = []
#for row in c.execute("select distinct firstImage from Answer"):
   # firsts.append(row)
    # print(row)
# get second

imgs = []

for row in c.execute("select distinct secondImage from Answer"):
    #seconds.append(row)







# print(temp)
imgs = list(dict.fromkeys(imgs))
print(imgs)


# print(temp)
print(len(imgs))
# create distance metric

distMatrix = []

for img in imgs:
    # compare to all others images
    listDist = []
    for img2 in imgs:
        dist = getAnswer(img, img2, conn)
        listDist.append(dist)
    # append to distMatrix
    distMatrix.append(listDist)