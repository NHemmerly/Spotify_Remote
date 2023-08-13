import os
import sys
import spotipy 
from dotenv import load_dotenv
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import server_socket

# userID: neilhemm0 or 023e099b16264e2c

def actions(action, device):
    if (action == 'next'):
        sp.next_track(device_id=device)
    elif (action == 'pause'):
        sp.pause_playback(device_id=device)
    elif (action == 'previous'):
        sp.previous_track(device_id=device)

# Client ID and Client Secret

load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_TOKEN = os.getenv("USER_TOKEN")
SPOTIPY_REDIRECT_URI = os.getenv("REDIRECT_URI")

# arguments

# action = sys.argv[1]

# Scope

modifyPlayback = "user-modify-playback-state"
deviceInfo = "user-read-playback-state"
scopes=[modifyPlayback,deviceInfo]

# user token

spotifyObject = spotipy.Spotify(auth=USER_TOKEN)

#  oauth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))

# actions
device = sp.devices()['devices'][0]['id']
print(device)

while True:
    action = server_socket.start()
    try:
        actions(action, device)
    except:
        device = sp.devices()['devices'][0]['id']
        actions(action, device)

# Nice to have functionality
# repeat(state, device_id=None)
# shuffle(state, device_id=None)
