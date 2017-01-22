import pprint, sys, os, subprocess
import spotipy
import spotipy.util as util
from spotifyCredentials import credentials


def spotifyOAuth(listofURI):
    username = credentials()

    scope = "playlist-modify-public"

    token = util.prompt_for_user_token(username, scope)

    tracklist = listofURI

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.user_playlist_create(username, 'Workout', public=True)

        playlists = sp.user_playlists(username)
        for playlist in playlists["items"]:
            if playlist['name'] == 'Workout':
                sp.user_playlist_add_tracks(username, playlist['id'], tracklist)
    return
