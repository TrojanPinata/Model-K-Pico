# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid white
background, a smaller black rectangle, and some white text.
"""

import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import busio
import adafruit_imageload
from adafruit_bitmap_font import bitmap_font

displayio.release_displays()

# Use for I2C
i2c = busio.I2C(board.GP1, board.GP0)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
display.auto_brightness = False
display.brightness = 0.1



#for image meow
bitmap, palette = adafruit_imageload.load("/logo.bmp",bitmap=displayio.Bitmap,palette=displayio.Palette)
palette = displayio.Palette(2)
palette[0] = 0xFFFFFF
palette[1] = 0x000000
#Create a TileGrid to hold the bitmap
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
#Create a Group to hold the TileGrid
group = displayio.Group()
#Add the TileGrid to the Group
group.append(tile_grid)
#Add the Group to the Display
display.show(group)

## Set text, font, and color
#text = " "
#font = terminalio.FONT
#color = 0xFFFFFF
#
## Create the text label
#text_area = label.Label(font, text=text, color=color)
#
## Set the location
#text_area.x = 0 + BORDER
#text_area.y = 0 + BORDER
## Show it
#display.show(text_area)
