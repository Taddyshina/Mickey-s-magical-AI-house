# ghostAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import Agent
from game import Actions
from game import Directions
import random
from util import manhattanDistance
import util

class GhostAgent( Agent ):
    def __init__( self, index ):
        self.index = index

    def getAction( self, state ):
        dist = self.getDistribution(state)
        if len(dist) == 0:
            return Directions.STOP
        else:
            return util.chooseFromDistribution( dist )

    def getDistribution(self, state):
        "Returns a Counter encoding a distribution over actions from the provided state."
        util.raiseNotDefined()

class RandomGhost( GhostAgent ):
    "A ghost that chooses a legal action uniformly at random."
    def getDistribution( self, state ):
        dist = util.Counter()
        for a in state.getLegalActions( self.index ): dist[a] = 1.0
        dist.normalize()
        return dist

class DirectionalGhost( GhostAgent ):
    "A ghost that prefers to rush Pacman, or flee when scared."
    def __init__( self, index, prob_attack=0.8, prob_scaredFlee=0.8 ,depth='2'):
        self.index = index
        self.prob_attack = prob_attack
        self.prob_scaredFlee = prob_scaredFlee
        self.depth = int(depth)
        self.evaluationFunction=self.scoreEvaluationFunction

    def scoreEvaluationFunction(self,state):
        """
          This default evaluation function just returns the score of the state.
          The score is the same one displayed in the Pacman GUI.

          This evaluation function is meant for use with adversarial search agents
          (not reflex agents).
        """
        return state.getScore()
    def getAction( self, state ):
        # Read variables from state
        Ghost_Actions = state.getLegalActions(self.index)

        minimum = float('Inf')
        result = []
        expect=[]

        for action in Ghost_Actions:
            currentMax = self.min_value(state, 1, self.index, self.index)
            if (action != "Stop"):
                expect.append(currentMax)
                result.append(action)
        Sco=min(expect)
        best=[index for index in range(len(expect)) if expect[index]==Sco]
        Index=random.choice(best)


        return result[Index]

    def max_value(self, state,currentDepth, agent,ghost):
        if currentDepth >=self.depth and currentDepth!=1:
            return self.evaluationFunction(state)
        v = float('-Inf')

        for pAction in state.getLegalActions(agent):
            v = max(v,self.min_value(state.generateSuccessor(ghost, pAction), currentDepth,agent, 0))
        return v

    def min_value(self, state,currentDepth, agent,ghost):

        if currentDepth >= self.depth and currentDepth != 1:
            return self.evaluationFunction(state)
        v = float('Inf')

        for pAction in state.getLegalActions(agent):
            v = max(v,self.max_value(state.generateSuccessor(ghost, pAction), currentDepth+1,agent, agent))
        return v
class MiniMaxAgent( GhostAgent):
    "A ghost that prefers to rush Pacman, or flee when scared."
    def __init__( self, index, prob_attack=0.8, prob_scaredFlee=0.8 ,depth='2'):
        self.index = index
        self.prob_attack = prob_attack
        self.prob_scaredFlee = prob_scaredFlee
        self.depth = int(depth)
        self.evaluationFunction=self.scoreEvaluationFunction

    def scoreEvaluationFunction(self,state):
        """
          This default evaluation function just returns the score of the state.
          The score is the same one displayed in the Pacman GUI.

          This evaluation function is meant for use with adversarial search agents
          (not reflex agents).
        """
        return state.getScore()
    def getAction( self, state ):
        # Read variables from state
        Ghost_Actions = state.getLegalActions(self.index)

        minimum = float('Inf')
        result = []
        expect=[]

        for action in Ghost_Actions:
            currentMax = self.min_value(state, 1, self.index, self.index)
            if (action != "Stop"):
                expect.append(currentMax)
                result.append(action)
        Sco=min(expect)
        best=[index for index in range(len(expect)) if expect[index]==Sco]
        Index=random.choice(best)


        return result[Index]

    def max_value(self, state,currentDepth, agent,ghost):
        if currentDepth >=self.depth and currentDepth!=1:
            return self.evaluationFunction(state)
        v = float('-Inf')

        for pAction in state.getLegalActions(agent):
            v = max(v,self.min_value(state.generateSuccessor(ghost, pAction), currentDepth,agent, 0))
        return v

    def min_value(self, state,currentDepth, agent,ghost):

        if currentDepth >= self.depth and currentDepth != 1:
            return self.evaluationFunction(state)
        v = float('Inf')

        for pAction in state.getLegalActions(agent):
            v = max(v,self.max_value(state.generateSuccessor(ghost, pAction), currentDepth+1,agent, agent))
        return v


def betterEvaluationFunctionGhost(currentGameState):

    ghostEval = betterEvaluationFunctionGhost