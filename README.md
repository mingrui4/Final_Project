Create a FORK of this repository to store your code, data, and documentation for the final project. Detailed instructions for this assignment are in the course Moodle site.  The reason I'm asking you to fork this empty repository instead of creating a stand-alone repository is that it will be much easier for me and all students in the course to find all of our projects for code review and for grading. You can even get code review from students in the other section of IS590PR this way.

Even though your fork of this repository shall be public, you'll still need to explicitly add any students on your team as Collaborators in the Settings. That way you can grant them write privileges.

DELETE these lines from TEMPLATE up.

TEMPLATE for your report:

# Title: Four-in-row game

## Team Member(s): 
Songwei Feng, Jinlin Zeng, Mingrui Yin, Ni Lin

# Monte Carlo Simulation Scenario & Purpose:


## Simulation's variables of uncertainty
Each step will be a different situation which will call a MCS for the decision, and the whole game is based on the collabraton of all MCS.

## Hypothesis or hypotheses before running the simulation:
Relatively randomness - For any specific situation, the machine will first try blank spot near the stone, then try blank spot further. In our case, the decision is on the basis of the simulation, which is on and only on the basis of randomness.
No human experiences involved - The program contains the idea of Exhaustive Attack method and the spirit of traversal, on the other hand, no human experience of the game is needed.
Decision making - Each possible solution is given appropriate weight for evaluation, and make the final decision; the process of decision making which based on the traversal on the next level(s) is called back propagation.

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

## Instructions on how to use the program:
Run main.py, then there will be a board shows in the run window, choose which one to move the stone first, the player or AI. For the player, input a tuple like (1,1) to put the stone. Then move the stone one by one. When someone has four stones in a row, then the player will be the winner. If there is no place to put a new stone, the game will be draw.

## All Sources Used:
Software: Python 3.6 (PyCharm)

Algorithm: Monte Carlo Tree Search

## References:
1. Jeff Bradberry “Introduction to Monte Carlo Tree Search”,Github. https://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/.
2. Gelly, S., & Silver, D. (2011). Monte-Carlo tree search and rapid action value estimation in computer Go. Artificial Intelligence, 175(11), 1856-1875.
3. Magnuson, M. (2015). Monte Carlo Tree Search and Its Applications. Scholarly Horizons: University of Minnesota, Morris Undergraduate Journal, 2(2), 4.
