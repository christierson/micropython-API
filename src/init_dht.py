
import dht
from src.pins import SENSOR


def sensor_read():
    SENSOR.measure()
    return SENSOR.temperature(), SENSOR.humidity()