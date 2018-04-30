# 2018 Spring 590PR Final Project

# Title: Four-in-row game

## Team Member(s): 

Songwei Feng, Jinlin Zeng, Mingrui Yin, Ni Lin

# Monte Carlo Simulation Scenario & Purpose:

Gomoku:Gomoku is one of the world intelligence games events. It is a purely strategic board game where two players play. Normally, both sides use black and white chess pieces, and they are placed on a straight and horizontal line. At the intersection, the winner of the first five sub-connections was forme.

MCTS: The full name of MCTS is Monte Carlo Tree Search, which is a method for making optimal decisions in artificial intelligence problems, and is generally a form of moving planning in combinational games. It combines the generality of random simulation and the accuracy of tree search.

Our project aims to apply the Monte Carlo Simulation and MCTS into training the machine to how to play Gomoku.

## Simulation's variables of uncertainty

Each step will be a different situation since it will call a MCTS for the decision each time, and the whole game is based on the collections of all MCTS decisions.

## Hypothesis or hypotheses before running the simulation:

Relatively randomness - For any specific situation, the machine will first try blank spot near the stone, then try blank spot further. In our case, the decision is on the basis of the simulation, which is on and only on the basis of randomness.

No human experiences involved - The program contains the idea of Exhaustive Attack method and the spirit of traversal, on the other hand, no human experience of the game is needed.

Decision making - Each possible solution is given appropriate weight for evaluation, and make the final decision; the process of decision making which based on the traversal on the next level(s) is called back propagation.

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

(1) When the board was relatively small (6x6) and we ran a four-in-row game, the algorithm had a good performance. However, when we had a relatively big board and ran a five-in-row game, even if we set a smaller calculation time, the algorithm didn't have a good performance. Based on this finding, we decided to choose the game into four-in-row.

(2) If the first step is made by AI, then the player will 100% lose.

## Instructions on how to use the program:

Run main.py, then there will be a board shows in the run window, choose which one to move the stone first, the player or AI. For the player, input a tuple like (1,1) to put the stone. Then move the stone one by one.The winner will be the one who first has four stones in a row. If there is no place to put a new stone, the game will be draw.

## All Sources Used:

Software: Python 3.6 (PyCharm)

Algorithm: Monte Carlo Tree Search

## References:

(1) Jeff Bradberry “Introduction to Monte Carlo Tree Search”,Github. https://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/.

(2) Gelly, S., & Silver, D. (2011). Monte-Carlo tree search and rapid action value estimation in computer Go. Artificial Intelligence, 175(11), 1856-1875.

(3) Magnuson, M. (2015). Monte Carlo Tree Search and Its Applications. Scholarly Horizons: University of Minnesota, Morris Undergraduate Journal, 2(2), 4.
