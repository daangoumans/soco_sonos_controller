#!/usr/bin/env python
import soco

# Get device and services
device = soco.discovery.any_soco()
print(device)
services = device.music_services.get_all_music_services_names()
print(services)


# Use service
spotify = MusicService('Spotify')

if 'chill' in input:
    response =  spotify.get_metadata(item_id='spotify:user:spotify:playlist:0FQk6BADgIIYd3yTLCThjg')
    print(response)

request_uri = spotify.sonos_uri_from_id(response)
device.clear_queue()
device.add_to_queue(request_uri)
device.play_mode("SHUFFLE_NOREPEAT")
device.play()
