"""
    main.py
    Call functions in Board.py, Player.py, MCTS.py to implement the whole game.
    Implemented the basic UI for the game.
"""

from Player import Player
from MCTS import MCTS
from Board import Board


class Game:
    def __init__(self, board, n_in_row=4, time=5.0, max_iteration=1000, model_choice=True):
        """
        initialize the variables of the game
        :param board:
        :param n_in_row: default as 4
        :param time: default as 5.0
        :param max_iteration: default as 1000
        :param model_choice: default as True, True: use MCTS model; False: use dumb model
        """
        self.board = board
        self.player = [1, 2]  # display the human and ai players as player1 and player2
        self.n_in_row = n_in_row
        self.time = time
        self.max_iteration = max_iteration
        self.model_choice = model_choice

    def init_player(self):
        """
        Ask the human player to choose whether to play first. Initialize and return the player turn.
        :return: list
        """
        choice = input("Do you want to play first?(y/n) \n")
        if choice.lower() == 'y':
            return [2, 1]    # human player is player2 and play first
        elif choice.lower() == 'n':
            return [1, 2]    # AI play first
        else:
            print("Please input y or n ! \n")
            play_turn = self.init_player()
            return play_turn

    def init_game(self):
        """
        This the main function to control the process of the game. Call other functions to initialize the game and
        play by turn until the game end situation is met.
        :return:
        """
        # initialize the player and board
        play_turn = self.init_player()
        self.board.init_board()

        ai = MCTS(self.board, [1, 2], self.n_in_row, self.time, self.max_iteration, self.model_choice)
        human = Player(self.board, 2)
        players = {}
        players[1] = ai  # store AI as value in player1
        players[2] = human  # store human as value in player2

        # implement the basic UI for the board and display the game
        self.draw_board(self.board, human, ai)
        while True:
            current_p = play_turn.pop(0)  # get the current player
            play_turn.append(current_p)
            player_in_turn = players[current_p]

            # get the actions of human and ai
            if str(player_in_turn) == 'Human':
                print('Now is your turn :')
                move = player_in_turn.human_action()
            else:
                print('Now is AI turn :')
                move = player_in_turn.action()

            self.board.update(current_p, move)   # update the board
            self.draw_board(self.board, human, ai)  # display the update

            # judge whether to end the game after each step
            result, winner = self.game_end(ai)
            if result:
                if winner != -1:
                    if str(players[winner]) == 'Human':
                        print('Congratulations! You Win!')
                    else:
                        print("Game end. You Lose!")
                break

    def compare_MCTS_Random(self):
        """
        This function is for comparision of MCTS ai and Random ai
        :return:
        """
        # initialize the player and board
        play_turn = [1, 2]
        self.board.init_board()

        ai_M = MCTS(self.board, [1, 2], self.n_in_row, self.time, self.max_iteration, self.model_choice)
        ai_R = MCTS(self.board, [2, 1], self.n_in_row, self.time, self.max_iteration, model_choice=False)
        print(ai_M, ai_R)

        players = {}
        players[1] = ai_M  # store MCTS AI as value in player1
        players[2] = ai_R  # store Random AI as value in player2

        # implement the basic UI for the board and display the game
        self.draw_board_compare(self.board, ai_R, ai_M)
        while True:
            current_p = play_turn.pop(0)  # get the current player
            play_turn.append(current_p)
            player_in_turn = players[current_p]

            # get the actions of the two ai
            if str(player_in_turn) == 'Random':
                print('Random turn :')
                move = player_in_turn.action()
            else:
                print('MCTS turn :')
                move = player_in_turn.action()

            self.board.update(current_p, move)  # update the board
            self.draw_board_compare(self.board, ai_R, ai_M)  # display the update

            # judge whether to end the game after each step
            result, winner = self.game_end(ai_M)
            if result:
                if winner != -1:
                    if winner == 1:
                        print('The winner is: MCTS AI!')
                    else:
                        print('The winner is the Random AI!')
                break


    def compare_MCTS(self):

        play_turn = [1, 2]
        self.board.init_board()

        MCTS1 = MCTS(self.board, [1, 2], self.n_in_row, self.time, self.max_iteration, self.model_choice)
        MCTS2 = MCTS(self.board, [2, 1], self.n_in_row, self.time, self.max_iteration, self.model_choice)
        print(MCTS1, " vs ", MCTS2)

        players = {}
        players[1] = MCTS1  # store MCTS AI as value in player1
        players[2] = MCTS2  # store Random AI as value in player2

        # implement the basic UI for the board and display the game
        self.draw_board_compare_MCTS(self.board, MCTS1, MCTS2)
        i = 0
        while True:
            current_p = play_turn.pop(0)  # get the current player
            play_turn.append(current_p)
            player_in_turn = players[current_p]
            # get the actions of the two ai
            if i % 2 == 0:
                print('MCTS1 turn :')
                move = player_in_turn.action()
                i = i + 1
            else:
                print('MCTS2 turn :')
                move = player_in_turn.action()
                i = i + 1

            self.board.update(current_p, move)  # update the board
            self.draw_board_compare_MCTS(self.board, MCTS1, MCTS2)  # display the update

            # judge whether to end the game after each step
            result, winner = self.game_end(MCTS1)
            if result:
                if winner != -1:
                    if winner == 1:
                        print('The winner is MCTS1!')
                    else:
                        print('The winner is MCTS2!')
                break


    def game_end(self, ai):
        """
        Get the result of the game and the winner.
        :param ai:
        :return: Boolean, Integer
        """
        has_win, winner = ai.winner(self.board)
        if has_win:
            return True, winner
        elif not len(self.board.blanks):
            print("No Spaces. Tie!")
            return True, -1
        return False, -1

    def draw_board(self, board, human, ai):
        """
        Implemented the basic display of the board and moves.
        :param board:
        :param human:
        :param ai:
        :return:
        """
        width = board.width
        height = board.height
        print("Player 1: AI player -- A \n")
        print("Player 2: Human player -- H \n")
        for x in range(width):
            print("{0:8}".format(x), end='')
        print('\r\n')
        for i in range(height - 1, -1, -1):
            print("{0:4d}".format(i), end='')
            for j in range(width):
                position = i * width + j
                player = board.states.get(position, -1)
                if player == human.player:
                    print('H'.center(8), end='')
                elif player == ai.player:
                    print('A'.center(8), end='')
                else:
                    print('.'.center(8), end='')
            print('\r\n\r\n')

    def draw_board_compare(self, board, ai_r, ai_m):
        """
        Implemented the basic display of the board and moves for the compare.
        :param board:
        :param ai_r:
        :param ai_m:
        :return:
        """
        width = board.width
        height = board.height
        print("Player 1: MCTS AI player -- M \n")
        print("Player 2: Random AI player -- R \n")
        for x in range(width):
            print("{0:8}".format(x), end='')
        print('\r\n')
        for i in range(height - 1, -1, -1):
            print("{0:4d}".format(i), end='')
            for j in range(width):
                position = i * width + j
                player = board.states.get(position, -1)
                if player == ai_r.player:
                    print('R'.center(8), end='')
                elif player == ai_m.player:
                    print('M'.center(8), end='')
                else:
                    print('.'.center(8), end='')
            print('\r\n\r\n')

    def draw_board_compare_MCTS(self, board, MCTS1, MCTS2):
        """
        Implemented the basic display of the board and moves for the compare.
        :param board:
        :param MCTS1:
        :param MCTS2:
        :return:
        """
        width = board.width
        height = board.height
        print("Player 1: MCTS1 AI player -- M \n")
        print("Player 2: MCTS2 AI player -- N \n")
        for x in range(width):
            print("{0:8}".format(x), end='')
        print('\r\n')
        for i in range(height - 1, -1, -1):
            print("{0:4d}".format(i), end='')
            for j in range(width):
                position = i * width + j
                player = board.states.get(position, -1)
                if player == MCTS2.player:
                    print('N'.center(8), end='')
                elif player == MCTS1.player:
                    print('M'.center(8), end='')
                else:
                    print('.'.center(8), end='')
            print('\r\n\r\n')


def board_input():
    """
    Ask the human player to input the expected board size where width is equals to height.
    :return: Integer
    """
    board_width = input("Please input the width/height of the board, the length need to be larger than 4\n")
    if not board_width.isdigit() or int(board_width) <= 4:
        print("Invalid input! Please enter again!")
        board_width = board_input()
        return board_width
    return int(board_width)

def compare_input():
    compare = input("a. Do you want to compare MCTS and Random? \n"
                    "b. Do you want to compare two MCTS AI? \n"
                    "c. Start Your Own Game \n"
                    "Please choose (a/b/c) \n")

    return compare

if __name__ == '__main__':

    print("Welcome to Four-In-Row!")
    compare = compare_input()
    while compare.lower() == 'y':
        width = board_input()
        height = width
        n_in_row = 4
        # start the game
        game_board = Board(width, height, n_in_row)
        game = Game(game_board)
        game.compare_MCTS_Random()
        compare = 'n'

    print('Now start your own game!')
    # init the the game board with width and height
    width = board_input()
    height = width
    n_in_row = 4
    # start the game
    game_board = Board(width, height, n_in_row)
    game = Game(game_board)
    game.init_game()




