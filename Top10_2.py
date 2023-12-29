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


def tenSavedTracks():
    
    results = sp.current_user_saved_tracks(limit=1)
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
        artist = track['artists']
        artists_name = artist[0]['name']
        artist_id = artist[0]['id']

        
        print("genres: ", ', '.join(sp.artist(artist_id)['genres']))
        print("track name: ", track['name'])
        print("track ID: ", track['id'])
        print("artist ID: ", artist_id)
        
        print("Popularity: ", track['popularity'])
        print("artist name: ", artists_name)                
        print("duration ms: ", track['duration_ms'])
        print("duration s: ", convertmstosec(track['duration_ms']))
        print("release year: ", album["release_date"][0:4])
        print("release month: ", album["release_date"][5:7])
        
        print('------------------------------------------------')
        
        
        #print(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}")
        
        
        

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
    list = sp.artist(id)['genres']
    genre = ', '.join(list)
    print ("genres: ", genre)
    
    
        
        

def main():
    print("hello from main")
    #tenSavedTracks()

    #printPlaylistTracks("37i9dQZF1Fa1IIVtEpGUcU")
    printPlaylistTracks("37i9dQZF1Fa1IIVtEpGUcU")


if __name__ == "__main__":

    main()