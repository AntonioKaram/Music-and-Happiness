import csv

file1 = open("./DataSet/GDP.csv", encoding="utf8", errors='ignore')
fh = csv.reader(file1)


info = list(fh)
header = info[0]
data = info[1:]
file1.close()
final = []

for dt in data:
    d = dt[:2]
    d.append(float( (dt[2]).replace(',','') ))
    final.append(d)

file2 = open("./DataSet/GDP2.csv", 'w')
fh = csv.writer(file2)

fh.writerow(["Country","Year","Score"])
for line in final:
    print(line)
    fh.writerow(line)
file2.close()