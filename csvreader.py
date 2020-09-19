import csv

with open('testfile.csv','r',encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    i=0

    for line in csv_reader:
        print(i,"  >",line[0])
        i=i+1

