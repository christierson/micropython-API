from component import PWMComponent, DHTComponent, GPOComponent, GPIComponent

NON_GP = [3, 8, 13, 18, 23, 28, 33, 35, 36, 37, 38, 39, 40]


class Board:
    def __init__(self) -> None:
        self.board = self.default_board()
        print("Created board")
        self.print_board()

    def available_pins(self):
        return [key for key, value in self.board.items() if value == None]

    def default_board(self):
        return {f"{id}": None for id in range(1, 41) if id not in NON_GP}

    def create(self, name, type, pin):
        if self.board[f"{pin}"] != None:
            return f"Pin busy - try one of the available ones: {self.available_pins()}"

        if type in ["INP", 1, "1"]:
            component = GPIComponent(pin, name)
        elif type in ["OUT", 2, "2"]:
            component = GPOComponent(pin, name)
        elif type in ["DHT", 3, "3"]:
            component = DHTComponent(pin, name)
        elif type in ["PWM", 4, "4"]:
            component = PWMComponent(pin, name)

        self.board[f"{pin}"] = component

    def print_board(self):
        for i in range(20):
            print(self.board[f"{i+1}"], "\t\t", self.board[f"{40-i}"])
