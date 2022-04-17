import csv
import math
with open('2022.csv', 'r') as f1: 
  f1reader = csv.reader(f1)
  country = []
  happiness= []
  rank = []
  for index, line in enumerate(f1reader):
    if index !=0:
      country.append(line[1])
      rank.append(line[0])
      happiness.append(line[2].replace(',','.'))
  
f1.close()

print(country)
print(rank)
print(happiness)

headers = ['Country', 'Rank', "Happiness", 'Year']
with open('depression.csv','a') as f2:
    f2writer = csv.writer(f2)
    for i in range(len(country)):
        line = [country[i],rank[i],happiness[i],2022]
        f2writer.writerow(line)



