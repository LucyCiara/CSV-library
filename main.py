import csv
with open("test.csv") as inputFile:
    dataDictList = list(csv.DictReader(inputFile))

for row in dataDictList:
    print(row["Goblin modes"])