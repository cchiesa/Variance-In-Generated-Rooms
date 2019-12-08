# Cluster All Rooms from Fisher
import numpy as np 
import pandas as pd 
import os
import matplotlib.pyplot as plt
import numpy as np


from kmodes.kmodes import KModes
df = pd.read_csv('GenRooms.csv')
# make data frame
roomType = df['RoomType']

del df['RoomType']
rows = df.sample(frac = .05)
data = rows
var_names = df.columns.values
print(data)
km = KModes(n_clusters=4, init='Huang', n_init=5, verbose=1)

clusters = km.fit_predict(data)

# Print the cluster centroids
print(km.cluster_centroids_)

file = open("outfile.txt","w") 

for i in km.cluster_centroids_:
    file.write(i)
file.close()
