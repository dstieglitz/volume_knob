import time
import gaugette.gpio
import gaugette.rotary_encoder
import mixertest
import alsaaudio

#
# Configure this for your environment
#
A_PIN = 7 
B_PIN = 9 
mixer_name = 'PCM'
min_state = 0
max_state = 100
multiplier = 2

# Returns volume in percent format or -1 if muted
def get_volume(name, kwargs):
    try:
        mixer = alsaaudio.Mixer(name, **kwargs)
    except alsaaudio.ALSAAudioError:
        print("No such mixer", file=sys.stderr)
        sys.exit(1)

    try:
        mutes = mixer.getmute()
        for i in range(len(mutes)):
            if mutes[i]:
                return -1
    except alsaaudio.ALSAAudioError:
        # May not support muting
        pass

    volumes = mixer.getvolume()
    return volumes[0] # assumes all channels are at the same volume


def rotated(direction):
    global state
    global max_state
    global min_state

    if state+direction*multiplier >= max_state: state = max_state
    elif state+direction*multiplier <= min_state: state = min_state
    else: state+=direction*multiplier

    print(state)
    mixertest.set_mixer('PCM',str(state),{'cardindex':0});

def pushed():
    # FIXME implement
    pass

state = get_volume(mixer_name,{})

gpio = gaugette.gpio.GPIO()
encoder = gaugette.rotary_encoder.RotaryEncoder(gpio, A_PIN, B_PIN, rotated)
encoder.start()

while True:
    time.sleep(100)

