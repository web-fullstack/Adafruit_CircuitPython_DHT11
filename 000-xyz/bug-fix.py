#!/usr/bin/python3
import sys
import board
import time
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D17)

try:
  # Print the values to the serial port
  temperature_c = dhtDevice.temperature
  temperature_f = temperature_c * (9 / 5) + 32
  humidity = dhtDevice.humidity
  print("%-3.1f " % temperature_c + " " + "%-3.1f " % humidity)
  print(
    "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
      temperature_f, temperature_c, humidity
    )
  )
  # time.sleep(2.0)
except KeyboardInterrupt:
  dhtDevice.exit()
  print("Ctrl + C, exit ✅")
except RuntimeError as error:
  # Errors happen fairly often, DHT's are hard to read, just keep going
  print(error.args[0])
  time.sleep(2.0)
except Exception as error:
  dhtDevice.exit()
  raise error
finally:
  # ✅
  time.sleep(2.0)
  dhtDevice.exit()
  print("clear")

"""
https://www.cnblogs.com/xgqfrms/p/17406481.html

https://stackoverflow.com/questions/74167188/get-rid-of-lost-access-to-message-queue-in-a-simple-python-script/76264450#76264450

"""