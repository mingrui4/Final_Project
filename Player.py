"""
    Player.py
    This class defines the operation for human players, including movement of the stone.
"""

class Player(object):

    def __init__(self, board, player):
        self.board = board
        self.player = player

    def human_action(self):
        """
        ask player to input the position to put the stone
        :return: integer
        """
        try:
            user_input = input("Your move: ").split(",")
            position = [int(step, 10) for step in user_input]
            put_stone = self.board.position_to_stone(position)
        except:
            put_stone = -999
        while True:
            if put_stone == -999 or put_stone not in self.board.blanks:
                user_input = input("This is a invalid move, please enter again!(x,x)\n")
                position = [int(step, 10) for step in user_input]
                put_stone = self.board.position_to_stone(position)
            return put_stone



    def __str__(self):
        return "Human"
