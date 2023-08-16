import os
import sys
import spotipy 
from dotenv import load_dotenv
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import server_socket

# userID: neilhemm0 or 023e099b16264e2c

# Controls all actions. 
def actions(action, device):

    item = (sp.currently_playing())
    disallows = item['actions']['disallows'].keys()
    playback = sp.current_playback()

    if (action == '0'):
        sp.next_track(device_id=device)

    elif (action == '1'):
        if not item['is_playing']:
            sp.start_playback(device_id=device)

        else:
            sp.pause_playback(device_id=device)

    elif (action == '2'):
            sp.previous_track(device_id=device)

    elif (action == '3') and 'toggling_shuffle' not in disallows:
        if not playback['shuffle_state']:
            sp.shuffle(True, device)

        else:
            sp.shuffle(False, device)

    elif (action == '4') and 'toggling_repeat_track' not in disallows:
        if playback['repeat_state'] == 'track':
            sp.repeat('context', device)

        elif playback['repeat_state'] == 'context':
            sp.repeat('off', device)

        elif playback['repeat_state'] == 'off':
            sp.repeat('track', device)

# Client ID and Client Secret

load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
USER_TOKEN = os.getenv("USER_TOKEN")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# Scope

modifyPlayback = "user-modify-playback-state"
deviceInfo = "user-read-playback-state"
scopes=[modifyPlayback,deviceInfo]

# user token

spotifyObject = spotipy.Spotify(auth=USER_TOKEN)

#  oauth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))

# action loop

# Updates to current device
device = sp.devices()['devices'][0]['id']

while True:
    # Gathers command from socket
    action = server_socket.start()
    try:
        # Sends command to API
        actions(action, device)
    except:
        device = sp.devices()['devices'][0]['id']
        actions(action, device)

