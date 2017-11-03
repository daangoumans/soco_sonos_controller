#!/usr/bin/env python
import soco
from soco.music_services import MusicService
import sys

speaker_name = 'Woonkamer'

def find_speaker(speaker_name):
    speakers = soco.discover()
    for speaker in speakers:
        if speaker.player_name == speaker_name:
            return speaker
    if not speakers:
        sys.exit()

def get_play_url(station_name):
    stations = speaker.get_sonos_favorites()
    for station in stations['favorites']:
        if(str(station_name) in station['title']):
            return str(station['uri'])

if len(sys.argv) <= 1:
    print('No radio Selected')
    print('please add "bbc1" or "radio2" as parameter')
    sys.exit()
else:
    style = sys.argv[1]
    if (str(style) == 'bbc1'):
        station_name = 'BBC Radio 1'
    if (str(style) == 'radio2'):
        station_name = 'NPO Radio 2'


speaker = find_speaker(speaker_name)
play_url = str(get_play_url(station_name))
speaker.play_uri(uri=play_url,title=station_name)
