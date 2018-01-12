#!/usr/bin/env python
import soco
from soco.music_services import MusicService
import sys

names = []
devices = soco.discover()


if devices:
    for device in devices:
        names.append(device.player_name)
    print ','.join(names)
else:
    print False
