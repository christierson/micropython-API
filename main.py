from api import API
from board import Board
COMMANDS = {
    "help": help,
    # "board": board,
    # "read": read,
    # "write": write,
    # "pin": pin
}


board = Board()
api = API(board.recieve)
# api.run()
