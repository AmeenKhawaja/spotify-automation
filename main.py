import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
 
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(client_id, client_secret)