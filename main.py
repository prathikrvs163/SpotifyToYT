from ytmusicapi import YTMusic
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

# Step 1: Set up authentication with client credentials
SPOTIPY_CLIENT_ID = 'YOUR_SPOTIFY_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'YOUR_SPOTIFY_CLIENT_ID'

# Authenticating via Client Credentials Flow
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)


# Step 2: Get Spotify playlist details
def get_spotify_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    songs = []

    while results:
        for item in results['items']:
            track = item['track']
            song_name = track['name']
            artist_name = track['artists'][0]['name']
            songs.append(f"{song_name} - {artist_name}")

        # Check if there are more pages of results
        if results['next']:
            results = sp.next(results)
        else:
            results = None

    return songs


# Example Spotify Playlist ID (you can extract this from the playlist URL)
playlist_id = 'YOUR_PLAYLIST_ID'  # e.g., '37i9dQZF1DXcBWIGoYBM5M' for a public playlist

# Step 3: Retrieve and print the songs
spotify_songs = get_spotify_playlist_tracks(playlist_id)

print(spotify_songs)

ytmusic = YTMusic('oauth.json')  # You can authenticate using your YTMusic account


def create_youtube_playlist(title, description):
    playlist_id = ytmusic.create_playlist(title, description)
    return playlist_id


yt_playlist_id = create_youtube_playlist("Spotify Playlist name", " ")


def add_song_to_youtube_playlist(playlist_id, song):
    print(song)
    search_results = ytmusic.search(song, filter='songs')
    if search_results:
        song_video_id = search_results[0]['videoId']
        ytmusic.add_playlist_items(playlist_id, [song_video_id])
        time.sleep(1)


# Step 4: Add each Spotify song to YouTube Music Playlist
for song in spotify_songs:
    add_song_to_youtube_playlist(yt_playlist_id, song)
