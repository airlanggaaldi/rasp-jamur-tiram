# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details: https://RandomNerdTutorials.com/raspberry-pi-pico-w-http-requests-micropython/

import network
import urequests as requests
import time
from picozero import pico_temp_sensor
import ujson
from machine import Pin
import dht

sensor_dht = dht.DHT11(Pin(2))

# Wi-Fi credentials
# ssid = 'air'
# password = 'ranggabaikhati'
# ssid = 'iPhone (2)'
# password = '11111111'
ssid = 'RB750GR3'
password = '11223344556677888'
# ssid = 'UISI 2'
# password = ''
# ssid = 'GOLDEN CAFE 2'
# password = 'sosisbakar'
# ssid = 'realme 13+ 5G'
# password = 'i7h2zwmv'

def get_temperature():
      temperatureC = pico_temp_sensor.temp
      sensor_dht.measure()
      # temperatureC = sensor_dht.temperature()
      # hum = sensor_dht.humidity()
      return temperatureC

try:
      # Connect to network
      wlan = network.WLAN(network.STA_IF)
      wlan.active(True)

      # Connect to your network
      wlan.connect(ssid, password)

      # ip = '192.168.193.19'
      # ip = '172.20.10.11' #akbar
      ip = ' 192.168.43.19' #gutnur
      # ip = '10.1.16.254' #uisi
      # ip = '192.168.18.16' #golden

      while True:
            # set temperature
            temperatureC = get_temperature()
            data = ujson.dumps({ 'suhu': round(temperatureC, 3) })
            print(data)

            # Make GET request
            # response = requests.post(
            #       f"http://{ip}:8000/api/monitoring",
            #       headers = {'content-type': 'application/json'},
            #       data= data,
            #       timeout=10
            # )

            # # Get response code
            # response_code = response.status_code
            # # Get response content
            # response_content = response.content
            # # Print results
            # print('Response code: ', response_code)
            # print('Response content:', response_content)
            time.sleep(5)
except OSError as e:
      print("OS Error:", e)
except Exception as e:
      print("General Error:", e)
