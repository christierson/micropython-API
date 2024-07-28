from component import Component, COMPONENTS
import json
NON_GP = [3, 8, 13, 18, 23, 28, 30, 33, 35, 36, 37, 38, 39, 40]


class Board:
    def __init__(self) -> None:
        self.board = {}
        self.load_default()
        print("Created board")
        self.print_board()

    def available_pins(self):
        return [key for key, value in self.board.items() if value.available]

    def load_default(self):
        try:
            with open("boardconfig.json", "r") as fp:
                default = json.loads(fp.read())
        except:
            print("CREATING NEW DEFAULT FILE")
            self.board = {f"{id}": Component(
                id) for id in range(1, 31) if id not in NON_GP}
            self.save_default()
            return

        for c in default.values():
            C = COMPONENTS[c["type"]]
            instance = C(c["pin"], c["name"])
            self.board[c["pin"]] = instance

    def save_default(self):
        with open("boardconfig.json", "w") as fp:
            fp.write(json.dumps(self.serialize()))
        return "Saved current board"

    def get_board(self):
        return self.serialize()

    def serialize(self):
        d = {n: pin.serialize() for n, pin in self.board.items()}
        print("Serialized:", d)
        return d

    def print_board(self):
        def get_str(p):
            if p in self.board:
                return str(self.board[p])
            return f"{p}: Unavailable"

        for i in range(20):
            pa = i+1
            pb = 40-i
            print(f"{get_str(pa) : <20}{get_str(pb) : <20}")

    def recieve(self, data):
        print(data)
        command = data.get('command')
        if not command:
            raise ValueError("No command provided in the data")
        command_method = getattr(self, command, None)
        if not command_method:
            raise ValueError(f"Command '{command}' not found")
        args = data.get('args', [])
        kwargs = data.get('kwargs', {})
        return command_method(*args, **kwargs)

    def read(self, pin):
        pin = self.board.get(pin)
        if not pin:
            return f"Invalid pin - valid pins: {list(self.board.keys())}"
        return pin.read()

    def write(self, pin, value):
        pin = self.board.get(pin)
        if not pin:
            return f"Invalid pin - valid pins: {list(self.board.keys())}"
        return pin.write(value)

    def set_pin(self, pin, name, mode):
        if pin not in self.board:
            return f"Invalid pin - valid pins: {list(self.board.keys())}"
        if not self.board[pin].available:
            return f"Pin busy - try one of the available ones: {self.available_pins()}"
        mode = COMPONENTS.get(mode)
        if not mode:
            return f"Unknown mode - valid modes: {list(COMPONENTS.keys())}"
        component = mode(pin, name)

        self.board[pin] = component
        return f"Created {str(component)}"

    def help(self):
        return {"Commands": {
            "load_default": {
                "action": "Loads board config from file, creates one if needed"
            },
            "save_default": {
                "action": "Saves the current board setup into config file"
            },
            "help": {
                "returns": "This message"
            },
            "get_board": {
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
