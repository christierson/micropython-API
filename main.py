from ArduinoController import *
import math

def main():
    values = [math.sin(x/100) for x in range(100)]
    delays = [0.05]*100
    print(values)
    print(delays)
    lamp = Lamp()
    lamp.set(1)
    sleep(0.5)
    lamp.set(0)
    sleep(0.5)
    lamp.set(1)
    sleep(0.5)
    lamp.set(0)
    # lamp.fade(1, 1)
    # lamp.fade(0, 1)
    # lamp.fade(1, 1)
    # lamp.fade(0, 1)

def points(n):
    return [x/n for x in range(n)]

if __name__ == "__main__":
    main()