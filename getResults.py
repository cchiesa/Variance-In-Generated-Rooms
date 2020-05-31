import csv
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
customRooms = []
for row in c.execute("SELECT DISTINCT firstImage from answer WHERE firstImage LIKE '%Custom%'"):
   # print(row)
    customRooms.append(''.join(row[0]))

for row in c.execute("SELECT DISTINCT secondImage from answer WHERE secondImage LIKE '%Custom%'"):
    # print(row)
    customRooms.append(''.join(row[0]))

customRooms = list(dict.fromkeys(customRooms))
print(customRooms)
print(len(customRooms))

kermaniRooms = []
for row in c.execute("SELECT DISTINCT firstImage from answer WHERE firstImage LIKE '%Kermani%'"):
   # print(row)
    kermaniRooms.append(''.join(row[0]))

for row in c.execute("SELECT DISTINCT secondImage from answer WHERE secondImage LIKE '%Kermani%'"):
    # print(row)
    kermaniRooms.append(''.join(row[0]))

kermaniRooms = list(dict.fromkeys(kermaniRooms))
print(kermaniRooms)
print(len(kermaniRooms))

sceneSeerRooms = []
for row in c.execute("SELECT DISTINCT firstImage from answer WHERE firstImage LIKE '%SceneSeer%'"):
   # print(row)
    sceneSeerRooms.append(''.join(row[0]))

for row in c.execute("SELECT DISTINCT secondImage from answer WHERE secondImage LIKE '%SceneSeer%'"):
    # print(row)
    sceneSeerRooms.append(''.join(row[0]))

sceneSeerRooms = list(dict.fromkeys(sceneSeerRooms))
print(sceneSeerRooms)
print(len(sceneSeerRooms))

row_list = []
# bedrooms to baths
bedTitle = bedrooms.copy()
bedTitle.insert(0, '')
row_list.append(bedTitle)
for bathroom in bathrooms:
    temp = []
    temp.append(bathroom)
    for bedroom in bedrooms:
        temp.append(getAnswer(bedroom, bathroom, conn))
    row_list.append(temp)
# print(row_list)

row_list.append([""])
row_list.append([""])

# bathrooms to bathroooms
bathTitle = bathrooms.copy()
bathTitle.insert(0, '')
row_list.append(bathTitle)
for bathroom in bathrooms:
    temp = []
    temp.append(bathroom)
    for bathroom1 in bathrooms:
        temp.append(getAnswer(bathroom1, bathroom, conn))
    row_list.append(temp)
# print(row_list)

row_list.append([""])
row_list.append([""])

# bath to living
lTitle = livingrooms.copy()
lTitle.insert(0, '')
row_list.append(lTitle)
for bathroom in bathrooms:
    temp = []
    temp.append(bathroom)
    for lroom in livingrooms:
        temp.append(getAnswer(lroom, bathroom, conn))
    row_list.append(temp)
# print(row_list)

row_list.append([""])
row_list.append([""])

#bed - bed


row_list.append(bedTitle)
for bedroom in bedrooms:
    temp = []
    temp.append(bathroom)
    for bedroom1 in bedrooms:
        temp.append(getAnswer(bedroom, bedroom1, conn))
    row_list.append(temp)
# print(row_list)
row_list.append([""])
row_list.append([""])


# living-bed


row_list.append(bedTitle)
for lroom in livingrooms:
    temp = []
    temp.append(lroom)
    for bedroom in bedrooms:
        temp.append(getAnswer(bedroom, lroom, conn))
    row_list.append(temp)
# print(row_list)


row_list.append([""])
row_list.append([""])

#living - living

row_list.append(lTitle)
for lroom in livingrooms:
    temp = []
    temp.append(lroom)
    for livingroom in livingrooms:
        temp.append(getAnswer(livingroom, lroom, conn))
    row_list.append(temp)
# print(row_list)


row_list.append([""])
row_list.append([""])


# Below are the comparisons by generator
customRoomsColumnTitles = customRooms.copy()
customRoomsColumnTitles.insert(0, '')
kermaniRoomsColumnTitles = kermaniRooms.copy()
kermaniRoomsColumnTitles.insert(0, '')
sceneSeerRoomsColumnTitles = sceneSeerRooms.copy()
sceneSeerRoomsColumnTitles.insert(0, '')

# custom to custom
row_list.append(customRoomsColumnTitles)
for customRoom in customRooms:
    temp = []
    temp.append(customRoom)
    for customRoom2 in customRooms:
        temp.append(getAnswer(customRoom, customRoom2, conn))
    row_list.append(temp)
# print(row_list)

row_list.append([""])
row_list.append([""])

# kermani to kermani
row_list.append(kermaniRoomsColumnTitles)
for kermaniRoom in kermaniRooms:
    temp = []
    temp.append(kermaniRoom)
    for kermaniRoom2 in kermaniRooms:
        temp.append(getAnswer(kermaniRoom, kermaniRoom2, conn))
    row_list.append(temp)
# print(row_list)

row_list.append([""])
row_list.append([""])

# sceneseer to sceneseer
row_list.append(sceneSeerRoomsColumnTitles)
for sceneSeerRoom in sceneSeerRooms:
    temp = []
    temp.append(sceneSeerRoom)
    for sceneSeerRoom2 in sceneSeerRooms:
        temp.append(getAnswer(sceneSeerRoom, sceneSeerRoom2, conn))
    row_list.append(temp)
# print(row_list)

row_list.append([""])
row_list.append([""])

# custom to kermani
row_list.append(customRoomsColumnTitles)
for kermaniRoom in kermaniRooms:
    temp = []
    temp.append(kermaniRoom)
    for customRoom in customRooms:
        temp.append(getAnswer(customRoom, kermaniRoom, conn))
    row_list.append(temp)
# print(row_list)

row_list.append([""])
row_list.append([""])

# kermani to sceneseer
row_list.append(kermaniRoomsColumnTitles)
for sceneSeerRoom in sceneSeerRooms:
    temp = []
    temp.append(sceneSeerRoom)
    for kermaniRoom in kermaniRooms:
        temp.append(getAnswer(kermaniRoom, sceneSeerRoom, conn))
    row_list.append(temp)
# print(row_list)

row_list.append([""])
row_list.append([""])

# sceneseer to custom
row_list.append(sceneSeerRoomsColumnTitles)
for customRoom in customRooms:
    temp = []
    temp.append(customRoom)
    for sceneSeerRoom in sceneSeerRooms:
        temp.append(getAnswer(sceneSeerRoom, customRoom, conn))
    row_list.append(temp)
# print(row_list)

row_list.append([""])
row_list.append([""])

with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)
