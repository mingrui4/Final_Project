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

        self.plays = {}  # key:(action, state), value:visited times 记录着法参与模拟的次数，键形如(player, move)，即（玩家，落子）
        self.wins = {}  # key:(action, state), value:win times 记录着法获胜的次数

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
        plays = self.plays
        wins = self.wins
        availables = board.availables

        player = self.get_player(turn)

        state_list = []
        winner = -1

        # Simulation
        for t in range(1, self.max_actions + 1):
            # choose one that have max UCB value
            state = board.current_state()
            actions = [(move, player) for move in availables]
            if all(plays.get((action, state)) for action in actions):
                total = 0
                for a, s in plays:
                    if s == state:
                        total += plays.get((a, s)) # N(s)

                UCB =[(wins[(action, state)] /total)+ np.sqrt(self.confident * np.log(total) / total) for action in actions]
                value,action = max(UCB)


            else:
                # choose the nearest blank point
                adjacents = []
                if len(availables) > self.n_in_row:
                    adjacents = self.adjacent(board, state, player, plays)

                if len(adjacents):
                    action = (np.random.choice(adjacents), player)
                else:
                    action = np.random.choice(actions)

                move, p = action
                board.update(player, move)
                state_list.append((action, state))

                #judge whether to break the loop
                full = not len(availables)
                win, winner = self.winner(board)
                if full or win:
                    break

            # Back-propagation
            for i, ((a, s), state) in enumerate(state_list):
                action = (a, s)
                if (action, state) in plays:
                    plays[(action, state)] += 1  # all visited moves
                    if player == winner and player in action:
                        wins[(action, state)] += 1  # only winner's moves


    def adjacent(self, board, state, player, plays):
        """
        adjacent moves
        """
        moved = list(set(range(board.width * board.height)) - set(board.availables))
        adjacents = set()
        width = board.width
        height = board.height

        for m in moved:
            # 3*3 board's moves like:
            # 6 7 8
            # 3 4 5
            # 0 1 2
            # let the stone be 4
            h = m // width
            w = m % width
            if w < width - 1:
                adjacents.add(m + 1)  # 5
            if w > 0:
                adjacents.add(m - 1)  # 3
            if h < height - 1:
                adjacents.add(m + width)  # 7
            if h > 0:
                adjacents.add(m - width)  # 1
            if w < width - 1 and h < height - 1:
                adjacents.add(m + width + 1)  # 8
            if w > 0 and h < height - 1:
                adjacents.add(m + width - 1)  # 6
            if w < width - 1 and h > 0:
                adjacents.add(m - width + 1)  # 2
            if w > 0 and h > 0:
                adjacents.add(m - width - 1)  # 1

        adjacents = list(set(adjacents) - set(moved))
        for move in adjacents:
            if plays.get(((move, player), state)):
                adjacents.remove(move)
        return adjacents

    def get_player(self,turn):
        """
        get players by turn here
        """
        player = None
        return player

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

    def winner(self,board):
        win = None
        winner = None
        return win,winner

    def __str__(self):
        return "AI"