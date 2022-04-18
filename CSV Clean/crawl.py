import cloudscraper
import pandas as pd

#add ae 2022

countries = ['ae','ar','at','au', 'be', 'bg', 'bo', 'br', 'by', 'ca', 'ch', 'cl', 'co', 'cr', 'cy', 'cz', 'de', 'dk', 'do', 'ec', 'ee', 'eg', 'es', 'fi', 'fr', 'gb', 'gr', 'gt', 'hk', 'hn', 'hu', 'id', 'ie', 'il', 'in', 'is', 'it', 'jp', 'kr', 'kz', 'lt', 'lu', 'lv', 'ma', 'mx', 'my', 'ng', 'ni', 'nl', 'no', 'nz', 'pa', 'pe', 'ph', 'pl', 'pt', 'py', 'ro', 'sa', 'se', 'sg', 'sk', 'sv', 'th', 'tr', 'tw', 'ua', 'us', 'uy', 've', 'vn', 'za']

scraper = cloudscraper.create_scraper()
run = True

day = 1
month = 1

for c in countries:
    for year in range(2016,2023):
        if year == 2016:
            ms = 12
            dy = 28
        else:
            ms = 1
            dy = 1
        for month in range(ms,13):

            if month < 10:
                month = '0' + str(month)
            else:
                month = str(month)

            run = True
            for day in range(dy,32):
                day = day - 1
                newday = day + 7
                
                if day < 10:
                    day = '0' + str(day)
                else:
                    day = str(day)
                
                if newday < 10:
                    newday = '0' + str(newday)
                else:
                    newday = str(newday)

                run = True
                try:
                    run = False
                    r=scraper.get("https://spotifycharts.com/regional/%s/weekly/%s-%s-%s--%s-%s-%s"%(c,year,month,day,year,month,newday))
                    df = pd.read_html(r.text)
                    df = df[0]
                    
                    df.drop('Unnamed: 0', inplace=True, axis=1)
                    df.drop('Unnamed: 2', inplace=True, axis=1)

                    df = df.rename(columns={" ":"Index", 'Unnamed: 1':"Rank"})
                    df["Year"] = year
                    df["Country"] = c


                    nw = df.Track.str.split("by",expand=True)

                    nw = nw.loc[:, :1]

                    df[["Title","Artist"]] = nw

                    df.drop("Track", inplace=True, axis=1)
                    
                    df["Title"] = df.Title.str.replace(',','')
                    df["Title"] = df.Title.str.rstrip()

                    
                    nm = df.Artist.str.split(',',1)
                    
                    for i in range(len(nm)):
                        try:
                            nm[i] = nm[i][0]
                        except TypeError:
                            pass
                    
                    df["Artist"] =  nm

                    

                    df.to_csv('./DATA/%s-%s.csv'%(c,year))

                except ValueError:
                    run = True
                    print(c, year, month, day, "https://spotifycharts.com/regional/%s/weekly/%s-%s-%s--%s-%s-%s"%(c,year,month,day,year,month,newday))
                if not run:
                    print("yes")
                    break
            if not run:
                    print("yes")
                    break
        