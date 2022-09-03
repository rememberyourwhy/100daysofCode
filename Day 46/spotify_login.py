# 85ce79a536e84726825de05e1b9eecc3
# 6f8a9a90fc184417b11b5b82862f05aa

# OAUTH_AUTHORIZE_URL='https://accounts.spotify.com/authorize'
#
# OAUTH_TOKEN_URL='https://accounts.spotify.com/api/token'
#
# __init__(
#     client_id=None,
#     client_secret=None,
#     redirect_uri=None,
#     state=None,
#     scope=None,
#     cache_path=None,
#     username=None,
#     proxies=None,
#     show_dialog=False,
#     requests_session=True,
#     requests_timeout=None
# )

"""

Create a private playlist on Spotify

"""
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# import json
#
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

import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "85ce79a536e84726825de05e1b9eecc3"
SPOTIPY_CLIENT_SECRET = "6f8a9a90fc184417b11b5b82862f05aa"

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
user_id = sp.current_user()["id"]
print(user_id)
