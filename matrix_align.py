#!/usr/bin/env python

import max7219.led as led
device = led.matrix(cascaded=1)


device.pixel(0, 0, 1, redraw=False)
device.pixel(7, 0, 1, redraw=False)
device.pixel(0, 7, 1, redraw=False)
device.pixel(7, 7, 1, redraw=False)
device.pixel(3, 3, 1, redraw=False)
device.pixel(3, 4, 1, redraw=False)
device.pixel(4, 4, 1, redraw=False)
device.pixel(4, 3, 1, redraw=False)

# set top left hand 4 leds
device.set_byte(0,8,0B10000011)
device.set_byte(0,7,0B00000011)

device.flush()


