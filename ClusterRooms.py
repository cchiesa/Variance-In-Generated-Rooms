# Tests Variance of All Rooms
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
data = df
var_names = df.columns.values

km = KModes(n_clusters=4, init='Huang', n_init=5, verbose=1)

clusters = km.fit_predict(data)

# Print the cluster centroids
print(km.cluster_centroids_)
