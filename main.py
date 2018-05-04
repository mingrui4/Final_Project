"""
    main.py
    Call other functions to implement the whole game.
    Need to judge when to end the game.
"""

from Player import Player
from MCTS import MCTS
from Board import Board
from random import shuffle


class Game:
    def __init__(self, board, n_in_row = 4, time = 5, max_iteration = 1000):
        self.board = board
        self.player = [1, 2]
        self.n_in_row = n_in_row
        self.time = time
        self.max_iteration = max_iteration

    def init_player(self):
        choice = input("Do you want to play first ?(y/n) \n")
        if choice.lower() == 'y':
            return [2, 1]
        elif choice.lower() == 'n':
            return [1, 2]
        else:
            print("Please input y or n ! \n")
            result = self.init_player()
            return result

    def init_game(self):
        turn = self.init_player()
        self.board.init_board()

        ai = MCTS(self.board, [1,2], self.n_in_row, self.time, self.max_iteration)
        human = Player(self.board, 2)
        players = {}
        players[1] = ai
        players[2] = human

        self.draw_board(self.board, human, ai)
        while True:
            current_p = turn.pop(0)
            turn.append(current_p)
            player_in_turn = players[current_p]

            if str(player_in_turn) == 'Human':
                print('Now is your turn :')
                move = player_in_turn.get_action()
            else:
                print('Now is AI turn :')
                move = player_in_turn.action()
            self.board.update(current_p, move)
            self.draw_board(self.board, human, ai)
            result, winner = self.game_end(ai)
            if result:
                if winner != -1:
                    if str(players[winner]) == 'Human':
                        print('Congratulations! You Win!')
                    else:
                        print("Game end. You Lose!")
                break

    def game_end(self, ai):
        has_win, winner = ai.winner(self.board)
        if has_win:
            return True, winner
        elif not len(self.board.availables):
            print("No Spaces. Tie!")
            return True, -1
        return False, -1

    def draw_board(self, board, human, ai):
        width = board.width
        height = board.height
        print("Human Player", human.player, "with X \n")
        print("AI    Player", ai.player, "with O \n")
        for x in range(width):
            print("{0:8}".format(x), end='')
        print('\r\n')
        for i in range(height - 1, -1, -1):
            print("{0:4d}".format(i), end='')
            for j in range(width):
                loc = i * width + j
                p = board.states.get(loc, -1)
                if p == human.player:
                    print('X'.center(8), end='')
                elif p == ai.player:
                    print('O'.center(8), end='')
                else:
                    print('_'.center(8), end='')
            print('\r\n\r\n')

def iinput():
    width = input("Please input the width and height, the length need to larger than 4\n")
    width = int(width)
    if width <= 4:
        print("Invalid input!")
        width = iinput()
        return width
    return width


if __name__ == '__main__':
    # init the the game board
    width = iinput()
    height = width
    # n_in_row = input('Please input the n_in_row')
    game_board = Board(width, height, n_in_row=4)
    game = Game(game_board)
    game.init_game()





