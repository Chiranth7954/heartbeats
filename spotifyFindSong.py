import webbrowser
def findSong(s):
    a = s.replace(" ", "+")
    url = "https://api.spotify.com/v1/search?query=" + a + "&type=track&market=US&offset=0&limit=20"
    webbrowser.open_new(url)
#findSong("Money Pink Floyd")
