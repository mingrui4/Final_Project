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

    def move_to_location(self, move):
        """
        transfer move to location
        3*3 board's moves like:
        6 7 8
        3 4 5
        0 1 2
        and move 7's location is (2,1)
        """
        h = move // self.width
        w = move % self.width
        return [h, w]

    def location_to_move(self, location):
        """
        transfer location to move
        """
        if len(location) != 2:
            move = -1
            return move
        h = location[0]
        w = location[1]
        move = h * self.width + w
        if move not in self.blanks:
            move = -1
        return move

    def update(self, player, move):
        """
        update the board
        """
        self.states[move] = player
        self.blanks.remove(move)

    def current_state(self):
        return tuple((m, self.states[m]) for m in sorted(self.states))  # for hash