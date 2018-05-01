from microbit import sleep, i2c, Image as I

WIDTH = 17
HEIGHT = 7

_f = 0
_b = bytearray(145)
_i = [getattr(I,x) for x in dir(I) if hasattr(getattr(I,x),'get_pixel')]

def _w(*args):
    if len(args) == 1: args = args[0]
    i2c.write(116, bytes(args))

def clear():
    global _b
    del _b
    _b = bytearray(145)
    
def icon_format(text):
    r = {}
    for a_n in dir(I):
       a = getattr(I, a_n)
       if a in _i and a_n in text:
           r[a_n] = chr(128+_i.index(a))

    return text.format(**r)

def show():
    global _f
    _f = not _f
    _w(253, _f)
    _b[0] = 36
    _w(_b)
    _w(253, 11)
    _w(1, _f)

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
    i = None
    for letter in text:
        i = None
        letter_width = char_len(letter)

        if letter != " " and (offset_col + letter_width) >= 1:
            if ord(letter) > 127:
                i = _i[ord(letter) - 128]
            else:
                try:
                    i = I(letter)
                except:
                    pass

        if i is not None:
            if not draw_icon(offset_col, offset_row, i, brightness):
                return

        offset_col += letter_width + 1

    del i

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
    _b[_pixel_addr(col, row)] = brightness

def get_pixel(col, row):
    return _b[_pixel_addr(col, row)]
    
def _pixel_addr(x, y):
    y = 7 - (y + 1)

    if x > 8:
        x = x - 8
        y = 6 - (y + 8)
    else:
        x = 8 - x

    return (x * 16 + y) + 1

_w(253, 11)
sleep(100)
_w(10, 0)
sleep(100)
_w(10, 1)
sleep(100)
_w(0, 0)
_w(6, 0)
for bank in [1,0]:
    _w(253, bank)
    _w([0] + [255] * 17)
clear()
show()