import board
import time
import random
import terminalio
import displayio
import vectorio
from adafruit_display_text import label
from digitalio import DigitalInOut, Direction, Pull

# display init
display = board.DISPLAY
display.rotation = 180

# set up act-LED
act = DigitalInOut(board.USER_LED)
act.direction = Direction.OUTPUT
act.value = False

# buttons
a_button = DigitalInOut(board.SW_A)
b_button = DigitalInOut(board.SW_B)
c_button = DigitalInOut(board.SW_C)
r_button = DigitalInOut(board.SW_UP)
a_button.direction = Direction.INPUT
b_button.direction = Direction.INPUT
c_button.direction = Direction.INPUT
r_button.direction = Direction.INPUT
a_button.pull = Pull.DOWN
b_button.pull = Pull.DOWN
c_button.pull = Pull.DOWN
r_button.pull = Pull.DOWN

# Set text, font, and color
title = "{TAROT}"
subtitle = "<by famosomocoso>"
indicator = "press\n  |\n  V"
font = terminalio.FONT
color = 0x000000

# Set the palette for the background color
palette = displayio.Palette(1)
palette[0] = 0xFFFFFF

# Add a background rectangle
rectangle = vectorio.Rectangle(
    pixel_shader=palette, width=display.width + 1, height=display.height + 1, x=0, y=0
)

# Create the title and subtitle labels
title_label = label.Label(font, text=title, color=color, scale=2)
subtitle_label = label.Label(font, text=subtitle, color=color, scale=1)
indicator_label = label.Label(font, text=indicator, color=color, scale=1)

# Creat title image
cover_file = open("/images/start.bmp", "rb")
cover = displayio.OnDiskBitmap(cover_file)
cover_sprite = displayio.TileGrid(
    cover, pixel_shader=getattr(cover, "pixel_shader", displayio.ColorConverter())
)
cover_sprite.x = 16
cover_sprite.y = 90

card_file = open("/images/card.bmp", "rb")
card = displayio.OnDiskBitmap(card_file)

card_sprite = displayio.TileGrid(
    card, pixel_shader=getattr(card, "pixel_shader", displayio.ColorConverter())
)

card_sprite2 = displayio.TileGrid(
    card, pixel_shader=getattr(card, "pixel_shader", displayio.ColorConverter())
)

card_sprite3 = displayio.TileGrid(
    card, pixel_shader=getattr(card, "pixel_shader", displayio.ColorConverter())
)

# Set the label locations
title_label.x = 25
title_label.y = 35

subtitle_label.x = 15
subtitle_label.y = 52

indicator_label.x = 85
indicator_label.y = 260

# list img-file names
image_files = [
    "./images/00.bmp",
    "./images/01.bmp",
    "./images/02.bmp",
    "./images/03.bmp",
    "./images/04.bmp",
    "./images/05.bmp",
    "./images/06.bmp",
    "./images/07.bmp",
    "./images/08.bmp",
    "./images/09.bmp",
    "./images/10.bmp",
    "./images/11.bmp",
    "./images/12.bmp",
    "./images/13.bmp",
    "./images/14.bmp",
    "./images/15.bmp",
    "./images/16.bmp",
    "./images/17.bmp",
    "./images/18.bmp",
    "./images/19.bmp",
    "./images/20.bmp",
    "./images/21.bmp",
    "./images/22.bmp",
    "./images/23.bmp",
    "./images/24.bmp",
    "./images/25.bmp",
    "./images/26.bmp",
    "./images/27.bmp",
    "./images/28.bmp",
    "./images/29.bmp",
    "./images/30.bmp",
    "./images/31.bmp",
    "./images/32.bmp",
    "./images/33.bmp",
    "./images/34.bmp",
    "./images/35.bmp",
    "./images/36.bmp",
    "./images/37.bmp",
    "./images/38.bmp",
    "./images/39.bmp",
    "./images/40.bmp",
    "./images/41.bmp",
    "./images/42.bmp",
    "./images/43.bmp",
    "./images/44.bmp",
    "./images/45.bmp",
    "./images/46.bmp",
    "./images/47.bmp",
    "./images/48.bmp",
    "./images/49.bmp",
    "./images/50.bmp",
    "./images/51.bmp",
    "./images/52.bmp",
    "./images/53.bmp",
    "./images/54.bmp",
    "./images/55.bmp",
]

# load images from list
images = [displayio.OnDiskBitmap(open(filename, "rb")) for filename in image_files]

# create list of TileGrids using loaded images
tilegrids = [
    displayio.TileGrid(
        image, pixel_shader=getattr(image, "pixel_shader", displayio.ColorConverter())
    )
    for image in images
]

# create splash group and append objects
splash = displayio.Group()
splash.append(rectangle)
splash.append(title_label)
splash.append(subtitle_label)
splash.append(indicator_label)
splash.append(cover_sprite)

# preload card screen
card1 = displayio.Group(x=8, y=2)
card2 = displayio.Group(x=8, y=100)
card3 = displayio.Group(x=8, y=198)
card1.append(card_sprite)
card2.append(card_sprite2)
card3.append(card_sprite3)

# show  splash screen and refresh display
time.sleep(1)
display.show(splash)
while display.busy==True:
    time.sleep(0.1)
display.refresh()
time.sleep(3)

splash.remove(title_label)
splash.remove(subtitle_label)
splash.remove(indicator_label)
splash.remove(cover_sprite)

splash.append(card1)
splash.append(card2)
splash.append(card3)

time.sleep(1)
rnx1 = 99
rnx2 = 99
rnx3 = 99

print("--------DEBUG-Info--------")
time.sleep(1)
print("Display-Setting:----------")
print(
    "Rotation =", display.rotation, "Resolution =", display.width, "x", display.height
)
time.sleep(1)
print("Button-State:-------------")
print("A =", a_button.value)  # True == button pressed
print("B =", b_button.value)  # True == button pressed
print("C =", c_button.value)  # True == button pressed
print("R =", r_button.value)  # True == button pressed
time.sleep(2)
print("-------INIT-complete------")
time.sleep(3)
print("-----------ready----------")
act.value = True

while True:
    
    if r_button.value:
        while display.busy==True:
            time.sleep(0.1)
        act.value = False
        display.refresh()
        time.sleep(5)
        act.value = True

    if a_button.value:
        act.value = False
        # Generate a random number in the range of the number of images
        rnx1 = random.randint(0, len(images) - 1)
        print("rn1=", rnx1)
        # Remove all existing TileGrids
        while len(card1) > 0:
            card1.pop()
        time.sleep(0.5)
        # add the randomly selected TileGrid
        if rnx1!=rnx2 and rnx1!=rnx3:
            card1.append(tilegrids[rnx1])
        else:
            card1.append(tilegrids[rnx1-1])
        # refresh to show the 1st card
        while display.busy==True:
            time.sleep(0.1)
        display.refresh()
        time.sleep(5)
        act.value = True

    if b_button.value:
        act.value = False
        rnx2 = random.randint(0, len(images) - 1)
        print("rn2=", rnx2)
        time.sleep(0.5)
        while len(card2) > 0:
            card2.pop()
        time.sleep(0.5)
        if rnx2!=rnx1 and rnx2!=rnx3:
            card2.append(tilegrids[rnx2])
        else:
            card2.append(tilegrids[rnx2-1])
        while display.busy==True:
            time.sleep(0.1)
        display.refresh()
        time.sleep(5)
        act.value = True

    if c_button.value:
        act.value = False
        rnx3 = random.randint(0, len(images) - 1)
        print("rn3=", rnx3)
        time.sleep(0.5)
        while len(card3) > 0:
            card3.pop()
        time.sleep(0.5)
        if rnx3!=rnx1 and rnx3!=rnx2:
            card3.append(tilegrids[rnx3])
        else:
            card3.append(tilegrids[rnx3-1])
        while display.busy==True:
            time.sleep(0.1)
        display.refresh()
        time.sleep(5)
        act.value = True
