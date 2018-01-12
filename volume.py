#!/usr/bin/env python
import soco
from soco.music_services import MusicService
import sys


def find_speaker(speaker_name):
    speakers = soco.discover()
    for speaker in speakers:
        if speaker.player_name == speaker_name:
            return speaker
    if not speakers:
        print "Speaker not found"
        return False

if len(sys.argv) <= 3:
    print('please add a speakername and "up" or "down" and amount as parameter')
    print('example: living_room up 10')
    sys.exit()

speaker_name = sys.argv[1]
command = sys.argv[2]
amount = sys.argv[3]
speaker = find_speaker(speaker_name)
if speaker:
    if (str(command) == 'up'):
        speaker.volume += int(amount)
        print speaker.volume
        sys.exit()
    if (str(command) == 'down'):
        speaker.volume -= int(amount)
            print speaker.volume
            sys.exit()
else:
    print "False"
    sys.exit()
