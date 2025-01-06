from machine import Pin # type: ignore
from time import sleep

# Set up the built-in LED (on GPIO pin 0 for Pico W)
led = Pin("LED", Pin.OUT)

# Turn on the built-in LED
led.on()
led.off()

# while True:
led.on()
sleep(1)
led.off()
# sleep(0.1)
