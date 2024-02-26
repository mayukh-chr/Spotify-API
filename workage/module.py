from main import sp

def printPlaylistTracks(playlist_id): # Print names of all tracks in the playlist
    

    playlist_tracks = sp.playlist_tracks(playlist_id)

    # Print names of all tracks in the playlist
    print("Tracks in Playlist:")
    for item in playlist_tracks['items']:
        print(item['track']['name'])
        #break

def getTrackDuration(track_id): # returns duration of a track given its track id

    # Get track information
    track_info = sp.track(track_id)

    # Extract duration from track information
    duration_ms = track_info['duration_ms']

    # Convert duration from milliseconds to seconds
    duration_sec = duration_ms / 1000

    return duration_sec


def getTrackDetails(track_id): #returns the JSON output of each track
    # Get track information
    track_info = sp.track(track_id)

    return track_info 


    
