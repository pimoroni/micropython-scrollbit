# MicroPython scroll:bit library for the BBC micro:bit

# Installing

First, install the Mu micropython editor from https://codewith.mu/ by following the instructions online.

Copy the code from library/scrollbit.py into your "mu_code" folder by pasting it into the blank file in the Mu editor and saving it as "scrollbit.py". The folder might be in:

* C:\Users\YourUserName\mu_code on Windows
* /Users/YourUserName/mu_code on macOS

Create a new blank file in Mu for your project, leave it blank and Flash it to your micro:bit with the Flash button. You can close this for now.

Create another new file, save this one as "main.py" and keep it open.

Now open the "Files" dialog (you might have to close the "Repl" first) and drag and drop main.py and scrollbit.py from the right pane, to the left pane.

When you reset your micro:bit, it will load main.py- so you can "import scrollbit" and start writing your code here!

# Function Reference

## Scroll text across your scroll:bit

`scrollbit.scroll(text, brightness=255, delay=10, icons=True)`

The text will always start off the right edge of the screen, and scroll across until it disappears off the left edge. You can optionally set the brightness and delay, and turn off icon support if you dont need it (slightly faster).

EG:

`scrollbit.scroll("Hello {HEART} World")`

Icon names should be in ALL CAPS and surrounded by {CURLY BRACES}. Available icons are:

HEART, HEART_SMALL, HAPPY, SMILE, SAD, CONFUSED, ANGRY, ASLEEP, SURPRISED, SILLY, FABULOUS, MEH, YES, NO, CLOCK12, CLOCK1, CLOCK2, CLOCK3, CLOCK4, CLOCK5, CLOCK6, CLOCK7, CLOCK8, CLOCK9, CLOCK10, CLOCK11, ARROW_N, ARROW_NE, ARROW_E, ARROW_SE, ARROW_S, ARROW_SW, ARROW_W, ARROW_NW, TRIANGLE, TRIANGLE_LEFT, CHESSBOARD, DIAMOND, DIAMOND_SMALL, SQUARE, SQUARE_SMALL, RABBIT, COW, MUSIC_CROTCHET, MUSIC_QUAVER, MUSIC_QUAVERS, PITCHFORK, XMAS, PACMAN, TARGET, ALL_CLOCKS, ALL_ARROWS, TSHIRT, ROLLERSKATE, DUCK, HOUSE, TORTOISE, BUTTERFLY, STICKFIGURE, GHOST, SWORD, GIRAFFE, SKULL, UMBRELLA and SNAKE

## Write a string of text to scroll:bit

`scrollbit.write(text, offset_col=0, offset_row=0, brightness=255)`

This wont appear immediately, you'll have to call `show()` to display it, but it's useful for positioning short phrases on scroll:bit.

## Show an icon on scroll:bit

`scrollbit.draw_icon(col, row, icon, brightness=255)`

You'll need to use an icon from `microbit.Image` like `microbit.Image.HAPPY`, consult the list above or try `dir(microbit.Image)` in the Repl.

## Set a single pixel

`scrollbit.set_pixel(col, row, brightness)`

The columns and rows you can use are labelled on your scroll:bit, and the brightness can be from 0 to 255.

## Show your changes

`scrollbit.show()`

Call this to display your changes on scroll:bit.

## Clear the scroll:bit

`scrollbit.clear()`

Call this to clear the scroll:bit display.

# Troubleshooting

## Memory Error

If you receive a Memory Error exception on the line where you `import scroll` bit the best resolution is to copy the contents of `scrollbit.py` into your `main.py` file.

