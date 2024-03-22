from ArduinoController import *

LAMP = 9
FAN = 10

def main():
    lamp = Component(LAMP)
    fan = Component(FAN)

    controller = ArduinoController()
    controller.add_component(lamp)
    controller.add_component(fan)

    controller.start()

if __name__ == "__main__":
    main()