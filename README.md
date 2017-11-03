# Workflow Sonos controller

Control sonos radiostation / favorites

Depends on:

 * A server with python and soco installed: http://python-soco.com/
 * http://workflow.is/
 * Sonos favorites

To make this work:
* Setup sonos in your network with your favorite radiostations
* Deploy a server with python and soco
  * pip install soco
* Deploy the play.py file
	* Please edit the speaker_name in the play.py
	* Edit the server station names
		* print(stations) on line 18 from play.py
	* Add your own stations to the if/else statement
	
* Load the .wflow in your ios workflow app
	* Edit the server ip and credentials
	* Edit the radio tags
	* Save the workflow as a widget for quick access

Enjoy
