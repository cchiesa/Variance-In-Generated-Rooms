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



###########anova one way####################
import scipy.stats as stats

#bed - baths to bed - bed

#convert to ints
bath_bed = list(map(int,list(answers['Bathroom_Bedroom']['answer'])))
bath_bed = np.array(bath_bed)
print(bath_bed)

bed_bed = list(map(int,list(answers['Bedroom_Bedroom']['answer'])))
bed_bed = np.array(bed_bed)
print(bed_bed)

s = stats.f_oneway(bath_bed,bed_bed)
print(s.pvalue)
#bed-bath to bath-bath
#s1 = stats.f_oneway(bed_bath,bath_bath)
#print(s1.pvalue)