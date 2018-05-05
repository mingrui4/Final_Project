"""
    MCTS.py
    Core function. Use MCTS and RAVE to implement the AI.
    For point Ni, UCB = \frac{W_{i}}{N_{i}} + \sqrt{\frac{C \times lnN}{N_{i}}}
    C = 2^0.5
"""
import numpy as np
import time
import copy
class MCTS(object):
    def __init__(self, board, turn, n_in_row=4, time=10.0, max_actions=1000, model_choice = True):
        self.board = board
        self.turn = turn # step order
        self.calculation_time = float(time) # maximum operation time.
        self.max_actions = max_actions  # The maximum number of steps in each simulation.
        self.n_in_row = n_in_row

        self.player = turn[0]
        self.confident = np.sqrt(2)
        self.equivalence = 1000
        self.max_depth = 1
        self.model_choice = model_choice

        self.plays = {}  # Record the number of times the method is involved in the simulation.
        #  key:(action, state), value:visited times
        self.wins = {}  # Record the number of wins.
        # key:(action, state), value:win times

    def action(self):
        """
        :return: move
        """
        # If the board has only one final position, then returns directly.
        if len(self.board.blanks) == 1:
            return self.board.blanks[0]

        if self.model_choice:
            simulations = 0
            begin = time.time()
            while time.time() - begin < self.calculation_time:
                board_copy = copy.deepcopy(self.board)  # simulation will change board's states,
                turn_copy = copy.deepcopy(self.turn)  # and play turn
                self.run_simulation(board_copy, turn_copy)
                simulations += 1


            move = self.move()  # choose the best method to move
            location = self.board.stone_to_position(move)

            print("AI puts stone on position: %d,%d" % (location[0], location[1]))
            print("Total simulation times=", simulations)
            print('Maximum depth searched:', self.max_depth, "\n")

            self.delete()

        else:
            board_copy = copy.deepcopy(self.board)
            random = list(set(board_copy.blanks))
            move = np.random.choice(random)
            location = self.board.stone_to_position(move)
            print("AI puts stone on position: %d,%d\n" % (location[0], location[1]))

        return move

    def run_simulation(self, board, turn):
        """
        run the simulation to implement the MCTS
        """
        plays = self.plays
        wins = self.wins
        blanks = board.blanks

        player = self.get_player(turn)

        state_list = []
        winner = -1
        expand = True

        # Simulation
        for t in range(1, self.max_actions + 1):
            # choose one that have max UCB value
            state = board.current_state()
            actions = [(move, player) for move in blanks]
            if all(plays.get((action, state)) for action in actions):
                total = 0
                for a, s in plays:
                    if s == state:
                        total += plays.get((a, s)) # N(s)

                value, action = max(((wins[(action, state)] / total) +
                     np.sqrt(self.confident * np.log(total) / total), action) for action in actions)  # UCB

            else:
                # choose the nearest blank point
                border = []
                if len(blanks) > self.n_in_row:
                    border = self.adjacent(board, state, player, plays)

                if len(border):
                    action = (np.random.choice(border), player)
                # if do not have adajacents,choice a blank randomly
                else:
                    random = list(set(board.blanks))
                    action = (np.random.choice(random),player)

            move, p = action
            board.update(player, move)

            # Expand
            # add only one new child node each time
            if expand and (action, state) not in plays:
                expand = False
                plays[(action, state)] = 0
                # Under the board state, reset the number of simulations of the move from players.
                wins[(action, state)] = 0
                # Under the board state, reset the number of wins of the move from players.

                if t > self.max_depth:
                    self.max_depth = t
            state_list.append((action, state))

            # If there is no blank location or there is a winner, The game is over,
            full = not len(blanks)
            win, winner = self.winner(board)
            if full or win:
                break

            player = self.get_player(turn)

        # Back-propagation
        for i, ((a, s), state) in enumerate(state_list):
            action = (a, s)
            if (action, state) in plays:
                plays[(action, state)] += 1  # all visited moves +1
                if player == winner and player in action:
                    wins[(action, state)] += 1  # only winner's moves +1


    def adjacent(self, board, state, player, plays):
        """
        adjacent moves
        3*3 board's moves like:
        6 7 8
        3 4 5
        0 1 2
        let the stone be 4
        """
        moved = list(set(range(board.width * board.height)) - set(board.blanks))
        border = set()
        width = board.width
        height = board.height

        for m in moved:

            h = m // width
            w = m % width
            if w < width - 1:
                border.add(m + 1)  # 5
            if w > 0:
                border.add(m - 1)  # 3
            if h < height - 1:
                border.add(m + width)  # 7
            if h > 0:
                border.add(m - width)  # 1
            if w < width - 1 and h < height - 1:
                border.add(m + width + 1)  # 8
            if w > 0 and h < height - 1:
                border.add(m + width - 1)  # 6
            if w < width - 1 and h > 0:
                border.add(m - width + 1)  # 2
            if w > 0 and h > 0:
                border.add(m - width - 1)  # 1

        border = list(set(border) - set(moved))
        for move in border:
            if plays.get(((move, player), state)):
                border.remove(move)
        return border

    def get_player(self,turn):
        """
        get players by turn here
        """
        player = turn.pop(0)
        turn.append(player)
        return player

    def move(self):
        """
        Choose the movement with the highest winning rate.
        """
        percent_wins, move = max(
            (self.wins.get(((move, self.player), self.board.current_state()), 0) /
             self.plays.get(((move, self.player), self.board.current_state()), 1),
             move)
            for move in self.board.blanks)
        return move

    def delete(self):
        """
        remove paths which not been selected
        """

        length = len(self.board.states)
        keys = list(self.plays)
        for action, state in keys:
            if len(state) < length + 2:
                del self.plays[(action, state)]
                del self.wins[(action, state)]

    def winner(self,board):
        """
        judge whether there be a winner
        """
        moved = list(set(range(board.width * board.height)) - set(board.blanks))
        if len(moved) < self.n_in_row + 2:
            return False, -1

        width = board.width
        height = board.height
        states = board.states
        n = self.n_in_row
        for m in moved:
            h = m // width
            w = m % width
            player = states[m]

            if (w in range(width - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n))) == 1):
                return True, player

            if (h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * width, width))) == 1):
                return True, player

            if (w in range(width - n + 1) and h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * (width + 1), width + 1))) == 1):
                return True, player

            if (w in range(n - 1, width) and h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * (width - 1), width - 1))) == 1):
                return True, player

        return False, -1

    def __str__(self):
        return "AI"