#!/usr/bin/env python3
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="e76827e00ebf4df299af1ace0817ea86",
                                                           client_secret="c3636f0904e74ab6967098d25dc2f1c5"))
'''
x = sp.categories(country="US", locale=None, limit=30, offset=0)
print(json.dumps(x, indent=5))
c = sp.category_playlists(category_id='party', country="IN", limit=2, offset=0)
'''
# sad
# https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1?si=9c7c299dac184137

sad = sp.playlist_tracks("spotify:playlist:37i9dQZF1DX7qK8ma5wgG1", fields= "items.track.id, total, items.track.name, items.track.album.artists.name", limit=10)
#print(json.dumps(sad,  indent=5))

# happy
#https://open.spotify.com/playlist/1llkez7kiZtBeOw5UjFlJq?si=4a7282d5a9df49a1
happy = sp.playlist_tracks("spotify:playlist:1llkez7kiZtBeOw5UjFlJq", fields= "items.track.id, total, items.track.name, items.track.album.artists.name", limit=10)
print(json.dumps(happy,  indent=5))





'''
a = sp.playlist_tracks("spotify:playlist:37i9dQZF1DX7qK8ma5wgG1", limit=1)

print(json.dumps(c,  indent=5))
t = sp.track("0gplL1WMoJ6iYaPgMCL0gX")

print(json.dumps(t['name'], indent=5))
print(json.dumps(t['external_urls']['spotify'], indent=5))
print(json.dumps(t['artists']))

'''
