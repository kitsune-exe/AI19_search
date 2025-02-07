# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem 
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, 
        (successor, action, stepCost), where 'successor' is a 
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental 
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # 10/10/2019
    Fringe = util.Stack()
    Visited = []
    Fringe.push((problem.getStartState(), []))
    Visited.append(problem.getStartState())

    while not Fringe.isEmpty():
        
        state, action = Fringe.pop()

        for next in problem.getSuccessors(state):

            next_state = next[0]
            next_direction = next[1]
            if next_state not in Visited:
                if problem.isGoalState(next_state):
                    return action + [next_direction]
                else:
                    Fringe.push((next_state, action + [next_direction]))
                    Visited.append(next_state)
            

    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 81]"
    "*** YOUR CODE HERE ***"
    # 10/10/2019
    Fringe = util.Queue()
    Visited = []
    Fringe.push((problem.getStartState(), []))
    
    while not Fringe.isEmpty():
        state, action = Fringe.pop()
        
        for next in problem.getSuccessors(state):
            
            next_state = next[0]
            next_direction = next[1]

            if next_state not in Visited:
                if problem.isGoalState(next_state):
                    return action + [next_direction]
                else:
                    Fringe.push((next_state, action + [next_direction]))
                    Visited.append(next_state)
    #util.raiseNotDefined()


def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    # 21/10/2019
    Fringe = util.PriorityQueue()
    Visited = []
    Fringe.push((problem.getStartState(), [], 0), 
        0 + heuristic(problem.getStartState(), problem))
    (state, action, cost) = Fringe.pop()
    Visited.append((state, cost + heuristic(problem.getStartState(), problem)))

    while not problem.isGoalState(state):
        for next in problem.getSuccessors(state):
            visitedFlag = False
            totalCost = next[2] + cost
            for (visitedState, visitedCost) in Visited:
                if (next[0] == visitedState) and (totalCost >= visitedCost):
                    visitedFlag = True
                    break
            if visitedFlag == False:
                Fringe.push((next[0], action+[next[1]], cost + next[2]),
                    cost + next[2] + heuristic(next[0], problem))
                Visited.append((next[0], cost + next[2]))
        (state, action, cost) = Fringe.pop()
    return action

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
