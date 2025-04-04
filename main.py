from machine import Pin
from time import sleep
import dht 

sensor = dht.DHT11(Pin(14))
led_pin=Pin(5,Pin.OUT) #connected with D1
led_pin2=Pin(4,Pin.OUT) #connected with D2
#sensor = dht.DHT22(Pin(14))

while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    if(temp>30):
        led_pin(1)
    if(hum>50):
        led_pin2(1)
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
  except OSError as e:
    print('Failed to read sensor.')