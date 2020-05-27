
import sqlite3


def k_means(num_clusters, features):
    #get starting centers randomly
    center = []
    centerPos = []
    for i in range(0,num_clusters):
        centerPos.append(-1)
    for i in range(0,num_clusters):
        while(True):
            rand = random.randint(0,len(features))
            if(rand in centerPos):
                continue
            else:
                break
        center.append(features[rand])
        
    done = False
    while(not done):
        nextCenter = [[] for i in range(0,num_clusters)]
        cluster = [[] for i in range(0,num_clusters)]
        for i in range(0,len(center)):
            cluster[i].append(center[i])
     #  pred = []
        for row in features:
            dist = []   
            for c in center:
                #print(row)
                #dist.append(euclid(row,c))
                #changes to 0-3 ext sim to ext disssim
                dist.append(getAnswer(row,c))
            min = 0
            for i in range(0,len(center)):           
                if dist[i] < dist[min]:
                    min = i
            cluster[min].append(row)
            #print(len(cluster[min]))
        print("getting next center")
        for cl in range(0,num_clusters):
            #print("cluster",x)
            nextCenter[cl] = getCenter(cluster[cl])

        for i in range(0,len(center)):
            if(not(np.array_equal(center[i],nextCenter[i]))):
                center = nextCenter[:]
                #print(center)
                print("new center")
                break
            elif( i == len(center)-1):
                #done
                print("DONE")
                #print(nextCenter)
                return nextCenter
                done = True




def getAnswer(room1, room2, conn):
    
    c = conn.cursor()
    #find avg answer for room 1 and 2
    count = 0
    sum = 0
    for row in c.execute("select answer from Answer where (firstImage=? and secondImage=?) or (secondImage=? and firstImage=?)",(room1,room2,room1,room2)):
        print(row)
        # 3 is extrDis, 2 diss, 1 sim, 0 extrSimm
        if(row[0] == 'extremelyDissimilar'):
            #print(3)
            count += 1
            sum = sum + 3
        elif(row[0] == 'dissimilar'):
            #print(2)
            count += 1
            sum = sum + 2
        elif(row[0] == 'similar'):
            count += 1
            sum = sum + 1
        elif(row[0] == 'extremelySimilar'):
            count += 1
            sum = sum + 0
    
    #return avg of 'distance'
    #returns float
    return sum/count


        
    


conn = sqlite3.connect('websiteDatabase.db')
#get lsit of all images
c = conn.cursor()
#get firstIMages
firsts = []
seconds = []
for row in c.execute("select distinct firstImage from Answer"):
    firsts.append(row)
    #print(row)
#get second
for row in c.execute("select distinct firstImage from Answer"):
    seconds.append(row)

imgs = firsts + seconds
imgs = list(dict.fromkeys(imgs))

j = 0
for i in imgs:
    j += 1
    print(j)
    print(i)

test = getAnswer("CustomBathroom1.2580f005.jpg","CustomBathroom2.b78c9823.jpg", conn)
#main

#get list of rooms
#fstI
#for row in conn.cursor.execute("select firstImage from Answer group by firstImage"):

conn.close()
    
# cluster = MiniBatchKMeans(n_clusters = num_clusters[i])
#               cluster_labels = cluster.fit_predict(data)
#                silhouette_avg = metrics.silhouette_score(data,cluster_labels) #May want to do sampling here