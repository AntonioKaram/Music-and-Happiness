import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f664dd2901c94f7098a37aff415b1f83",
                                                           client_secret="02f450a40d674ebf983882ee5cebcbde"))

file1 = open("./DataSet/musicData.csv", 'r')

fh = csv.reader(file1)
data = list(fh)

file1.close()

header = data[0]
header.append('valence')

final = []
final.append(header)
i = 22328
count = 0

file2 = open("./DataSet/musicData2.csv","a")
fh2 = csv.writer(file2)
#fh2.writerow(header)

for line in data[22328:]:
    print(i)

    song = line[5]
    art = line[6]
    query = song+' '+art

    try:
        t = sp.search(q=query,limit = 2, type = "track")
        tid = t['tracks']['items'][0]["uri"]
        info = sp.audio_features(tid)
        valence = info[0]['valence']

        line.append(valence)
        
        fh2.writerow(line)

    except (IndexError, TypeError, spotipy.exceptions.SpotifyException):
        print(query,"Not Found")
        count += 1

    i += 1

file2.close()
print("Number not found:",count)