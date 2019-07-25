from microbit import *
import radio

# =============================================================================

radio.config(group=0, length=251) # group=N is team by team!
radio.on()

# =============================================================================

while True:
    received = radio.receive()

    if received is not None: print(received)