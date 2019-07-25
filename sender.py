from time import sleep

from microbit import *
import radio

# =============================================================================

radio.config(group=0, length=251) # group=N is team by team!
radio.on()

# =============================================================================

while True:
    radio.send('{},{},{},{}'.format(
        running_time(),
        *accelerometer.get_values()
    ))
    sleep(0.5)
