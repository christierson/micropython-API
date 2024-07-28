from api import API
from board import Board

if __name__ == "__main__":
    board = Board()
    api = API(board.recieve)
    # api.run()
