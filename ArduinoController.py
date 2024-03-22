from datetime import datetime
from threading import Thread
from time import sleep

class Component:
    def __init__(self, pin):
        self.value = 0
        self.pin = pin

    def write(self):
        self.pin.write(self.value)

    def set(self, value):
        self.value = value

class Controller(Thread):
    def __init__(self, freq) -> None:
        self.T = 1/freq
        self.t0 = datetime.now()
        return super().__init__()

    def run(self):
        self.sleep_T()
        self.cycle()
        self.t0 = datetime.now()

    def sleep_T(self):
        delta = (datetime.now() - self.t0).total_seconds()
        sleep(max(0, self.T - delta))        


    def cycle(self):
        print("You forgot to override the cycle method")
        pass

class ArduinoController(Controller):
    def __init__(self) -> None:
        self.components = []
        return super().__init__(freq=24)

    def add_component(self, component: Component):
        self.components.append(component)

    def cycle(self):
        for component in self.components:
            component.write()

class Program(Thread):
    def __init__(self, component: Component, rate) -> None:
        self.component = component
        self.schedule = []
        return super().__init__(freq=)
    
    def run(self):
        pass

    def cycle(self, index):
        if index > len(self.schedule) - 1:
            return
        self.component.set(self.schedule[index])
        return self.cycle(index + 1)


class Schedule(Program):
    pass

