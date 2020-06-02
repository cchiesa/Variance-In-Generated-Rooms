import csv
import sqlite3
import numpy as np
from scipy.cluster.hierarchy import median



#get all comparions of bath-beds
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

bed_baths = []
for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%Bathroom%' and secondImage LIKE '%Bedroom%') or (secondImage LIKE '%Bedroom%'and firstImage LIKE'%Bathroom%') "):
    print(row)
    bed_baths.append(getNum(row[0]))
print(bed_baths)
        



