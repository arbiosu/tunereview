from dotenv import load_dotenv
import os
import requests

load_dotenv()


def get_access_token():
    """
    Get the access token to authenticate the Spotify API requests.
    """
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    auth_url = 'https://accounts.spotify.com/api/token'
    grant_type = 'client_credentials'

    auth_response = requests.post(auth_url, {
        'grant_type': grant_type,
        'client_id': client_id,
        'client_secret': client_secret,
    })

    auth_response_data = auth_response.json()

    access_token = auth_response_data['access_token']

    return access_token


def search_album(album_name: str):
    """
    Search for an album by name.
    """

    access_token = get_access_token()

    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    search_url = 'https://api.spotify.com/v1/search'
    params = {
        'q': album_name,
        'type': 'album',
        'limit': 10
    }

    search_response = requests.get(search_url, headers=headers, params=params)

    if search_response.status_code == 200:
        search_response_data = search_response.json()
        albums = search_response_data['albums']['items']

        for album in albums:
            print(f"album id: {album['id']}")
            print(f"album name: {album['name']}")
            print(f"artist: {album['artists'][0]['name']}")

    return albums


print(search_album("Graduation"))
