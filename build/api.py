#!/usr/bin/env python3
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

class Emotion(object):
  def __init__(self):
    self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="e76827e00ebf4df299af1ace0817ea86",
                                                           client_secret="c3636f0904e74ab6967098d25dc2f1c5"))
  def retrieve_sad(self):
    sad = self.sp.playlist_tracks("spotify:playlist:37i9dQZF1DX7qK8ma5wgG1", fields= "items.track.id, total, items.track.name, items.track.album.artists.name", limit=10)
    return json.dumps(sad,  indent=5)
  
  def retrieve_happy(self):
    happy = self.sp.playlist_tracks("spotify:playlist:1llkez7kiZtBeOw5UjFlJq", fields= "items.track.id, total, items.track.name, items.track.album.artists.name", limit=10)
    return json.dumps(happy,  indent=5)

x = Emotion()
print(x.retrieve_happy())
