import csv
import sqlite3
import numpy as np
from scipy.cluster.hierarchy import median
import statistics


def getAnswer(room1, room2, conn, writer):
    c = conn.cursor()
    #writer.writerow(['room1','room2','number of answers','std dev','average'])
    # find avg answer for room 1 and 2
    count = 0
    sum = 0
    array = []
    for row in c.execute("select answer from Answer where (firstImage=? and secondImage=?) or (secondImage=? and firstImage=?)", (room1, room2, room1, room2)):
        # print(row)
        # 3 is extrDis, 2 diss, 1 sim, 0 extrSimm
        if(row[0] == 'extremelyDissimilar'):
            # print(3)
            array.append(3)
            count += 1
            sum = sum + 3
        elif(row[0] == 'dissimilar'):
            array.append(2)
            # print(2)
            count += 1
            sum = sum + 2
        elif(row[0] == 'similar'):
            array.append(1)
            count += 1
            sum = sum + 1
        elif(row[0] == 'extremelySimilar'):
            array.append(0)
            count += 1
            sum = sum + 0
    #print("TEST sql")
    # print(c.rowcount)
    if(count == 0):
        return -1

    std_dev = statistics.stdev(array)
    writer.writerow([room1, room2, count, std_dev,
                     statistics.variance(array), sum/count])

    return sum/count


# return value for answer
def getNum(answer):
    if(answer == 'extremelyDissimilar'):
        return 3
    elif(answer == 'dissimilar'):
        return 2
    elif(answer == 'similar'):
        return 1
    elif(answer == 'extremelySimilar'):
        return 0


conn = sqlite3.connect('websiteDatabase.db')
c = conn.cursor()
# get all unique images

# get firstIMages
firsts = []
seconds = []
for row in c.execute("select distinct firstImage from Answer"):
    firsts.append(row)
    # print(row)
# get second
for row in c.execute("select distinct secondImage from Answer"):
    seconds.append(row)

temp = firsts + seconds
# print(temp)
temp = list(dict.fromkeys(temp))
# print(temp)

j = 0
imgs = []
for i in temp:
    j += 1
   # print(j)
    imgs.append(''.join(i))

# print(len(imgs))


'''
imgs = []
for row in c.execute("SELECT DISTINCT firstImage,secondImage from answer WHERE (firstImage LIKE '%room1.%' OR firstImage LIKE '%room2.%'OR firstImage LIKE '%room3.%'OR firstImage LIKE '%room4.%'OR firstImage LIKE '%room5.%') AND (secondImage LIKE '%room1.%' OR secondImage LIKE '%room2.%' OR secondImage LIKE '%room3.%' OR secondImage LIKE '%room4.%' OR secondImage LIKE '%room5.%')"):
    print(row)
    imgs.append(''.join(row[0]))
    imgs.append(''.join(row[1]))

# print(temp)
imgs = list(dict.fromkeys(imgs))
print(imgs)'''


# print(temp)
# print(len(imgs))
with open('pairResults.csv', mode='w', newline='') as file:

    writer = csv.writer(file)
    writer.writerow(
        ['room1', 'room2', 'number of answers', 'std dev', 'variance', 'average'])
    for i in imgs:
        for j in imgs:
            getAnswer(i, j, conn, writer)
