#!/usr/bin/env python3
import spotipy
import json
from types import SimpleNamespace
from spotipy.oauth2 import SpotifyClientCredentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="e76827e00ebf4df299af1ace0817ea86",
                                                           client_secret="c3636f0904e74ab6967098d25dc2f1c5"))
def retrieve_sad():
  sad = sp.playlist_tracks("spotify:playlist:37i9dQZF1DX7qK8ma5wgG1", fields= "items.track.id, total, items.track.name, items.track.album.artists.name", limit=20)
  return sad

def retrieve_happy():
  happy = sp.playlist_tracks("spotify:playlist:1llkez7kiZtBeOw5UjFlJq", fields= "items.track.id, total, items.track.name, items.track.album.artists.name", limit=20)
  return happy

def retrieve_neutral():
  neutral = sp.playlist_tracks("spotify:playlist:37i9dQZF1DWWQRwui0ExPn", fields= "items.track.id, total, items.track.name, items.track.album.artists.name", limit=20)
  return neutral



with open('data/happy_data.json', 'w') as f:
  happy = retrieve_happy()
  json.dump(happy, f)

with open('data/sad_data.json', 'w') as f:
  sad = retrieve_sad()
  json.dump(sad, f)

with open('data/neutral_data.json', 'w') as f:
  neu = retrieve_neutral()
  for x in neu['items']:
    print(len(x['track']['album']['artists']))
  json.dump(neu, f)





