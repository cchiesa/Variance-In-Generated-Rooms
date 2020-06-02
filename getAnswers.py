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
    #bed - bath
    bed_bath = getList('%Bathroom%','%Bedroom%',writer)
    #bath - bath
    bath_bath = getList('%Bathroom%','%Bathroom%',writer)
    #bath-living
    bath_living = getList('%Bathroom%','%LivingRoom%',writer)
    #bed-bed
    bed_bed = getList('%Bedroom%','%Bedroom%',writer)
    #living-bed
    living_bed = getList('%LivingRoom%','%Bedroom%',writer)
    #living-lving
    living_living = getList('%LivingRoom%','%LivingRoom%',writer)

    #generator-generator

    kermani_sceneseer = getList('%Kermani%', '%SceneSeer%', writer)

    sceneseer_custom = getList('%Custom%', '%SceneSeer%', writer)

    custom_kermani = getList('%Kermani%', '%Custom%', writer)

    kermani_kermani = getList('%Kermani%', '%Kermani%', writer)

    sceneseer_sceneseer = getList('%SceneSeer%', '%SceneSeer%', writer)

    custom_custom = getList('%Custom%', '%Custom%', writer)


###########anova one way####################
import scipy.stats as stats

#bed - baths to bed - bed
s = stats.f_oneway(bed_bath,bed_bed)
print(s.pvalue)
#bed-bath to bath-bath
s1 = stats.f_oneway(bed_bath,bath_bath)
print(s1.pvalue)

