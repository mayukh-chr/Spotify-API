import base64
import os
from dotenv import load_dotenv
import json
import requests
from urllib.parse import urlencode


load_dotenv()
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
redirect_uri = os.environ["REDIRECT_URI"]
response_type = 'code'


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers = headers, data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = requests.get(query_url, headers = headers)
    json_result = json.loads(result.content)["artists"]["items"]
    
    if len(json_result) == 0:
        print("No artist found.")
        return None
    
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def Oauth2():
    auth_url = 'https://accounts.spotify.com/authorize'
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'scope': 'user-read-private user-read-email',
        'redirect_uri': redirect_uri,
          # Add necessary scopes
        }
    auth_url = f"{auth_url}?{urlencode(params)}"
    print(f"1. Click this URL to authorize your app: {auth_url}")

def get_my_followers(token):
    
    url = "https://api.spotify.com/v1/me/followers"
    headers = get_auth_header(token)
    result = requests.get(url, headers= headers)
    if result.status_code == 200:
        followers_data = result.json()
        total_followers = followers_data["total"]
        followers = followers_data["followers"]
        print(f"Total Spotify Followers: {total_followers}")
        print("Followers:")
        for follower in followers:
            print(f"- {follower['display_name']}")

    else:
        print("Failed to retrieve Spotify followers.")
        print(f"Status Code: {result.status_code}")
        print(f"Response: {result.text}")


token = get_token()

get_my_followers(token)