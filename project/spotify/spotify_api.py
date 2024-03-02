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
        'limit': 3
    }

    search_response = requests.get(search_url, headers=headers, params=params)

    if search_response.status_code == 200:
        search_response_data = search_response.json()
        albums = search_response_data['albums']['items']

        # for album in albums:
        #     print(f"album id: {album['id']}")
        #     print(f"album name: {album['name']}")
        #     print(f"artist: {album['artists'][0]['name']}")

        return albums

    if search_response.status_code == 401:
        print("Error 400: Bad or Expired Token")
        return
    if search_response.status_code == 403:
        print("Error 403: Bad OAuth Request")
    if search_response.status_code == 429:
        print("Error 429: The app has exceeded its rate limits.")


def get_album_genre(album_id: str) -> str:
    """
    Get the genre of an album by its Spotify id.

    Args:
        album_id: The Spotify id of the album.

    Returns:
        genre: a string representing the genre of the album.
    """

    access_token = get_access_token()

    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    search_url = f"https://api.spotify.com/v1/albums/{album_id}"

    search_response = requests.get(search_url, headers=headers)

    if search_response.status_code == 200:
        search_response_data = search_response.json()
        genre = search_response_data['genres']

        return genre
