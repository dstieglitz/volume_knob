# Python rotary encoder ALSA volume control for Raspberry Pi

A little project that allows you to control the ALSA mixer using a rotary encoder and some open source libraries. Includes a systemd service definition for installing a service on startup.

# Dependencies

py-gaugette (https://github.com/guyc/py-gaugette.git)

pyalsaaudio (https://github.com/larsimmisch/pyalsaaudio.git)

wiringpi (https://github.com/WiringPi/WiringPi.git)

# Installation 

Install py-gaugette and pyalsaaudio as python libraries, either through pip or using `setup.py` (see each project for instructions)

# Service Installation

Copy volume_knob.service to `/lib/systemd/system` 

To make the service startup automatically, run

`sudo systemctl enable volume_knob.service`

# Configuration

Make sure the pins referenced in volume_knob.py correspond to how your knob is wired.

# Testing

Install the service, start the service, play some test audio (convieniently provided in test_audio/) and turn the knob. Enjoy the changing volume.

