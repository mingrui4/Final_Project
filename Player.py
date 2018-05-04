"""
    Player.py
    Operation form players, including movement of the stone.
"""

class Player(object):
    """
    human player
    """

    def __init__(self, board, player):
        self.board = board
        self.player = player

    def get_action(self):
        try:
            location = [int(n, 10) for n in input("Your move: ").split(",")]
            move = self.board.location_to_move(location)
        except Exception as e:
            move = -1
        if move == -1 or move not in self.board.availables:
            print("invalid move")
            move = self.get_action()
        return move

    def __str__(self):
        return "Human"