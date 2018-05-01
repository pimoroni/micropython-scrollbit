import random
try:
    import scrollbit
    scrollbit.setup()
except ImportError:
    print("Please copy the scrollbit.py library to your micro:bit")

import microbit

numbers = ["One", "Two", "Three", "Four", "Five", "Six"]

while True:
    if microbit.button_a.was_pressed():
        try:
            scrollbit.scroll(random.choice(numbers))
        except:
            print(random.choice(numbers))
    microbit.sleep(100)