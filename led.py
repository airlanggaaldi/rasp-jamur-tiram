# from picozero import RGBLED
# from time import sleep

# rgb = RGBLED(red = 2, green = 3, blue = 1)

# while True:
#     rgb.color = (255, 0, 0)
#     sleep(0.5)
#     rgb.color = (0, 255, 0)
#     sleep(0.5)

from machine import Pin, PWM
from time import sleep

red = PWM(Pin(2))  # Red channel on GPIO pin 26
green = PWM(Pin(3))  # Green channel on GPIO pin 27

red.freq(1000)
green.freq(1000)

def set_color(r, g):
    # Scale 0-255 to 0-65535
    red.duty_u16(int(r * 65535 / 255))
    green.duty_u16(int(g * 65535 / 255))
    
try:
    while True:
        set_color(255,0)  # Red
        sleep(1)
        set_color(0,255)  # Green
        sleep(1)
except KeyboardInterrupt:
    set_color(0, 0)  # Turn off RGB LED on interrupt

# from machine import Pin # type: ignore
# import time

# # Set up the built-in LED (on GPIO pin 0 for Pico W)
# led2 = Pin(2, Pin.OUT)
# led3 = Pin(3, Pin.OUT)

# while True:
#       # Turn on the built-in LED
#       # led2.on()
#       led3.on()
#       time.sleep(2)
#       # led2.off()
#       led3.off()
#       time.sleep(2)