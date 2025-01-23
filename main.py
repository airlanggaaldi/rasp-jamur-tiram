from machine import Pin, SoftI2C
from time import sleep
import dht
import asyncio
import network
from fix.pico_i2c_lcd import I2cLcd
import urequests as requests
import ujson

sistem = "on"
dht_error = False
post_error = False
connecting = True
is_connect = False

pin_mistmaker = 2
pin_kipas = 3
pin_dht = 4
pin_lcd_sda = 6
pin_lcd_scl = 7
pin_soil = 5

set_mistmaker = "Mati"
set_kipas = "Mati"
temp = 0
hum = 0

# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = SoftI2C(sda=Pin(pin_lcd_sda), scl=Pin(pin_lcd_scl), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.putstr("Jamur Tiram")
sleep(1)

async def main():
      asyncio.create_task(main_dht())
      if (dht_error == False):
            asyncio.create_task(mist_maker())
            asyncio.create_task(kipas())
      asyncio.create_task(post())
      asyncio.create_task(print_lcd())

async def mist_maker():
#     print("mist cek")
    global hum
    global set_mistmaker
    relay = Pin(pin_mistmaker, Pin.OUT)

    while True:
        if hum < 80: #80
              # on
              relay.value(0)
              set_mistmaker = "Menyala"
        else:
              # off
              relay.value(1)
              set_mistmaker = "Mati"
        print("Mist: ", set_mistmaker)
        await asyncio.sleep(1)

async def kipas():
#     print("kipas cek")\
    global temp
    global set_kipas
    relay = Pin(pin_kipas, Pin.OUT)

    while True:
        if temp > 30: # 30
              # on
              relay.value(0)
              set_kipas = "Menyala"
        else:
              # off
              relay.value(1)
              set_kipas = "Mati"
        print("Kipas: ", set_kipas)
        await asyncio.sleep(1)

async def main_dht():
      global dht_error
      sensor = dht.DHT11(Pin(pin_dht))
      while True:
            try:
                  sensor.measure()
                  dht_error = False
                  global temp
                  global hum
                  temp = sensor.temperature()
                  hum = sensor.humidity()
                  print('Temperature: %3.1f C' %temp)
                  print('Humidity: %3.1f %%' %hum)
            except OSError as e:
                  print('Failed to read sensor.')
                  print(e)
                  dht_error = True

            await asyncio.sleep(1)

def connect_wifi():
      global connecting
      global is_connect
      connecting = True
      is_connect = False

      # while is_connect == False:
      # ssid = 'RB750GR3'
      # password = '11223344556677888'
      ssid = 'air'
      password = 'ranggabaikhati'

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
            is_connect = False
      else:
            print('Connection successful!')
            network_info = wlan.ifconfig()
            print('IP address:', network_info[0])
            is_connect = True
            connecting = False
#       return is_connect

async def post():
      global is_connect
      global post_error
      while True:
            try:
                  if (is_connect == False):
                      while is_connect == False:
                            connect_wifi()
                            sleep(2)

                  ip = '192.168.170.198'

                  # set temperature
                  data = ujson.dumps({ 'suhu': round(temp, 3), 'kelembapan': hum, 'status_kipas': set_kipas, 'status_mist_maker': set_mistmaker })
                  # print(data)

                  # Make GET request
                  response = requests.post(
                        f"http://{ip}:8000/api/monitoring",
                        headers = {'content-type': 'application/json'},
                        data= data,
                        timeout=10
                  )

                  # Get response code
                  response_code = response.status_code
                  # Get response content
                  response_content = response.content
                  # Print results
                  print('Response code: ', response_code)
                  print('Response content:', response_content)
                  post_error = False
            except OSError as e:
                  print("OS Error:", e)
                  is_connect = False
                  post_error = True
            await asyncio.sleep(2)

async def print_lcd():
      global dht_error
      while True:
            if(dht_error == True):
                  lcd.clear()
                  lcd.putstr("ERROR DHT...")
                  sleep(1)
            else:
                  lcd.clear()
                  lcd.putstr("Temp: %3.1f C" %temp)
                  lcd.move_to(0, 1)
                  lcd.putstr("Hum: %3.1f %%" %hum)
                  sleep(1)
            
            if(post_error == True):
                  if(connecting == True):
                      lcd.clear()
                      lcd.putstr("Connecting...")
                      sleep(1)
                  else:
                      lcd.clear()
                      lcd.putstr("ERROR POST...")
                      sleep(1)
                  
            await asyncio.sleep(1)

# Run main event
loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()


