from servo import Servo
from time import sleep

from picozero import pico_temp_sensor

from machine import Pin
import utime

servo=Servo(pin=14)

try:
    led = Pin(5, Pin.OUT)
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
            print("pppp")

        while echo.value() == 1:
            signalon = utime.ticks_us()
                
            timepassed = signalon - signaloff
            distance = (timepassed * 0.0343) / 2
            print("The distance from object is ", distance, "cm")
            print()
            
            if(distance <= 10):
                led.on()
                led_internal.on()
                servo.move(0)
            elif(distance < 100 and distance > 10):
                led.off()
                led_internal.off()
                servo.move(90)
            else:
                led.off()
                led_internal.off()
                servo.move(180)
    while True:
        ultra()
        utime.sleep(0.5)

except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM 
    servo.stop()

# Create a Servo object on pin 0

    
    
#     while True:
#         #Servo at 0 degrees
#         servo.move(0)
#         sleep(2)
#         #Servo at 90 degrees
#         servo.move(90)
#         sleep(2)
#         #Servo at 180 degrees
#         servo.move(180)
#         sleep(2)
        

