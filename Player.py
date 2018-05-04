"""
    Player.py
    This class defines the operation for human players, including movement of the stone.
"""

class Player(object):
    """
    human player
    """

    def __init__(self, board, player):
        self.board = board
        self.player = player

    def human_action(self):
        """
        ask player to input the position to put the stone
        :return: integer
        """
        try:
            position = [int(n, 10) for n in input("Your move: ").split(",")]
            put_stone = self.board.location_to_move(position)
        except:
            put_stone = -999
        if put_stone == -999 or put_stone not in self.board.blanks:
            print("This is a invalid move, please enter again!")
            put_stone = self.human_action()
        return put_stone

    def __str__(self):
        return "Human"