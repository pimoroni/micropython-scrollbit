# code written by F, age 11, at one of our workshops
# randomly turns pixels on or off, creating a game of life effect

import scrollbit
import random

# picks a random pixel on the scrollbit
# picks a second set of pixel coordinates
# sets the first random pixel to full brightness
# sets the second random pixel to off
# shows the changes

while True:
    col = random.randint(0, 16)
    row = random.randint(0, 6)
    newcol = random.randint(0, 16)
    newrow = random.randint(0, 6)

    scrollbit.set_pixel(col, row, 255)
    scrollbit.set_pixel(newcol, newrow, 0)
    scrollbit.show()
