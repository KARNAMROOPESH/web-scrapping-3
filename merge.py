import csv
from os import write

first=[]
with open("final.csv","r")as f:
    reader = csv.reader(f)
    for row in reader:
        first.append(row)

second=[]
with open("sorteddata.csv","r")as f:
    reader = csv.reader(f)
    for row in reader:
        second.append(row)

headerone = first[0]
headertwo = second[0]

onedata = first[1:]
twodata = second[1:]

finalheader = headerone+headertwo
finaldata = []

for index,datarow in enumerate(onedata):
    finaldata.append(onedata[index]+twodata[index])


with open("completedata.csv","a+")as f:
    writer = csv.writer(f)
    writer.writerow(finalheader)
    writer.writerows(finaldata)