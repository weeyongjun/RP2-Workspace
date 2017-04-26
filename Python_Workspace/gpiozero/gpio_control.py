# Basic Python Physical Computing
# Guide - https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/
# Resource - https://gpiozero.readthedocs.io/en/stable/
# Tutorial 1 - Lighting an LED
# Description
# - Make the LED switch on when the button is being held down, and off when button released
# - Two methods of the Button class called when_pressed and when_released.
# - These don't block the flow of the program, so if they are placed in a loop, the program will continue to cycle indefinitely.

from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()
