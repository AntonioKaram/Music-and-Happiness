import csv

countries = ['ae', 'ar', 'at', 'au', 'be', 'bg', 'bo', 'br', 'by', 'ca', 'ch', 'cl', 'co', 'cr', 'cy', 
'cz', 'de', 'dk', 'do', 'ec', 'ee', 'eg', 'es', 'fi', 'fr', 'gb', 'gr', 'gt', 'hk', 'hn', 'hu', 'id', 
'ie', 'il', 'in', 'is', 'it', 'jp', 'kr', 'kz', 'lt', 'lu', 'lv', 'ma', 'mx', 'my', 'ng', 'ni', 'nl', 
'no', 'nz', 'pa', 'pe', 'ph', 'pl', 'pt', 'py', 'ro', 'sa', 'se', 'sg', 'sk', 'sv', 'th', 'tr', 'tw', 
'ua', 'us', 'uy', 've', 'vn', 'za']


headers = ['index','postion','streams','year','country','title','artist']

with open('musicData.csv', 'w') as data:
    dataWriter = csv.writer(data)
    dataWriter.writerow(headers)
    for c in countries:
        for y in range(2016,2023):
            csvName = '%s-%s.csv'%(c,y)
            try:
                with open(csvName,'r') as f1:
                    f1List = f1.readlines()
                    for l in f1List[1:]:
                        line = l.split(',')
                        dataWriter.writerow(line)
            except FileNotFoundError:
                print(csvName)


                    


        

