#Aquí va el punto 3
class Problem():
    def __init__(self,initialState,desiredState):
        self.goal=desiredState
        self.initialState=initialState
    def isGoal(self,state):
        return self.goal==state
    def getActions(self, state):
        return []
    def getNextState(self,state,action):
        return ()
    def getActionCost(self,state,action):
        return 0