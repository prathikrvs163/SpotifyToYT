# Spotify to YouTube Music Playlist Transfer

This script allows you to transfer your Spotify playlists to YouTube Music automatically.

## Features

1. Fetches all tracks from a specified Spotify playlist.

2. Create a new playlist on YouTube Music.

3. Add each song from Spotify to the YouTube Music playlist.

## Prerequisites

### Install Required Packages

Run the following command to install the necessary dependencies:

`pip install ytmusicapi spotipy`

## YouTube Music Authentication

To authenticate with YouTube Music:

Run the command:

`ytmusicapi oauth`

Follow the on-screen instructions to complete authentication. This will generate a oauth.json file.

## Configuration

1. Replace the placeholder values in the script:

2. SPOTIPY_CLIENT_ID: Your Spotify client ID.

3. SPOTIPY_CLIENT_SECRET: Your Spotify client secret.

4. playlist_id: The ID of your Spotify playlist.

## Usage

Run the script:

`python script_name.py`

The script will:

1. Fetch songs from the specified Spotify playlist.

2. Create a new playlist on YouTube Music.

3. Add each song to the newly created YouTube Music playlist.

## Notes

1. To avoid API rate limits, the script introduces a 1-second delay (time.sleep(1)) between adding each song.

2. Ensure oauth.json is in the same directory as the script.

## License

This project is for personal use only.
