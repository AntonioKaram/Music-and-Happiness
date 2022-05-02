import csv

f = open("../DataSet/countryCodes2.csv", "r")
fh = csv.reader(f)

data = list(fh)

f2 = open("../DataSet/countryCodes3.csv", "w")
fh2 = csv.writer(f2)

fh2.writerow(['Name','Code'])


for item in data[1:]:
    row = [item[0],item[2]]

    fh2.writerow(row)