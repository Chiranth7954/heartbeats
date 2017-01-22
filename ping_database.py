from pymongo import MongoClient

client = MongoClient("mongodb://0.tcp.ngrok.io:16289/songs")
db = client['primer']

cursor = db.songs.find()
for document in cursor:
    print(document)
