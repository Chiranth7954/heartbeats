from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests

client = MongoClient()
db = client['primer']

current_bpm = 80
max_bpm = 201
while current_bpm < max_bpm:
    html_doc = requests.get('https://www.cs.ubc.ca/~Davet/music/bpm/' + str(current_bpm) + '.html').text
    soup = BeautifulSoup(html_doc, "lxml")

    table = soup.find('tbody')
    rows = table.find_all('tr')


    for row in rows:
        all_songs = row.find_all('td')
        trash1, artist, song, time, bpm, year, genre, trash2, trash3 = all_songs
        result = db.songs.insert_one(
            {
                "artist": artist.text,
                "song": song.text,
                "time": time.text,
                "bpm": bpm.text,
                "year": year.text,
                "genre": genre.text
            }
        )

    current_bpm += 1
