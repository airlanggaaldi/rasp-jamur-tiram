from machine import Pin
from time import sleep
import dht
import asyncio
import network

sistem = "on"

pin_dht = 2
pin_mistmaker = 3
pin_kipas = 4

set_mistmaker = "Mati"
set_kipas = "Mati"
temp = 0
hum = 0

async def main():
      asyncio.create_task(main_dht())
      asyncio.create_task(kipas())
      asyncio.create_task(mist_maker())

async def mist_maker():
      global set_mistmaker
      relay = Pin(pin_mistmaker, Pin.OUT)

      while True:
            if hum < 80:
                  # on
                  relay.value(0)
                  set_mistmaker = "Menyala"
            else:
                  # off
                  relay.value(1)
                  set_mistmaker = "Mati"
            sleep(3)

async def kipas():
      global set_kipas
      relay = Pin(pin_kipas, Pin.OUT)

      while True:
            if temp > 30:
                  # on
                  relay.value(0)
                  set_kipas = "Menyala"
            else:
                  # off
                  relay.value(1)
                  set_kipas = "Mati"
            sleep(3)

async def main_dht():
      sensor = dht.DHT11(Pin(pin_dht))
      while True:
            try:
                  sleep(2)
                  sensor.measure()
                  global temp
                  global hum
                  temp = sensor.temperature()
                  hum = sensor.humidity()
                  temp_f = temp * (9/5) + 32.0
                  print('Temperature: %3.1f C' %temp)
                  print('Temperature: %3.1f F' %temp_f)
                  print('Humidity: %3.1f %%' %hum)
            except OSError as e:
                  print('Failed to read sensor.')
                  print(e)

def connect_wifi():
      is_connect = False

      while is_connect == False:
            # ssid = 'RB750GR3'
            # password = '11223344556677888'
            ssid = 'GOLDEN CAFE 2'
            password = 'jussemangka'

            # Init Wi-Fi Interface
            wlan = network.WLAN(network.STA_IF)
            wlan.active(True)

            # Connect to your network
            wlan.connect(ssid, password)

            # Wait for Wi-Fi connection
            connection_timeout = 10
            while connection_timeout > 0:
                  if wlan.status() >= 3:
                        break
                  connection_timeout -= 1
                  print('Waiting for Wi-Fi connection...')
                  sleep(1)

            # Check if connection is successful
            if wlan.status() != 3:
                  raise RuntimeError('Failed to establish a network connection')
            else:
                  print('Connection successful!')
                  network_info = wlan.ifconfig()
                  print('IP address:', network_info[0])
                  is_connect = True

# Run main event
loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
