from pymongo import MongoClient

client = MongoClient()
db = client['primer']

cursor = db.songs.find()
for document in cursor:
    print(document)
