import csv
import matplotlib.pyplot as plt
import numpy as np

fig, ax1 = plt.subplots()

people = {}
with open('Romania.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0    
    for row in csv_reader:
        if line_count == 0:
            line_count = 1
            continue
        if row[3] in people.keys():
            people[row[3]].append(int(row[6]))
        else:
            people[row[3]] = [int(row[6])]

zone = {' Maramures',' CENTER', ' WEST', ' Bucharest Municipality'}

for key in people.keys():
    if 'REGION' not in key and '-' not in key and key not in zone:
        x=people[key]
        ax1.plot(np.arange(2012,2012+len(x)),x,label=key)        
ax1.legend(loc='upper left', prop={'size': 6})
plt.show()
