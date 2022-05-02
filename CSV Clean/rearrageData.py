import csv


countryISO = {'ar': 'Argentina', 'au': 'Australia', 'at': 'Austria', 'by': 'Belarus', 'be': 'Belgium', 'bo': 'Bolivia, Plurinational State of', 'br': 'Brazil', 'bg': 'Bulgaria', 'ca': 'Canada', 'cl': 'Chile', 'co': 'Colombia', 'cr': 'Costa Rica', 'cy': 'Cyprus', 'cz': 'Czech Republic', 'dk': 'Denmark', 'do': 'Dominican Republic', 'ec': 'Ecuador', 'eg': 'Egypt', 'sv': 'El Salvador', 'ee': 'Estonia', 'fi': 'Finland', 'fr': 'France', 'de': 'Germany', 'gr': 'Greece', 'gt': 'Guatemala', 'hn': 'Honduras', 'hk': 'Hong Kong', 'hu': 'Hungary', 'is': 'Iceland', 'in': 'India', 'id': 'Indonesia', 'ie': 'Ireland', 'il': 'Israel', 'it': 'Italy', 'jp': 'Japan', 'kz': 'Kazakhstan', 'kr': 'Korea, Republic of', 'lv': 'Latvia', 'lt': 'Lithuania', 'lu': 'Luxembourg', 'my': 'Malaysia', 'mx': 'Mexico', 'ma': 'Morocco', 'nl': 'Netherlands', 'nz': 'New Zealand', 'ni': 'Nicaragua', 'ng': 'Nigeria', 'no': 'Norway', 'pa': 'Panama', 'py': 'Paraguay', 'pe': 'Peru', 'ph': 'Philippines', 'pl': 'Poland', 'pt': 'Portugal', 'ro': 'Romania', 'sa': 'Saudi Arabia', 'sg': 'Singapore', 'sk': 'Slovakia', 'za': 'South Africa', 'es': 'Spain', 'se': 'Sweden', 'ch': 'Switzerland', 'tw': 'Taiwan, Province of China', 'th': 'Thailand', 'tr': 'Turkey', 'ua': 'Ukraine', 'ae': 'United Arab Emirates', 'gb': 'United Kingdom', 'us': 'United States', 'uy': 'Uruguay', 've': 'Venezuela, Bolivarian Republic of', 'vn': 'Viet Nam'}

file1 = open('./DataSet/Depression.csv','r')
fh = csv.reader(file1)
info = list(fh)

header = info[0]
data = info[1:]

final = []

for line in data:
    if line[0] in countryISO.values():
        final.append(line)
file1.close()

file2 = open('./DataSet/Depression1.csv','w')
fh2 = csv.writer(file2)

fh2.writerow(["Country","Rank","Happiness","Year"])
for line in final:
    fh2.writerow(line)

file2.close()