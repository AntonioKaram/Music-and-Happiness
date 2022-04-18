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
i = 1
for line in data[1:5]:
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
        final.append(line)

    except IndexError:
        print(query,"Not Found")

    i += 1

file2 = open("./DataSet/musicData2.csv","w")
fh = csv.writer(file2)

for line in final:
    fh.writerow(line)

