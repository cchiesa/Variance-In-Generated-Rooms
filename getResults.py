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
      # return count

    # return avg of 'distance'
    # returns float
    return sum/count
    # return count


conn = sqlite3.connect('websiteDatabase.db')
# get lsit of all images
c = conn.cursor()
# get firstIMages
# bathrooms
bathrooms = []
for row in c.execute("SELECT DISTINCT firstImage from answer WHERE firstImage LIKE '%Bathroom%'"):
   # print(row)
    bathrooms.append(''.join(row[0]))

for row in c.execute("SELECT DISTINCT secondImage from answer WHERE secondImage LIKE '%Bathroom%'"):
    # print(row)
    bathrooms.append(''.join(row[0]))

bathrooms = list(dict.fromkeys(bathrooms))
print(bathrooms)

# livingrooms
livingrooms = []

for row in c.execute("SELECT DISTINCT firstImage from answer WHERE firstImage LIKE '%LivingRoom%'"):
    # print(row)
    livingrooms.append(''.join(row[0]))

for row in c.execute("SELECT DISTINCT secondImage from answer WHERE secondImage LIKE '%LivingRoom%'"):
    # print(row)
    livingrooms.append(''.join(row[0]))

livingrooms = list(dict.fromkeys(livingrooms))

# bedrooms
bedrooms = []
for row in c.execute("SELECT DISTINCT firstImage from answer WHERE firstImage LIKE '%Bedroom%'"):
    # print(row)
    bedrooms.append(''.join(row[0]))

for row in c.execute("SELECT DISTINCT secondImage from answer WHERE secondImage LIKE '%Bedroom%'"):
    # print(row)
    bedrooms.append(''.join(row[0]))

bedrooms = list(dict.fromkeys(bedrooms))
