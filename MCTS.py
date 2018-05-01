'''
    MCTS.py
    Core function. Use MCTS and RAVE to implement the AI.
    For point Ni, UCB = \frac{W_{i}}{N_{i}} + \sqrt{\frac{C \times lnN}{N_{i}}}
    C = 2^0.5
'''
import numpy as np
import time
import copy
class MCTS(object):
    def __init__(self, board, turn, n_in_row=4, time=10.0, max_actions=1000):
        self.board = board
        self.turn = turn
        self.calculation_time = float(time)
        self.max_actions = max_actions
        self.n_in_row = n_in_row

        self.player = turn
        self.confident = np.sqrt(2)
        self.equivalence = 1000
        self.max_depth = 1

        self.plays = {}  # key:(action, state), value:visited times
        self.wins = {}  # key:(action, state), value:win times
        self.plays_rave = {}  # key:(move, state), value:visited times
        self.wins_rave = {}  # key:(move, state), value:{player: win times}

    def action(self):
        if len(self.board.availables) == 1:
            return self.board.availables[0]

        simulations = 0
        begin = time.time()
        while time.time() - begin < self.calculation_time:
            board_copy = copy.deepcopy(self.board)  # simulation will change board's states,
            turn_copy = copy.deepcopy(self.turn)  # and play turn
            self.run_simulation(board_copy, turn_copy)
            simulations += 1

        print("total simulations=", simulations)

        move = self.move()
        location = self.board.move_to_location(move)
        print('Maximum depth searched:', self.max_depth)

        print("AI move: %d,%d\n" % (location[0], location[1]))

        self.delete()

        return move

    def run_simulation(self,board,turn):
        pass

    def move(self):
        """
        choose movement by win percentage
        """
        move = None
        return move

    def delete(self):
        """
        remove paths which not been selected
        """
        length = len(self.board.states)
        for action, state in self.plays:
            if len(state) < length + 2:
                del self.plays[(action, state)]
                del self.wins[(action, state)]

        for move, state in self.plays_rave:
            if len(state) < length + 2:
                del self.plays_rave[(move, state)]
                del self.wins_rave[(move, state)]

    def __str__(self):
        return "AI"