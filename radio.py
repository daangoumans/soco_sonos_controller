#!/usr/bin/env python
import soco
from soco.music_services import *
import sys


def find_speaker(speaker_name):
    speakers = soco.discover()
    for speaker in speakers:
        if speaker.player_name == speaker_name:
            return speaker
    if not speakers:
        print "Speaker not found"
        return False

def play_favorite(name):
    all_favorites = speaker.get_sonos_favorites()
    for favorite in all_favorites['favorites']:
        if (str(favorite['title']) == str(name)):
           speaker.play_uri(uri=favorite['uri'], title=favorite['title'], meta=favorite['meta'])
           return speaker.get_current_track_info()['title']

if len(sys.argv) <= 2:
    print('please add a speakername and "list" to get favorite items.')
    print('If you got the uri play the radio as parameter')
    print('example: living_room play_favorite <favorite name>')
    sys.exit()

speaker_name = sys.argv[1]
command = sys.argv[2]
favorite_list = []
speaker = find_speaker(speaker_name)

if speaker:
    if (str(command) == 'list'):
        all_favorites = speaker.get_sonos_favorites()
        for favorite in all_favorites['favorites']:
            favorite_list.append(favorite['title'])
        print ','.join(favorite_list)
        sys.exit()
    if (str(command) == 'play_favorite'):
        if (sys.argv[3]):
            name = sys.argv[3]
            song = play_favorite(name)
            if song:
                print song
                sys.exit()
            else:
                print "False"
                sys.exit()
