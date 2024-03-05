#
# Blink Many
# https://wokwi.com/projects/390907969099506689
#
import board
import digitalio
import time

# set up a pin for the Red LED
red_led = digitalio.DigitalInOut(board.GP10)
# tell the pin that it is a digital output
red_led.direction = digitalio.Direction.OUTPUT

# set up a pin for the Green LED and tell the pin that it is a digital output
green_led = digitalio.DigitalInOut(board.GP11)
green_led.direction = digitalio.Direction.OUTPUT

# set up a pin for the Blue LED and tell the pin that it is a digital output
blue_led = digitalio.DigitalInOut(board.GP12)
blue_led.direction = digitalio.Direction.OUTPUT

# main loop
while True:
    # Turn on the LED's 1 at a time
    red_led.value = True
    time.sleep(0.2)
    green_led.value = True
    time.sleep(0.2)
    blue_led.value = True
    time.sleep(0.2)

    # Turn off the LED's 1 at a time
    red_led.value = False
    time.sleep(0.2)
    green_led.value = False
    time.sleep(0.2)
    blue_led.value = False
    time.sleep(0.2)
