# RPI ST7789


Python library to control an ST7789 TFT LCD display

Designed to work with a ST7789 based 240x240 pixel TFT SPI display.

*Updated to allow spi mode to be set.*

*Some ST7789 display boards have no chip select (cs) pin. The spi mode must be set to 3 for these boards to work.*
*Other boards, including the Pirate Audio boards, work with spi mode set to 0, which is the default for the Pimoroni st7789-python driver.*

*This is an update that allows a mode parameter to be passed to the driver.*

Usage: Create ST7789 LCD display class for a board with no cs pin. For Pirate Audio or boards with a cs pin set mode=0, 
or even delete the "mode=3," line as the default is 0.

```python

import ST7789

disp = ST7789.ST7789(
    port=0,
    cs=ST7789.BG_SPI_CS_FRONT,  
    dc=9,
    rst=25,
    backlight=13,
    mode=3,
    spi_speed_hz=80 * 1000 * 1000
)   

```

Make sure you have the following dependencies:

```

sudo apt-get update
sudo apt-get install python-rpi.gpio python-spidev python-pip python-pil python-numpy
```
Install this library by running:

```
sudo pip3 install Rpi-ST7789
```

# Licensing & History

This library is a modification of a modification of code originally written by Tony DiCola for Adafruit Industries, and modified to work with the ST7735 by Clement Skau.

To create this ST7789 driver, it has been hard-forked from st7735-python which was originally modified by Pimoroni to include support for their 160x80 SPI LCD breakout.

## Modifications include:

* PIL/Pillow has been removed from the underlying display driver to separate concerns- you should create your own PIL image and display it using `display(image)`
* `mode`, `width`, `height`, `rotation`, `invert`, `offset_left` and `offset_top` parameters can be passed into `__init__` for alternate displays
* `Adafruit_GPIO` has been replaced with `RPi.GPIO` and `spidev` to closely align with our other software (IE: Raspberry Pi only)
* Test fixtures have been added to keep this library stable

Pimoroni invests time and resources forking and modifying this open source code, please support Pimoroni and open-source software by purchasing products from them, too!

Adafruit invests time and resources providing this open source code, please support Adafruit and open-source hardware by purchasing products from Adafruit!

Modified from the Pimoroni st7789-python 'Modified from 'Adafruit Python ILI9341' written by Tony DiCola for Adafruit Industries.' written by Clement Skau.

MIT license, all text above must be included in any redistribution
