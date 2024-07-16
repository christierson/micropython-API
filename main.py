from api import API
from board import Board
COMMANDS = {
    "help": help,
    # "board": board,
    # "read": read,
    # "write": write,
    # "pin": pin
}


def help():
    return {"Commands": {
        "help": {
            "returns": "This message"
        },
        "board": {
            "returns": "The current state of the board config"
        },
        "read": {
            "returns": "The value of a pin",
            "required arguments": {
                "pin": "The pin number for the pin you want to read"
            }
        },
        "write": {
            "action": "Sets the value of a pin",
            "returns": "The value of a pin",
            "required arguments": {
                "pin": "The pin number for the pin you want to write to",
                "value": "The value you want to write"
            }
        },
        "pin": {
            "action": "Sets the name and type for a pin",
            "returns": "The resulting state of the board",
            "required arguments": {
                "pin": "The number of the pin",
                "name": "Pin name for later reference",
                "mode": "Desired component type: {\"INP\": 1, \"OUT\": 2, \"DHT\": 3, \"PWM\": 4}"
            }
        }
    }
    }


def board_controller(board):
    def controller(data):
        print(data)
        command = data["command"]
        return data

    return controller


board = Board()
api = API(controller)
# api.run()
