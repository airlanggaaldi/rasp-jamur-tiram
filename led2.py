from machine import Pin # type: ignore
import time

# Set up the built-in LED (on GPIO pin 0 for Pico W)
# led2 = Pin(2, Pin.OUT)
led = Pin(2, Pin.OUT)

# while True:
led.on()
time.sleep(2)
led.off()
time.sleep(2)