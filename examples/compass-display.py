
# Shows the compass heading on your scroll:bit
# You will need to calibrate the compass by tilting the micro:bit
# when your program starts.

# Flash a blank file to your micro:bit,
# then save this as main.py and transfer it to your micro:bit using the Files menu
# you will also need to copy over scrollbit.py, see README.md for details.

import scrollbit
import microbit
import time

microbit.compass.calibrate()

while True:
    scrollbit.clear()
    scrollbit.write(str(microbit.compass.heading()), offset_col=1, offset_row=1, brightness=100)
    scrollbit.show()
    time.sleep(1)
