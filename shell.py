from ArduinoController import *
lamp = Lamp()
fan=Fan()
heater=Heater()
mister=Mister()
components = [lamp, heater, mister, fan]

def all_on():
    [component.on() for component in components]

def all_off():
    [component.off() for component in components]