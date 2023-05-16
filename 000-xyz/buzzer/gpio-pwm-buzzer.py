#!/usr/bin/env python3
# coding: utf8

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

PIN = 18
Hz = 4978
GPIO.setup(PIN, GPIO.OUT)
# 设置 GPIO 18 PIN 为 PWM 输出, PWM 脉冲频率为 4978Hz (2KHz ～ 5KHZ)
pwm = GPIO.PWM(PIN, Hz)
print('🔔 pwm =', pwm)
# 🔔 pwm = <RPi.GPIO.PWM object at 0x7f915fcd10>

print('\n开始鸣叫 🔔')
try:
  # 占空比 / DutyCycle 0.0 ～ 100.0
  pwm.start(0.0)
  pwm.ChangeDutyCycle(50.0)
  sleep(1)
  pwm.stop()
except KeyboardInterrupt:
  print('鸣叫 ❌')
finally:
  GPIO.cleanup()
  print('结束鸣叫 🔔')

"""

GPIO 18(PWM0)
GPIO 12(PWM0)

GPIO 13(PWM1)
GPIO 19(PWM1)

https://pinout.xyz/pinout/pwm

https://pinout.xyz/pinout/pin12_gpio18


`无源蜂鸣器`的特点：

1. 无源内部不带震荡源，所以如果用直流信号无法令其鸣叫。必须用`2K~5K`的方波去驱动它
2. 声音频率可控，可以做出“多来米发索拉西”的效果。(高阶玩家)
3. 在一些特例中，可以和 LED 复用一个控制口

💡: 使用无源蜂鸣器，只要输出不同频率的 PWM 方波(数字信号)，即可发出不同的音符; 不同的音符组合起来就是一个曲子了, 可以用来播放音乐; ✅

模拟信号：连续性
数字信号: 非连续 0 ～ 1

https://www.cnblogs.com/xgqfrms/p/17404551.html


PWM (Pulse Width Modulation) 即 脉冲宽度调制，
是一种利用微处理器的数字输出来控制模拟电路的控制技术。

但是，需要注意的是 BCM2835 芯片只支持`两路` PWM 输出，
12 Pin 脚和 32 Pin 脚对应的都是 channel 1 的 PWM 输出，
即如果这两个 Pin 的功能都选择的是 PWM 输出，则它们输出的 PWM 是完全相同的;
同理 33 Pin脚和 35 Pin脚对应芯片 channel 2 的 PWM 输出;


"""
