import pandas as pd
import csv

f_countryCodes = open("../DataSet/countryCodes.csv", "r")
r_countryCodes = csv.reader(f_countryCodes)

countryList = list(r_countryCodes)[1:]

f_countryCodes.close()

countries = {}

countries2 = {}

for item in countryList:
    countries[item[0]] = item[2]

for item in countryList:
    countries2[item[1]] = item[2]

f_education = open("../DataSet/Education.csv", "r")
r_education = csv.reader(f_education)

educationList  = list(r_education)[1:]

educationData = {}

for item in educationList:
    educationData[countries[item[0]]] = {}

for item in educationList:
    educationData[countries[item[0]]][item[1]] = item[2]


f_GDP = open("../DataSet/GDP.csv", "r")
r_GDP = csv.reader(f_GDP)

GDPList = list(r_GDP)[1:]

GDPData = {}

for item in GDPList:
    GDPData[countries[item[0]]] = {}

for item in GDPList:
    GDPData[countries[item[0]]][item[1]] = item[2]

f_crime = open("../DataSet/Crime.csv", "r")
r_crime = csv.reader(f_crime)

crimeList = list(r_crime)[1:]

crimeData = {}

for item in crimeList:
    crimeData[countries[item[0]]] = {}

for item in crimeList:
    crimeData[countries[item[0]]][item[1]] = item[2]

f_dep = open("../DataSet/Depression.csv", "r")
r_dep = csv.reader(f_dep)

depList = list(r_dep)[1:]

depData = {}

for item in depList:
    depData[countries[item[0]]] = {}

for item in depList:
    depData[countries[item[0]]][item[3]] = item[2]

f_music = open("../DataSet/musicData.csv", "r")
r_music = csv.reader(f_music)

musicList = list(r_music)[1:]

musicData = {}


for item in musicList:
    musicData[countries2[item[4]]] = {}


for item in musicList:
    
    c = countries2[item[4]]

    musicData[c][item[3]] = {'top 200': {},
                                   'crime' : 0, 
                                   'depression' : 0, 
                                   'education' : 0, 
                                   'gdp per cap' : 0, 
                                   'avg valence' : 0, 
                                   'top 5': {}
                                   }


for item in musicList:
    c = countries2[item[4]]
    musicData[c][item[3]]['top 200'][item[5]+ ' by ' + item[6]] = float(item[7])


    if int(item[1]) <= 5:
        musicData[c][item[3]]['top 5'][item[5]+ ' by ' + item[6]] = float(item[7])

    
    try:
        musicData[c][item[3]]['crime'] = float(crimeData[c][item[3]])

    except KeyError:
        pass

    try:
        musicData[c][item[3]]['depression'] = float(depData[c][item[3]])
    except KeyError:
        pass

    try:
        musicData[c][item[3]]['education'] = float(educationData[c][item[3]])
    except KeyError:
        pass
    
    try:
        musicData[c][item[3]]['gdp per cap'] = float(GDPData[c][item[3]])
    except KeyError:
        pass
    
for country, countryData in musicData.items():
    for year, yearData in countryData.items():
        total = 0
        for val in yearData['top 200'].values():
            total += val
        yearData['avg valence'] = total / len(yearData['top 200'])


df = pd.DataFrame(columns = ['country',
                             'year', 
                             'crime', 
                             'education',
                             'depression',
                             'gdp per cap', 
                             'avg valence', 
                             'top 1', 'top 2', 'top 3'])

for country, cData in musicData.items():
    for year, yearData in cData.items():
        try:
            df = df.append({'country' : country,
                            'year': int(year),
                            'crime': yearData['crime'], 
                            'education': yearData['education'], 
                            'depression' : yearData['depression'], 
                            'gdp per cap' : yearData['gdp per cap'], 
                            'avg valence': yearData['avg valence'],
                            'top 1': [list(yearData['top 5'].keys())[0],list(yearData['top 5'].values())[0]],
                            'top 2': [list(yearData['top 5'].keys())[1],list(yearData['top 5'].values())[1]],
                            'top 3': [list(yearData['top 5'].keys())[2],list(yearData['top 5'].values())[2]],
                            },
                        ignore_index = True)
        
        except IndexError:
            print(country,year,list(yearData['top 5'].keys()))

store = pd.HDFStore('store.h5')
store['df'] = df

print(df)

'''

Country | Year | Crime | Education | Depression | GDP | Avg Valance | Top 1 | Top 2 | Top 3 | Top 4 | Top 5 |
ae      | 2016 | 123   | 123       | 123        | 12  | 123         | Me    | X     | z     | w     | weqw  |
ae      | 2017 | 123   | 123       | 123        | 12  | 123         | Me    | X     | z     | w     | weqw  |
ae      | 2018 | 123   | 123       | 123        | 12  | 123         | Me    | X     | z     | w     | weqw  |
ae      | 2019 | 123   | 123       | 123        | 12  | 123         | Me    | X     | z     | w     | weqw  |
    .
    .
    .
za      | 2016 | 123   | 123       | 123        | 12  | 123         | Me    | X     | z     | w     | weqw  |
za      | 2017 | 123   | 123       | 123        | 12  | 123         | Me    | X     | z     | w     | weqw  |
za      | 2018 | 123   | 123       | 123        | 12  | 123         | Me    | X     | z     | w     | weqw  |
za      | 2019 | 123   | 123       | 123        | 12  | 123         | Me    | X     | z     | w     | weqw  |

'''


    
