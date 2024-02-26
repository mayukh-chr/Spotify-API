import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import json
import workage

load_dotenv()
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
redirect_uri = os.environ['REDIRECT_URI']

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def main():
    print("hello from main")

    load_dotenv()
    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']
    redirect_uri = os.environ['REDIRECT_URI']

    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    
    #workage.module.printPlaylistTracks("37i9dQZF1Fa1IIVtEpGUcU")

    print(workage.module.getTrackDetails("11dFghVXANMlKmJXsNCbNl"))
    

if __name__ == "__main__":
    main()