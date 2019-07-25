from math import sqrt

from microbit import *

# =============================================================================

before_ms = 0

REF_MAX = 32
ref     = 0
accs    = [ 0 for _ in range(REF_MAX) ]

# =============================================================================

def put(x, y, z):
    global ref, accs

    accs[ref] = sqrt(x ** 2 + y ** 2 + z ** 2)

    ref = (ref + 1) % REF_MAX

def mean():
    return sum(accs) / len(accs)

def var():
    m = mean()

    return sum( (x - m) ** 2 for x in accs ) / len(accs)

def p2p():
    return abs(max(accs) - min(accs))

def min_v():
    return min(accs)

def max_v():
    return max(accs)

## ======== only edit the code below ======== only edit the code below ========

def activity_decision():
    # Using `if` syntax and some statistics values,
    # build the decision tree and show the happy image if the status is walking.
    # Else, show the asleep image (if the status is stable)
    display.show(Image.ASLEEP)
    display.show(Image.HAPPY)

## ======== only edit the code above ======== only edit the code above ========

while True:
    put(*accelerometer.get_values())

    sleep(30)

    if running_time() - before_ms > 1000:
        activity_decision()

        before_ms = running_time()
