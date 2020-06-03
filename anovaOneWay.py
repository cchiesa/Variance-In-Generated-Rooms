###########anova one way####################
import scipy.stats as stats
import pandas as pd
import numpy as np
import csv
#df = pandas.read_csv('newResults.csv')
#print(df)

def csv_record_reader(csv_reader):
    """ Read a csv reader iterator until a blank line is found. """
    prev_row_blank = True
    for row in csv_reader:
        #print(row)
        row_blank = (row[0] == '')
        if not row_blank:
            yield row
            prev_row_blank = False
        elif not prev_row_blank:
            return

answers = {}
with open('newResults.csv') as file:

    ratings_reader = csv.reader(file)
    while True:
        category_row = list(csv_record_reader(ratings_reader))
        if len(category_row) == 0:
            break
        category = category_row[0][0]

        # get the generator for the data section
        data_generator = csv_record_reader(ratings_reader)
        print(category)
        # first row of data is the column names
        columns = next(data_generator)

        # use the rest of the data to build a data frame
        answers[category] = pd.DataFrame(data_generator, columns=columns)


#make all the arrays
arrays = [] #contains all the arrays in order
names = ["Bath-Bed","Bath-Bath","Bath-Living","Bed-Bed","Living-Bed","Living-Living","Kermani-Scene","Custom-Scene","Kermani-Custom","Kermani-Kermani",\
    "Scene-Scene","Custom-Custom"]

#convert to ints
bath_bed = list(map(int,list(answers['Bathroom_Bedroom']['answer'])))
bath_bed = np.array(bath_bed)
print(bath_bed)
arrays.append(bath_bed)
#bath-bath
bath_bath = list(map(int,list(answers['Bathroom_Bathroom']['answer'])))
bath_bath = np.array(bath_bath)
arrays.append(bath_bath)
#bed-bed
bed_bed = list(map(int,list(answers['Bedroom_Bedroom']['answer'])))
bed_bed = np.array(bed_bed)
print(bed_bed)
arrays.append(bed_bed)
#bath-living
bath_living = list(map(int,list(answers['Bathroom_LivingRoom']['answer'])))
bath_living = np.array(bath_living)
arrays.append(bath_living)
#living-bed
living_bed = list(map(int,list(answers['LivingRoom_Bedroom']['answer'])))
living_bed = np.array(living_bed)
arrays.append(living_bed)

#living-living
living_living = list(map(int,list(answers['LivingRoom_LivingRoom']['answer'])))
living_living  = np.array(living_living)
arrays.append(living_living)
#gen - gen
#kerm-scene
kermani_sceneseer = list(map(int,list(answers['Kermani_SceneSeer']['answer'])))
kermani_sceneseer = np.array(kermani_sceneseer)
arrays.append(kermani_sceneseer)
#custom-scene
sceneseer_custom = list(map(int,list(answers['Custom_SceneSeer']['answer'])))
sceneseer_custom = np.array(sceneseer_custom)
arrays.append(sceneseer_custom)
#kerm-custom
kermani_custom = list(map(int,list(answers['Kermani_Custom']['answer'])))
kermani_custom = np.array(kermani_custom)
arrays.append(kermani_custom)
#kerm-kerm
kermani_kermani = list(map(int,list(answers['Kermani_Kermani']['answer'])))
kermani_kermani = np.array(kermani_kermani)
arrays.append(kermani_kermani)
#scne-scene
sceneseer_sceneseer = list(map(int,list(answers['SceneSeer_SceneSeer']['answer'])))
sceneseer_sceneseer = np.array(sceneseer_sceneseer)
arrays.append(sceneseer_sceneseer)
#cust-cust
custom_custom = list(map(int,list(answers['Custom_Custom']['answer'])))
custom_custom = np.array(custom_custom)
arrays.append(custom_custom)


###########anova one way####################
import scipy.stats as stats

with open('anovaResults.txt', mode='w') as f:

    
    '''s = stats.f_oneway(bath_bed,bed_bed)
    print(s.pvalue)
    f.write("bath_bed to bed_bed: " + str(s.pvalue))

    s1 = stats.f_oneway(bath_bed,bath_bath)
    f.write("bath_bed to bath_bath: " + str(s1.pvalue))

    s2 = stats.f_oneway(bath_living,bath_bath)
    f.write("bath_living to bath_bath: "+ str(s2.pvalue))

    s3 = stats.f_oneway(bath_living,living_living)
    f.write("bath_living to living_living: "+ str(s3.pvalue))

    s4 = stats.f_oneway(living_bed,living_living)
    '''

    for i in range(0,6):
        for j in range(0,6):
            st = stats.f_oneway(arrays[i],arrays[j])
            f.write(names[i] + " to " + names[j] + " pvalue: " + str(st.pvalue) +"\n")
        f.write("\n")

    for i in range(6,12):
        for j in range(6,12):
            s = stats.f_oneway(arrays[i],arrays[j])
            f.write(names[i] + " to " + names[j] + " pvalue: " + str(s.pvalue) +"\n")
        f.write("\n")