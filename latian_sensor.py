from time import sleep
from picozero import pico_temp_sensor

from machine import Pin
import utime

led = Pin(2, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(27, Pin.OUT)
led_internal = Pin("LED", Pin.OUT)

trigger = Pin(20, Pin.OUT)
echo = Pin(21, Pin.IN)

def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    while echo.value() == 0:
        signaloff = utime.ticks_us()

    while echo.value() == 1:
        signalon = utime.ticks_us()
            
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
        print("The distance from object is ", distance, "cm")
        print()
        
        if(distance <= 10):
            led.on()
            led2.off()
            led_internal.on()
            led3.off()
        elif(distance < 100 and distance > 10):
            led.off()
            led2.on()
            led_internal.off()
            led3.off()
        else:
            led.off()
            led2.off()
            led_internal.off()
            led3.on()
while True:
    ultra()
    utime.sleep(0.5)
        
# Convert from celsius to fahrenheit
# def celsius_to_fahrenheit(temp_celsius): 
#     temp_fahrenheit = temp_celsius * (9/5) + 32 
#     return temp_fahrenheit
# 
# while True:
#     # Reading and printing the internal temperature
#     temperatureC = pico_temp_sensor.temp
#     temperatureF = celsius_to_fahrenheit(temperatureC)
# 
#     print("Internal Temperature:", temperatureC, "°C")
#     print("Internal Temperature:", temperatureF, "°F")
#     print()
#     
#     # Wait one second between each reading
#     sleep(3)
