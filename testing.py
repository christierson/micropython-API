import requests
import json
from subprocess import check_output, run, DEVNULL, PIPE
# curl -X POST http://192.168.0.102:8080/ -H "Content-Type: application/json" -d '{"key": "value"}


def send_data(data):
    headers = "Content-Type: application/json"
    url = "http://192.168.0.102:8080/"
    data = json.dumps(data)
    command = ["curl", "-X", "POST", url, "-H",
               headers, "-d", data]
    response = run(command, check=True, capture_output=True).stdout
    try:
        response = json.loads(response)
        print(json.dumps(response, sort_keys=True, indent=4))
        return response
    except:
        print("COULD NOT DECODE")
        print(response)


def get_board():
    return send_data({"command": "get_board"})


def read(pin):
    return send_data({"command": "read", "kwargs": {"pin": pin}})


def write(pin, value):
    return send_data({"command": "write", "kwargs": {"pin": pin, "value": value}})


def save_default():
    return send_data({"command": "save_default"})


def load_default():
    return send_data({"command": "load_default"})

def blink():
    return send_data({"command": "blink"})


def set_pin(pin, name, mode):
    return send_data({"command": "set_pin", "kwargs": {
        "pin": pin, "name": name, "mode": mode}})
