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

if len(sys.argv) <= 2:
    print('please add a speakername and "status", "play", "pause", "stop" as parameter')
    print('example: living_room pause')
    sys.exit()

speaker_name = sys.argv[1]
command = sys.argv[2]
speaker = find_speaker(speaker_name)
if speaker:
    if (str(command) == 'status'):
        print speaker.get_current_transport_info()['current_transport_state']
    if (str(command) == 'play'):
        speaker.play()
        print speaker.get_current_transport_info()['current_transport_state']
    if (str(command) == 'pause'):
        speaker.pause()
        print speaker.get_current_transport_info()['current_transport_state']
    if (str(command) == 'stop'):
        speaker.stop()
        print speaker.get_current_transport_info()['current_transport_state']
else:
    print "False"
    sys.exit()
