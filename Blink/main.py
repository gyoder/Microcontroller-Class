#
# Blink
# https://wokwi.com/projects/390907451325233153
#
import board
import digitalio
import time

# set up a pin for the LED
led = digitalio.DigitalInOut(board.GP14)
# tell the pin that it is a digital output
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
