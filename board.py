from component import PWMComponent, DHTComponent, GPOComponent, GPIComponent

NON_GP = [3, 8, 13, 18, 23, 28, 33, 35, 36, 37, 38, 39, 40]


class Board:
    def __init__(self) -> None:
        self.board = self.default_board()
        self.commands = {
            "help": self.help,
            "board": self.board,
            "read": self.read,
            "write": self.write,
            "pin": self.pin,
        }
        print("Created board")
        self.print_board()

    def available_pins(self):
        return [key for key, value in self.board.items() if value == None]

    def default_board(self):
        return {f"{id}": None for id in range(1, 41) if id not in NON_GP}

    def create(self, name, type, pin):
        if self.board[str(pin)] != None:
            return f"Pin busy - try one of the available ones: {self.available_pins()}"

        if type in ["INP", 1, "1"]:
            component = GPIComponent(pin, name)
        elif type in ["OUT", 2, "2"]:
            component = GPOComponent(pin, name)
        elif type in ["DHT", 3, "3"]:
            component = DHTComponent(pin, name)
        elif type in ["PWM", 4, "4"]:
            component = PWMComponent(pin, name)

        self.board[str(pin)] = component

    def print_board(self):
        for i in range(20):
            print(self.board[f"{i+1}"], "\t\t", self.board[f"{40-i}"])

    def recieve(self, data):
        print(data)
        if "command" not in data:
            return f"No command supplied. Format: {'{'}\"command\": \"[{self.commands.keys()}]\", \"args\": {'{}'}{'}'}"
        command = data["command"]
        arguments = data.get("args")
        if command not in self.commands:
            return f"Unrecognized command. Available commands: {self.commands.keys}"

        return self.commands[command]()
        print(f"Doing {data['command']}!")

    def board(self, arguments):
        return "Ran board!"

    def read(self, arguments):
        return "Ran read!"

    def write(self, arguments):
        return "Ran write!"

    def pin(self, arguments):
        return "Ran pin!"

    def help(self, arguments):
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
