# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details: https://RandomNerdTutorials.com/raspberry-pi-pico-w-http-requests-micropython/

import network
import urequests as requests
import time

# Wi-Fi credentials
# ssid = 'air'
# password = 'ranggabaikhati'
# ssid = 'iPhone (2)'
# password = '11111111'
ssid = 'RB750GR3'
password = '11223344556677888'
# ssid = 'GOLDEN CAFE 2'
# password = 'sosisbakar'
# ssid = 'realme 13+ 5G'
# password = 'i7h2zwmv'

try:
      # Connect to network
      wlan = network.WLAN(network.STA_IF)
      wlan.active(True)

      # Connect to your network
      wlan.connect(ssid, password)
      print("Connected:", wlan.isconnected())
      print("IP Configuration:", wlan.ifconfig())

      # Make GET request
      # ip = '172.20.10.11'
      ip = '192.168.43.19'
      # ip = '192.168.18.16' #golden
      response = requests.get(f"http://{ip}:8000/api/monitoring", timeout=10)
      # Get response code
      response_code = response.status_code
      # Get response content
      response_content = response.content
      # Print results
      print('Response code: ', response_code)
      print('Response content:', response_content)
except OSError as e:
      print("OS Error:", e)
except Exception as e:
      print("General Error:", e)
