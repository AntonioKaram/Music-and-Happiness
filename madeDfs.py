import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f664dd2901c94f7098a37aff415b1f83",
                                                           client_secret="02f450a40d674ebf983882ee5cebcbde"))

file1 = open("./DataSet/musicData.csv", 'r')

fh = csv.reader(file1)
data = list(fh)
header = data[0]

for line in data[1:2]:
    song = line[5]
    art = line[6]
    query = song+' '+art

    t = sp.search(q=query,limit = 2, type = "track")
    tid = t['tracks']['items'][]
    print()

