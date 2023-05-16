#!/usr/bin/env python3
# coding: utf8

from time import sleep
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D17)
# dhtDevice = adafruit_dht.DHT11(board.D18)
# dhtDevice = adafruit_dht.DHT11(board.D18, use_pulseio=False)

print('开始读取温湿度 🌡 💦')

# once
def once():
  try:
    temperature_c = dhtDevice.temperature
    temperature_f = temperature_c * (9 / 5) + 32
    humidity = dhtDevice.humidity
    # print("Temperature: {:.1f} °F / {:.1f} °C".format(temperature_f, temperature_c))
    print("🌡 华氏温度 Temperature: {:.1f} °F ".format(temperature_f))
    print("🌡 摄氏温度 Temperature: {:.1f} °C".format(temperature_c))
    print("💦 湿度 Humidity: {}% ".format(humidity))
  except KeyboardInterrupt:
    print('Ctrl + C 退出 ✅')
  except RuntimeError as error:
    print("error =", error, error.args[0])
    pass
  except Exception as error:
    # dhtDevice.exit()
    raise error
  finally:
    sleep(2.0)
    dhtDevice.exit()
    # cleanup
    print('clear 🚀')

# infinite loop
def infinite():
  while True:
    try:
      temperature_c = dhtDevice.temperature
      temperature_f = temperature_c * (9 / 5) + 32
      humidity = dhtDevice.humidity
      # print("Temperature: {:.1f} °F / {:.1f} °C".format(temperature_f, temperature_c))
      print("🌡 华氏温度 Temperature: {:.1f} °F ".format(temperature_f))
      print("🌡 摄氏温度 Temperature: {:.1f} °C".format(temperature_c))
      print("💦 湿度 Humidity: {}% ".format(humidity))
    except KeyboardInterrupt:
      print('Ctrl + C 退出 ✅')
    except RuntimeError as error:
      print("error =", error, error.args[0])
      pass
    except Exception as error:
      # dhtDevice.exit()
      raise error
    finally:
      sleep(2.0)
      dhtDevice.exit()
      # cleanup
      print('clear 🚀')

once()
# infinite()

"""
https://www.cnblogs.com/xgqfrms/p/17406481.html

https://stackoverflow.com/questions/74167188/get-rid-of-lost-access-to-message-queue-in-a-simple-python-script/76264450#76264450

"""
