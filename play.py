#!/usr/bin/env python
import soco
from soco.music_services import MusicService
import sys

speaker_name = ''
song_url=''

def find_speaker():
    # Get device and services
    speakers = soco.discover()
    for speaker in speakers:
        if speaker.player_name == speaker_name:
            return speaker
    if not speakers:
        sys.exit()


speaker = find_speaker()

if len(sys.argv) <= 1:
    print('No Playlist Selected')
    sys.exit()
else:
    style = sys.argv[1]
    stations = speaker.get_favorite_radio_stations(0, 2)
    print(stations)
    sys.exit()
    if (str(style) == 'bbc1'):
        song_url = stations['favorites'][0]['uri']
    if (str(style) == 'radio2'):
        song_url = stations['favorites'][1]['uri']

print(song_url)
speaker.volume = 15
speaker.play_uri(uri=song_url,force_radio=True)
