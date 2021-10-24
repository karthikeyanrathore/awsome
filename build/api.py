#!/usr/bin/env python3
import spotipy
import json
import config
from spotipy.oauth2 import SpotifyClientCredentials

class Emotion(object):
  def __init__(self):
    self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config.CLIENT_ID,
                                                           client_secret=config.CLIENT_SECRET))
  def retrieve_sad(self):
    sad = self.sp.playlist_tracks("spotify:playlist:37i9dQZF1DX7qK8ma5wgG1", fields= "items.track.id, total, items.track.name, items.track.album.artists.name", limit=10)
    return json.dumps(sad,  indent=5)
  
  def retrieve_happy(self):
    happy = self.sp.playlist_tracks("spotify:playlist:1llkez7kiZtBeOw5UjFlJq", fields= "items.track.id, total, items.track.name, items.track.album.artists.name", limit=10)
    return json.dumps(happy,  indent=5)

x = Emotion()
print(x.retrieve_happy())
