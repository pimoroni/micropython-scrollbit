# Displays a dot on your scroll:bit, move it by tilting!

# Flash this file your micro:bit,
# then save this as scrollbit.py and transfer it to your micro:bit using the Files menu.

ready = False
try:
    import scrollbit
    ready = True
except ImportError:
    print("Please copy the scrollbit.py library to your micro:bit")

import microbit

while ready:
    x = microbit.accelerometer.get_x() + 1024
    x = max(0, min(2048, x)) / 2048.0
    
    y = microbit.accelerometer.get_y() + 1024
    y = max(0, min(2048, y)) / 2048.0
    
    x = int((scrollbit.WIDTH - 1) * x)
    y = int((scrollbit.HEIGHT - 1) * y)

    scrollbit.clear()
    scrollbit.set_pixel(x, y, 255)
    scrollbit.show()
    
    microbit.sleep(50)