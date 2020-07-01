import time
import gaugette.gpio
import gaugette.rotary_encoder
import mixertest

A_PIN = 7 
B_PIN = 9 

state = 0
min_state = 0
max_state = 100
multiplier = 2

def rotated(direction):
    global state
    global max_state
    global min_state

    if state+direction*multiplier >= max_state: state = max_state
    elif state+direction*multiplier <= min_state: state = min_state
    else: state+=direction*multiplier

    print(state)
    mixertest.set_mixer('PCM',str(state),{'cardindex':0});

gpio = gaugette.gpio.GPIO()
encoder = gaugette.rotary_encoder.RotaryEncoder(gpio, A_PIN, B_PIN, rotated)
encoder.start()

while True:
    time.sleep(100)

