# let your scrollbit make the decisions for you!
# shake to get an answer chosen at random from the list

import scrollbit
import random
import microbit

# add any more answers here, remembering quote marks and commas between items
answers = ["yes", "no", "maybe"]

# draws a heart in the centre of the screen
# when a shake is detected, picks a random choice from the answers and scrolls it
while True:
    scrollbit.draw_icon(6, 1, microbit.Image.HEART)
    scrollbit.show()
    if microbit.accelerometer.was_gesture("shake"):
        scrollbit.clear()
        scrollbit.scroll(random.choice(answers))
