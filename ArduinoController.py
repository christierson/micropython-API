from threading import Thread, Lock
from queue import Queue
from datetime import datetime
from time import sleep
import math
from boardconfig import BOARD

LAMP = BOARD.get_pin('d:10:p')
FAN = BOARD.get_pin('d:9:p')
HEATER = BOARD.get_pin('d:8:o')
MISTER = BOARD.get_pin('d:7:o')

class Component(Thread):
    def __init__(self, pin, name="Unknown component", min=0, max=1):
        super().__init__()
        self.queue = Queue()
        self.running = False
        self.pin = pin
        self.name = name
        self.min = min
        self.max = max
        self.value = self.min
        print("Created component", name)

    def run(self):
        if self.queue.empty():
            self.running = False
            return
        delay, value = self.queue.get()
        sleep(delay)
        self.write(self.minmax(value))
        self.run()

    def minmax(self, value):
        return max(self.min, min(self.max, value))

    def translate(self, value):
        return value
    
    def set(self, value):
        self.schedule([0], [value])

    def on(self):
        self.set(self.max)
    
    def off(self):
        self.set(self.min)

    def write(self, value):
        self.value = value
        self.pin.write(self.translate(value))

    def schedule(self, delays, values):
        lenght = len(delays)
        if lenght != len(values) or lenght == 0:
            print("Delay and value list mismatch")
            return
        self.running = True
        for i, time in enumerate(delays):
            value = values[i]
            self.queue.put((time, value))
        self.run()
    
    def __str__(self) -> str:
        return self.name
    
class ComponentPWM(Component):

    def __init__(self, pin, name):
        self.freq = 32
        return super().__init__(pin, name)
    
    def fade(self, value, time):
        n = int(time*self.freq)
        diff = value - self.value
        step = diff/n
        delays = [1/self.freq]*(n+1)
        values = [self.value + step*x for x in range(n)] + [value]
        self.schedule(delays, values)
            
    def set(self, value):
        self.fade(value, 0.5)

class Lamp(ComponentPWM):

    def __init__(self):
        super().__init__(LAMP, "Lamp")

class Fan(ComponentPWM):

    def __init__(self):
        super().__init__(FAN, "Fan")

class Heater(Component):

    def __init__(self):
        super().__init__(HEATER, "Heater")

class Mister(Component):

    def __init__(self):
        super().__init__(MISTER, "Mister")

    def toggle(self):
        self.off()
        sleep(1)
        self.on()
        sleep(0.1)
        self.off()