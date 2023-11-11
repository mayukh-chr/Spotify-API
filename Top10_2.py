import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv


load_dotenv()
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
redirect_uri = os.environ['REDIRECT_URI']

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks(limit=10)
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx+1, track['artists'][0]['name'], " - ", track['name'])

