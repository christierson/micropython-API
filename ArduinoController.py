from threading import Thread, Lock
from queue import Queue
from datetime import datetime
from time import sleep
from boardconfig import BOARD

LAMP = BOARD.get_pin('d:9:p')
# FAN = BOARD.get_pin('d:10:p')

class Component(Thread):
    def __init__(self, pin, name = "Unknown component"):
        Thread.__init__(self)
        self.queue = Queue()
        self.running = False
        self.pin = pin
        self.name = name
        self.value = 0
        print("Created component", name)

    def run(self):
        if self.queue.empty():
            self.running = False
            return
        delay, value = self.queue.get()
        sleep(delay)
        self.write(self.translate(self.minmax(value)))
        self.run()

    def minmax(self, value):
        return max(0, min(1, value))

    def translate(self, value):
        return value

    def write(self, value):
        print("Writing", value, "to", self.name)
        self.value = value
        self.pin.write(1-value)

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
    
class Lamp(Component):

    def __init__(self):
        self.freq = 32
        return super().__init__(LAMP, name="Lamp")
    
    def fade(self, value, time):
        n = time*self.freq
        diff = value - self.value
        step = diff/n
        delays = [1/self.freq]*(n+1)
        values = [self.value + step*x for x in range(n)] + [value]

        self.schedule(delays, values)
            
