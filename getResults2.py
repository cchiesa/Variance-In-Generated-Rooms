import csv
import sqlite3
import numpy as np
from scipy.cluster.hierarchy import median



#return value for answer
def getNum(answer):
    if(answer == 'extremelyDissimilar'):
        return 3  
    elif(answer == 'dissimilar'):
        return 2
    elif(answer== 'similar'):
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


