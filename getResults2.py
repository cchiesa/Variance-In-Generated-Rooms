import csv
import sqlite3
import numpy as np
from scipy.cluster.hierarchy import median



#get all comparions of bath-beds


conn = sqlite3.connect('websiteDatabase.db')

c = conn.cursor()

for row in c.execute("SELECT  Answer from answer WHERE (firstImage LIKE '%Bathroom%' and secondImage LIKE '%Bedroom%') or (secondImage LIKE '%Bedroom%'and firstImage LIKE'%Bathroom%') "):
    print(row)



