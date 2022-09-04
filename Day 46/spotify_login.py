"""

Create a private playlist on Spotify

"""
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# import json
#
# Authentication
# scope = "playlist-modify-private"
# username = "31jlthfb4qsn4tssxem7cvohxjfa"
#
# token = SpotifyOAuth(scope=scope, username=username)
# spotifyObject = spotipy.Spotify(auth_manager=token)
#
# # create the playlist
# playlist_name = input("Enter a playlist name: ")
# playlist_description = input("Enter a playlist description: ")
#
# spotifyObject.user_playlist_create(user=username, name=playlist_name, public=False, description=playlist_description)

"""
Set these environment variables:
SPOTIPY_CLIENT_ID=85ce79a536e84726825de05e1b9eecc3;
SPOTIPY_CLIENT_SECRET=6f8a9a90fc184417b11b5b82862f05aa;
SPOTIPY_REDIRECT_URI=http://example.com
"""

"""
Get 100 top song
"""


import spotipy
from spotipy.oauth2 import SpotifyOAuth
from module_100topsong import get_top_song_list
import json

SPOTIPY_CLIENT_ID = "85ce79a536e84726825de05e1b9eecc3"
SPOTIPY_CLIENT_SECRET = "6f8a9a90fc184417b11b5b82862f05aa"


# -------------------------- CREATE SPOTIFY OBJECT -------------------------- #
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

# I have no idea about cache path.
# Compare to the other approach:
# Kalyan Codes YouTube tut approach:
# parameters:
# SPOTIPY_CLIENT_ID
# SPOTIPY_CLIENT_SECRET
# SPOTIPY_REDIRECT_URI
# scope, username from SpotifyOAuth

# Angela's approach is quite similar, the only different is:
# She tried to save cache_path to a token file
# And set show_dialog to True which is True anyway

# ---------------------- GET USER ID ---------------------------- #
user_id = sp.current_user()["id"]
print(user_id)

# ---------------------- GET DATE INPUT FROM USER --------------- #
# ---------------------- CREATE A PLAYLIST ---------------------- #
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

playlist_description = f"List Top 100 Billboard from date: {date}"

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, description=playlist_description)
# with open(file="user_playlist_create.json", mode="w") as user_playlist_create_json:
#     json.dump(playlist, user_playlist_create_json, indent=4)
playlist_id = playlist["id"]

# ---------------------- USE OTHER FILE'S FUNCTION TO GET SONG LIST FROM WEB ------------------ #
song_names = get_top_song_list(date)
song_uris = []
year = date.split("-")[0]

# ---------------------- SEARCH FOR SONGS -------------------- #
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# ---------------------- GET PLAYLIST ID --------------------- #
# Approach 1: Get from the list of playlists
# prePlaylist = sp.user_playlists(user=user_id)
# # with open(file="playlists_list.json", mode="w") as playlists_list_json:
# #     json.dump(prePlaylist, playlists_list_json, indent=4)
#
# playlist_id = prePlaylist["items"][0]["id"]

# Approach 2: Get from response message when we created the playlist above

# ----------------------- ADD SONGS TO THE PLAYLIST ------------ #
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

# 2000-08-12
# user_id = 31jlthfb4qsn4tssxem7cvohxjfa
