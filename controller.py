from time import sleep
from threading import Thread, Lock
from datetime import datetime
from boardconfig import BOARD, FREQ

T = 1/FREQ


LAMP = BOARD.get_pin('d:9:p')
FAN = BOARD.get_pin('d:10:p')


class PWM(Thread):
    def __init__(self, pin, curve = lambda x: x) -> None:
        self.lock = Lock()
        self.value = 0
        self.pin = pin
        self.curve = curve
        self.running = False
        self.t0 = datetime.now()
        return super().__init__()
        
    def run(self) -> None:
        with self.lock:
            self.running = True
        while self.running:
            diff = (datetime.now() - self.t0).total_seconds()
            if diff < T:
                sleep(T - diff)
            self.pin.write(self.value)
            self.t0 = datetime.now()

    def set(self, value:float) -> None:
        if 0<=value<=1:
            with self.lock:
                self.value = 1-self.curve(value)
                # self.value = self.curve(1-value)
                
    def join(self, timeout: float) -> None:
        with self.lock:
            self.running = False
        return super().join(timeout)

class Lamp(PWM):
    def __init__(self) -> None:
        super().__init__(LAMP, curve=lambda x: x)
        
if __name__ == "__main__":
    lamp = Lamp()
    lamp.start()
    print("Controller started")
    while True:
        value = input("Enter value 0-100: ")
        if not value.isnumeric():
            break
        lamp.set(float(value)/100)
    print("Controller stopped")
    lamp.set(0)
    lamp.join(1)
    print("Controller joined")
    BOARD.exit()
    print("Board exited")
    print("Exiting...")