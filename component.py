import time
from machine import Pin, PWM
from dht import DHT22


class Component:
    def __init__(self, pin_number, name) -> None:
        self.pin_number = pin_number
        self.name = name
        self.pin = Pin(pin_number)
        self.value = 0
        self.init_pin()

    def init_pin(self):
        self.abstract_warning()

    def read(self):
        self.abstract_warning()

    def write(self, value):
        self.abstract_warning()

    def abstract_warning(self):
        print("ABSTRACT CLASS INSTANCIATED")
        print("class Component should not be used directly")
        print("ABSTRACT CLASS INSTANCIATED")

    def __str__(self) -> str:
        return "Pin " + self.pin_number + ": " + self.name


class DHTComponent(Component):
    def init_pin(self) -> None:
        self.pin = DHT22(Pin(self.pin))
        print(f"Created DHT component on pin {self.pin_number}")

    def read(self):
        self.value = self.pin.measure()
        print(f"Reading {self.value} from pin {self.pin_number}")

        return self.value

    def write(self, value):
        print("Cannot write to DHT pin")


class PWMComponent(Component):

    def init_pin(self) -> None:
        self.freq = 5000
        self.value = 0
        self.pin = PWM(Pin(self.pin))
        self.pin.freq(self.freq)
        self.pin.duty_u16(self.value)
        print(
            f"Created PWM component on pin {self.pin_number} (value: 0-1023)")

    def write(self, value):
        self.value = value
        self.pin.duty_u16(value)
        print(f"Wrote {value} to pin {self.pin_number}")

    def read(self):
        print(f"Reading {self.value} from pin {self.pin_number}")
        return self.value


class GPIComponent(Component):
    def init_pin(self) -> None:
        self.pin = Pin(self.pin, Pin.IN)
        print(
            f"Created input component on pin {self.pin_number} (value: 0 or 1)")

    def read(self):
        return self.pin.value()

    def write(self, value):
        print("Cannot write to input pin")


class GPOComponent(Component):
    def init_pin(self) -> None:
        self.pin = Pin(pin, Pin.OUT)
        print(f"Created output component on pin {self.pin_number}")

    def write(self, value):
        self.value = value
        self.pin.value(value)
        print(f"Wrote {value} to pin {self.pin_number}")

    def read(self):
        print(f"Reading {self.value} from pin {self.pin_number}")
        return self.value
