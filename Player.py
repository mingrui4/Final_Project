'''
    Player.py
    Operation form players, including movement of the stone.
'''

class Human(object):
    """
    human player
    """

    def __init__(self, board, player):
        self.board = board
        self.player = player

    def get_action(self, location):
        try:
            move = self.board.location_to_move(location)
        except Exception as e:
            move = -1
        if move == -1 or move not in self.board.availables:
            print("Invalid move")
        return move

    def __str__(self):
        return "Human"