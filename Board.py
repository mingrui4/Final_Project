"""
    Board.py
    Create a board to play the game. Via data from Player.py and MCTS.py to put the stone.
"""

class Board(object):

    def __init__(self, width=6, height=6, n_in_row=4):
        self.width = width
        self.height = height
        self.states = {} # board states, key:move, value: player as piece type
        self.n_in_row = n_in_row # need how many pieces in a row to win

    def init_board(self):
        if self.width < self.n_in_row :
            raise Exception('board width can not less than %d' % self.n_in_row)

        if self.height < self.n_in_row:
            raise Exception('board height can not less than %d' % self.n_in_row)

        self.blanks = list(range(self.width * self.height)) # available moves

        self.states = {} # key:move as location on the board, value:player as pieces type

    def stone_to_position(self, stone):
        """
        transfer stone move to position
        3*3 board's moves like:
        6 7 8
        3 4 5
        0 1 2
        and move 7's location is (2,1)
        """
        h = stone // self.width
        w = stone % self.width
        return [h, w]

    def position_to_stone(self, position):
        """
        transfer position to stone move
        """
        if len(position) != 2:
            stone = -1
            return stone
        h = position[0]
        w = position[1]
        stone = h * self.width + w
        if stone not in self.blanks:
            stone = -1  # -1 means the current position is blank.
        return stone

    def update(self, player, stone):
        """
        update the board
        """
        self.states[stone] = player
        self.blanks.remove(stone)

    def current_state(self):
        return tuple((m, self.states[m]) for m in sorted(self.states))   # for hash