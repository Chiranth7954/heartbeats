import webbrowser
import json
import urllib2

def findSong(s):
    a = s.replace(" ", "+")
    url = "https://api.spotify.com/v1/search?query=" + a + "&type=track&market=US&offset=0&limit=20"
    data = json.load(urllib2.urlopen(url))

    link = data['tracks']['items'][0]['uri']
    return link
