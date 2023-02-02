import csv
f = open("train.txt", "w")
with open('mental.csv','r') as fa:
    reader=csv.reader(fa)
    for row  in reader:
        f.writelines(row[1])
        f.writelines(row[2])
f.close()