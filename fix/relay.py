from machine import Pin # type: ignore
from time import sleep

# ESP32 GPIO 26
relay = Pin(3, Pin.OUT)

# ESP8266 GPIO 5
#relay = Pin(5, Pin.OUT)

while True:
  # RELAY ON
  print('nyala')
  relay.value(0)
  sleep(5)
  # RELAY OFF
  print('mati')
  relay.value(1)
  sleep(5)