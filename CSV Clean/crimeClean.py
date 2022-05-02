import csv

file1 = open("./DataSet/Crime.csv",'r')
fh = csv.reader(file1)

data = list(fh)

file1.close()

countries = {}

for line in data[1:]:
    countries[line[0]] = {}
 
for line in data[1:]:
    if float(line[2]) <= 10.0 and float(line[2]) > 0.0 :
        countries[line[0]][line[1]] = line[2]

final = []

for country,dict in countries.items():
    i = 2016
    for year,index in dict.items():
        line = [country,i,index]
        i +=1

        final.append(line)


print(final)

 
file2 = open("./DataSet/Crime1.csv",'w')
fh = csv.writer(file2)

fh.writerow(["Country","Year","Score"])

for line in final:
    fh.writerow(line)

file2.close()
