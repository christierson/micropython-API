from machine import Pin, PWM
from dht import DHT22

SENSOR = DHT22(Pin(22))
AIR = PWM(Pin(15))
# HEAT = PWM(Pin())
# LIGHT = PWM(Pin())
# MIST = Pin()