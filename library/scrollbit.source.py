from microbit import sleep, i2c, Image

WIDTH = 17
HEIGHT = 7

orientation = 0
NORMAL = 0
INVERT = 1

_ADDRESS = 0x74

_MODE_REGISTER = 0x00
_FRAME_REGISTER = 0x01
_AUDIOSYNC_REGISTER = 0x06
_SHUTDOWN_REGISTER = 0x0a

_CONFIG_BANK = 0x0b
_BANK_ADDRESS = 0xfd

_PICTURE_MODE = 0x00
_AUTOPLAY_MODE = 0x08
_AUDIOPLAY_MODE = 0x18

_ENABLE_OFFSET = 0x00
_BLINK_OFFSET = 0x12
_COLOR_OFFSET = 0x24

_frame = 0
_buf = bytearray(145)
_icons = [getattr(Image,x) for x in dir(Image) if hasattr(getattr(Image,x),'get_pixel')]

def _i2c_write(*args):
    if len(args) == 1: args = args[0]
    i2c.write(_ADDRESS, bytes(args))

def clear():
    global _buf
    del _buf
    _buf = bytearray(145)
    
def icon_format(text):
    replace = {}
    for attr_name in dir(Image):
       attr = getattr(Image, attr_name)
       if attr in _icons and attr_name in text:
           replace[attr_name] = chr(128+_icons.index(attr))

    return text.format(**replace)

def show():
    global _frame

    _frame = not _frame

    _i2c_write(_BANK_ADDRESS, _frame)

    _buf[0] = _COLOR_OFFSET
    _i2c_write(_buf)

    _i2c_write(_BANK_ADDRESS, _CONFIG_BANK)
    _i2c_write(_FRAME_REGISTER, _frame)

def scroll(text, brightness=255, delay=10, icons=True):
    if icons: text = icon_format(text)
    for x in range(text_len(text) + WIDTH):
        clear()
        write(text, -x + WIDTH, 1, brightness)
        show()
        sleep(delay)

def char_len(char):
    if char in b"\"*+-0123<=>ABCDEFHKLOPQSUXZ[]^bcdefghjklnopqrsxz{":
        return 4
    if char in b"!'.:i|":
        return 2
    if char in b" (),;I`}":
        return 3
    return 5

def text_len(text):
    return sum(char_len(c) + 1 for c in text)

def write(text, offset_col=0, offset_row=0, brightness=255):
    image = None
    for letter in text:
        image = None
        letter_width = char_len(letter)

        if letter != " " and (offset_col + letter_width) >= 1:
            if ord(letter) > 127:
                image = _icons[ord(letter) - 128]
            else:
                try:
                    image = Image(letter)
                except:
                    pass

        if image is not None:
            if not draw_icon(offset_col, offset_row, image, brightness):
                return

        offset_col += letter_width + 1

    del image

def draw_icon(col, row, icon, brightness=255):
    brightness //= 9
    for x in range(5):
        if col + x < 0:
            continue
        if col + x >= WIDTH:
            return False
        for y in range(5):
            if not icon.get_pixel(x, y): continue
            try:
                set_pixel(x + col, y + row, icon.get_pixel(x, y) * brightness)
            except IndexError:
                pass
    return True

def set_pixel(col, row, brightness):
    _buf[_pixel_addr(col, row)] = brightness

def get_pixel(col, row):
    return _buf[_pixel_addr(col, row)]
    
def _pixel_addr(x, y):
    y =  (7 - (y + 1))*(1 - orientation) + orientation*y
    x = (17 - (x + 1))*orientation + (1 - orientation)*x

    if x > 8:
        x = x - 8
        y = 6 - (y + 8)
    else:
        x = 8 - x

    return (x * 16 + y) + 1

_i2c_write(_BANK_ADDRESS, _CONFIG_BANK)

sleep(100)
_i2c_write(_SHUTDOWN_REGISTER, 0)
sleep(100)
_i2c_write(_SHUTDOWN_REGISTER, 1)
sleep(100)

_i2c_write(_MODE_REGISTER, _PICTURE_MODE)
_i2c_write(_AUDIOSYNC_REGISTER, 0)

for bank in [1,0]:
    _i2c_write(_BANK_ADDRESS, bank)
    _i2c_write([0] + [255] * 17)
    
clear()
show()
