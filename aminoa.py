import csv
import numpy as np
from collections import Counter
from Bio import SeqIO
import os
data = []


header = ["A","C","D", "E", "F","G", "H","I","K","L", "M","N","P","Q","R","S","T","V","W","Y"]
'''with open('AAC.csv', 'a+', newline = '') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()'''

with open('Rnewdata.csv', mode='r', newline='') as csvreader:
    reader = csv.reader(csvreader)
    for rows,row in enumerate(reader,1):
        data1 = list(str(row))  # Convert into string and then to list (this breaks string into characters)
        #list1 = []
        #data = []
        for symbol in header:
            ctr = 0
            for sym in data1:
                if sym == symbol:
                    ctr += 1
            data.append(float(ctr) / len(data1))
    ak = np.asarray(data)
    ac = ak.reshape(7800, 20)   #For R new data 2017 (GPS-MSP)
    #ac = ak.reshape(3038, 20)  # For K new data 2017 (GPS-MSP)
    #ac = ak.reshape(1480, 20)  # For R-methylation data complete
    #ac = ak.reshape(1745, 20)  # For K-methylation data complete
    #ac = ak.reshape(370, 20)  #For R-methylation data
    #ac=ak.reshape(443, 20)   #For K-methylation data
    #ac=ak.reshape(2906,20)      #For R data 2020
    print(ac)
    print(ac.shape)


    with open('AAC.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
            csvfile.close()

