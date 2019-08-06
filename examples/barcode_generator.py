# generates a barcode pattern on the scroll:bit that redraws every 5 seconds
# ensure scrollbit.py is copied onto your micro:bit to avoid import errors

import scrollbit
import random
import time

# you can add another stripe variant here if you like.
stripes = [0, 50, 255]

# chose c for column and r for row but you could use x and y
while True:
    for c in range (0, 17):
        brightness = random.choice(stripes)
        for r in range(0, 7):
            scrollbit.set_pixel(c, r, brightness)
            scrollbit.show()
        time.sleep(5)
        scrollbit.clear()
