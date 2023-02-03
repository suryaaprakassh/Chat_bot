import csv
import yaml
with open("mental2.csv","r") as cc:
    csv_reader=csv.reader(cc)
    data=[]
    for i in csv_reader:
        data.append(i)
with open("test.txt","w") as ww:
    for row in data:
        if len(row)<2: 
            continue
        ww.write("- - ")
        ww.write(row[0])
        ww.write("\n")
        ww.write("  - ")
        ww.write(row[1])
        ww.write("\n")

