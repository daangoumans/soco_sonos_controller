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

if len(sys.argv) <= 1:
    print('No command selected')
    print('please add "up" or "down" as parameter')
    sys.exit()

command = sys.argv[1]
speaker = find_speaker(speaker_name)
if (str(command) == 'up'):
	speaker.volume += 10
if (str(command) == 'down'):
	speaker.volume -= 10
