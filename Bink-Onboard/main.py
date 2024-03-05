#
# Blink Onboard
# https://wokwi.com/projects/391538584375164929
#
import board
import digitalio
import time

# set up onboard LED
led = digitalio.DigitalInOut(board.LED)
# tell the LED that it is output
led.direction = digitalio.Direction.OUTPUT

# main loop
while True:
    # turn the LED on
    led.value = True
    # wait for 0.5 seconds
    time.sleep(0.5)
    # turn the LED off
    led.value = False
    # wait for 0.5 seconds
    time.sleep(0.5)
