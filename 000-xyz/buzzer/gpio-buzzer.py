#!/usr/bin/env python3
# coding: utf8

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PIN = 17
# 有源蜂鸣器，低电平触发
buzzer = GPIO.setup(PIN, GPIO.OUT)
print('🔔 buzzer =', buzzer)
# 🔔 buzzer = None

# print('GPIO.RPI_INFO =', GPIO.RPI_INFO)
# print('GPIO.VERSION =', GPIO.VERSION)
# P17_value = GPIO.gpio_function(17)
# print('GPIO.gpio_function(17) =', P17_value)

print('开始鸣叫 🔔')
try:
  for i in range(3):
    print('鸣叫 ✅', i)
    # buzzer.off()
    # buzzer.value(0)
    GPIO.output(PIN, GPIO.LOW)
    sleep(1)
    # buzzer.on()
    # buzzer.value(1)
    GPIO.output(PIN, GPIO.HIGH)
except KeyboardInterrupt:
  print('鸣叫 ❌')
finally:
  GPIO.cleanup()
  print('结束鸣叫 🔔')


"""
https://www.cnblogs.com/xgqfrms/p/17404551.html

https://github.com/xgqfrms/Raspberry-Pi/tree/master/Python
"""
