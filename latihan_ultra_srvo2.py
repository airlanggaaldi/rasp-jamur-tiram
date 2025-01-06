from servo import Servo
from time import sleep

from picozero import pico_temp_sensor

from machine import Pin, SoftI2C
import utime

from pico_i2c_lcd import I2cLcd

# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# Initialize I2C and LCD objects
i2c = SoftI2C(sda=Pin(7), scl=Pin(6), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

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

        while echo.value() == 1:
            signalon = utime.ticks_us()
                
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
#             text=("The distance from object is ", distance, "cm")
        return distance
    while True:
        distance = ultra()
        distance_str = str(distance)
            text=f"{distance_str}cm"
            print(text)
#             lcd_on(text)
#             print()
            lcd.putstr(text)
            sleep(0.5)
            lcd.clear()
            
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
        utime.sleep(2)

except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM
    lcd.backlight_off()
    lcd.display_off()
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
        


