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


conn = sqlite3.connect('websiteDatabase.db')

c = conn.cursor()

bed_bath = []
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%Bathroom%' and secondImage LIKE '%Bedroom%') or (firstImage LIKE '%Bedroom%'and secondImage LIKE'%Bathroom%') "):
    #print(row)
    bed_bath.append(getNum(row[0]))

#bath - bath
bath_bath = []
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%Bathroom%' and secondImage LIKE '%Bathroom%')"):
    #print(row)
    bath_bath.append(getNum(row[0]))
#print(bath_bath)     

#bath - living
bath_living = []
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%Bathroom%' and secondImage LIKE '%LivingRoom%') or (firstImage LIKE '%LivingRoom%'and secondImage LIKE'%Bathroom%') "):
    #print(row)
    bath_living.append(getNum(row[0]))
#print(bath_living)

#bed - bed
bed_bed = []
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%Bedroom%' and secondImage LIKE '%Bedroom%') or (firstImage LIKE '%Bedroom%'and secondImage LIKE'%Bedroom%') "):
    #print(row)
    bed_bed.append(getNum(row[0]))
#living - bed
living_bed = []
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%Bedroom%' and secondImage LIKE '%LivingRoom%') or (firstImage LIKE '%LivingRoom%'and secondImage LIKE'%Bedroom%') "):
    #print(row)
    living_bed.append(getNum(row[0]))

#lving - living 
living_living = []
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%LivingRoom%' and secondImage LIKE '%LivingRoom%') or (firstImage LIKE '%LivingRoom%'and secondImage LIKE'%LivingRoom%') "):
    #print(row)
    living_living.append(getNum(row[0]))
bed_baths = []
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%Bathroom%' and secondImage LIKE '%Bedroom%') or (secondImage LIKE '%Bedroom%'and firstImage LIKE'%Bathroom%') "):
    print(row)
    bed_baths.append(getNum(row[0]))
print(bed_baths)

# below are generator comparisons
kermani_sceneseer = []
print("kermani_sceneseer")
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%Kermani%' and secondImage LIKE '%SceneSeer%') or (secondImage LIKE '%Kermani%'and firstImage LIKE'%SceneSeer%') "):
    print(row)
    kermani_sceneseer.append(getNum(row[0]))
print(kermani_sceneseer)

sceneseer_custom = []
print("sceneseer_custom")
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%SceneSeer%' and secondImage LIKE '%Custom%') or (secondImage LIKE '%SceneSeer%'and firstImage LIKE'%Custom%') "):
    print(row)
    sceneseer_custom.append(getNum(row[0]))
print(sceneseer_custom)

custom_kermani = []
print("custom_kermani")
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%Custom%' and secondImage LIKE '%Kermani%') or (secondImage LIKE '%Custom%'and firstImage LIKE'%Kermani%') "):
    print(row)
    custom_kermani.append(getNum(row[0]))
print(custom_kermani)

kermani_kermani = []
print("kermani_kermani")
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%Kermani%' and secondImage LIKE '%Kermani%') "):
    print(row)
    kermani_kermani.append(getNum(row[0]))
print(kermani_kermani)

sceneseer_sceneseer = []
print("sceneseer_sceneseer")
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%SceneSeer%' and secondImage LIKE '%SceneSeer%') "):
    print(row)
    bed_baths.append(getNum(row[0]))
print(bed_baths)

custom_custom = []
print("custom_custom")
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%Custom%' and secondImage LIKE '%Custom%') "):
    print(row)
    custom_custom.append(getNum(row[0]))
print(custom_custom)
