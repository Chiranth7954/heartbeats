import json
import ast
from pymongo import MongoClient
from spotifyFindSong import *

client = MongoClient("mongodb://0.tcp.ngrok.io:16289/songs")
db = client['primer']

with open('../../Downloads/heartbeats.txt', 'r+') as f:
    content = f.read().split("|")


content = [x.strip() for x in content]
user_bpm = int(content[0])
user_genre = content[1].split(', ')
user_workout_length = int(content[2]) * 60   # convert minutes to seconds
user_workout = content[3]

BPM_INCREASE = 5
BPM_DECREASE = -5
song_bpm = 0
current_workout_length = 0
uri_links = []

print(user_workout)

if(user_workout.strip() == "constant"):
    query = {
        'bpm': int(user_bpm),
        'genre': {'$in': user_genre}
    }
    print(query)
    print(user_genre)
    valid_songs = db.songs.find(query)


    for song in valid_songs:
        try:
            uri_link = findSong(song['song'] + " " + song['artist'])
        except IndexError:
            print("song not found")
        else:
            # add_to_playlist(uri_link)
            # print(uri_link, current_workout_length, user_workout_length)
            uri_links.append(uri_link)
            current_workout_length += song['time']

        if(current_workout_length > user_workout_length):
            break
    print(uri_links)
    print("done")

else:
    query_buffer = 0.0000001

    while(current_workout_length < user_workout_length):
        query = {
            'bpm': {"$gt": int(user_bpm) - (query_buffer * int(user_bpm)), "$lt": int(user_bpm) + (query_buffer * int(user_bpm))} ,
            'genre': {'$in': user_genre}
        }
        print(query)
        valid_song = False

        while(not valid_song):
            print("trying...")
            song = db.songs.find_one(query)
            print song
            try:
                #print(song)
                #print type(song)
                uri_link = findSong(song['song'] + " " + song['artist'])
            except TypeError:
                query_buffer += 0.1
                print("none type")
            except IndexError:
                query_buffer += 0.1
                print("song not found")
            else:
                # add_to_playlist(uri_link)
                # print(uri_link, current_workout_length, user_workout_length)
                uri_links.append(uri_link)
                current_workout_length += song['time']
                valid_song = True


        if(current_workout_length > user_workout_length/2):
            user_bpm += BPM_INCREASE
        else:
            user_bpm += BPM_DECREASE

    print("done")
