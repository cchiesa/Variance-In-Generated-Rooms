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
data = df.sample(frac = .05)


var_names = df.columns.values
print(data)
km = KModes(n_clusters=3, init='random', n_init=2, verbose=1)


clusters = km.fit(data)
print(clusters)

# Print the cluster centroids
#print(km.cluster_centroids_)

file = open("outfile.txt","w") 
print("CENTERS")
for i in km.cluster_centroids_:
    for j in i:
        #print j, 
        file.write(str(j))  
    print(" ")
    file.write("\n")


print('Final training cost: {}'.format(km.cost_))
print('Training iterations: {}'.format(km.n_iter_))
#print df.loc[354]
indices = []
for center in km.cluster_centroids_:
 #   print "1"
    for index, row in df.iterrows():
        #print index, " "
        if np.array_equal( np.array(center) , np.array(row) ):
            indices.append(index)   
            print index 
            break
print indices
#print indicies[0]
f = open('indices.txt')
for i in indices:
    f.write(str(i))
    f.write("\n")

