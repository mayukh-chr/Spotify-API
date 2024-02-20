import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import json

'''todolist
    1. to write a detailed report on json output of item
    2. try to make a graph on genre vs count'''
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
    count = 1


    # Loop through each track and print its name
    for idx, item in enumerate(results['items']):
        
        track = item['track']
        artist = track['artists']

        album = track['album']
        artist = artist[0]['name']
        song = track['name']
        
        if count == 1:
            j_album = {f'album {count}':album}
            j_artist = {f'artist {count}':artist}
            j_song = {f'song {count}':song}
        else:
            j_album[f'album {count}'] = album
            j_artist[f'artist {count}'] = artist
            j_song[f'song {count}'] = song

        count += 1

    with (
        #open('data.json', 'w+') as t,
        open('album.json', 'w') as al,
        open('artist.json', 'w') as ar,
        open('song.json', 'w') as s
        ):
        json.dump(j_album, al)
        json.dump(j_artist, ar)
        json.dump(j_song, s)
        
        

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
    #print_playlist_tracks_details("37i9dQZF1Fa1IIVtEpGUcU")



if __name__ == "__main__":

    main()

