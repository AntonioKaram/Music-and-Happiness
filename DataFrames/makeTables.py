import pandas as pd
import csv

#Depression
f_dep = open("../DataSet/Depression.csv", "r")
dep_r = csv.reader(f_dep)
dep_data = list(dep_r)[1:]

df1 = pd.DataFrame(dep_data, columns = ['Country',  'Rank',  'Happiness',  'Year'])

fh = open("../Website/Tables/depTable.html", 'w')
fh.close()
df1.to_html("../Website/Tables/depTable.html")

#Education
f_ed = open("../DataSet/Education.csv", "r")
ed_r = csv.reader(f_ed)
ed_data = list(ed_r)[1:]

df2 = pd.DataFrame(ed_data, columns = ['Country', 'Year', 'Score'])


fh = open("../Website/Tables/edTable.html", 'w')
fh.close()
df2.to_html("../Website/Tables/edTable.html")

#GDP per Cap
f_g = open("../DataSet/GDP.csv", "r")
g_r = csv.reader(f_g)
g_data = list(g_r)[1:]
print(g_data)

df3 = pd.DataFrame(g_data, columns = ['Country', 'Year', 'GDP/CAP'])


fh = open("../Website/Tables/gdpTable.html", 'w')
fh.close()
df3.to_html("../Website/Tables/gdpTable.html") 


#Music Data
f_music = open("../DataSet/musicData.csv", "r")
music_r = csv.reader(f_music)
music_data = list(music_r)[1:]


df4 = pd.DataFrame(music_data, columns = ['index','postion','streams','year','country','title','artist','valence'])


fh = open("../Website/Tables/musicTable.html", 'w')
fh.close()
df4.to_html("../Website/Tables/musicTable.html") 

