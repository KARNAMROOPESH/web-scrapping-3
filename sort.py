import csv

data = []
with open("newdata.csv","r")as f:
    reader=csv.reader(f)
    for row in reader:
        data.append(row)
    
headers = data[0]
planetdata = data[1:]

for datapoint in planetdata:
    datapoint[0]=datapoint[0].lower()

planetdata.sort(key = lambda  planetdata : planetdata[0])

with open("sorteddata.csv" , "a+")as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planetdata)


