import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv


#


load_dotenv()
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
redirect_uri = os.environ['REDIRECT_URI']

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def tenSavedTracks():
    
    results = sp.current_user_saved_tracks(limit=10)
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx+1, track['artists'][0]['name'], " - ", track['name'])

def getWrapped():
    #something something
    return 0    

def getPlaylistByID(PlaylistID):
    
    
    results = sp.playlist(PlaylistID)
    print(results['name'])
    #print(results)

def printPlaylistTracks(playlist_id):
    # Fetch playlist tracks
    results = sp.playlist_tracks(playlist_id)
    
    # Loop through each track and print its name
    for idx, item in enumerate(results['items']):
        
        track = item['track']
        album = track['album']
        artists = track['artists']
        artist_id = item['track']['album']['artists'][0]['id']

        
        
        

        
        
        print("name: ", track['name'])
        print("track ID: ", track['id'])
        print("artist ID: ", album['id'])
        
        print("Popularity: ", track['popularity'])
        #print("artist name: ", artists['name'])                this doesnt work for some reason, gonna check on it later
        print("duration ms: ", track['duration_ms'])
        print("duration s: ", convertmstosec(track['duration_ms']))
        print("release year: ", album["release_date"][0:4])
        print("release month: ", album["release_date"][5:7])

        
        #print(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}")
        break
        
        
    print()

def print_playlist_tracks_details(playlist_id):
    # Fetch playlist tracks
    results = sp.playlist_tracks(playlist_id)
    
    # Loop through each track and print its details
    for idx, item in enumerate(results['items']):
        print(item)
        print(item[""])
    
    print()

def convertmstosec(time):
    result = time/1000
    return int(result)

def artistGenres(id):
    result = sp.artist(id)
    for item in (result['genres']):
        print(item, end=" ")

def main():
    print("hello from main")
    #tenSavedTracks()

    #printPlaylistTracks("37i9dQZF1Fa1IIVtEpGUcU")
    printPlaylistTracks("37i9dQZF1Fa1IIVtEpGUcU")


if __name__ == "__main__":

    main()