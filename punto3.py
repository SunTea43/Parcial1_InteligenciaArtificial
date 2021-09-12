from PriorityQueue import Stack,Queue

#Aquí va el punto 3
class Problem():
    def __init__(self,initialState,desiredState):
        self.goal=desiredState
        self.initialState=initialState
    def isGoal(self,state):
        return self.goal==state
    def getActions(self, state):
        """
        Definition that gets all the actions in a specific state.

        Parameters:

        - state: that represents the current state of the game. Its structure is:
         ('Position',#M_l,#C_l,#M_r,#C_r) where 
         Position represents the position of the boat in the river I = left or D=right.
         M and C are the missionaries and cannibals respectively and the indexes are left or right (l or r)

        returns all the actions that are possible in that state 
        """
        actions=[(1,0),(0,1),(1,1),(2,0),(0,2)]
        actions_s=[]
        if state[0]=='I': #Left to right
            for action in actions:
                new_missionaries=state[1]-action[0]
                new_cannibals = state[2]-action[1]
                other_missionaries= state[3]+action[0]
                other_cannibals= state[4]+action[1]
                if(new_missionaries>=0 and new_cannibals>=0 ):
                    if (new_missionaries>=new_cannibals or new_missionaries==0):
                        if(other_missionaries>=other_cannibals or other_missionaries==0):
                            actions_s.append(action)
        else: #Right to left
            for action in actions:
                new_missionaries=state[3]-action[0]
                new_cannibals = state[4]-action[1]
                other_missionaries= state[1]+action[0]
                other_cannibals= state[2]+action[1]
                if(new_missionaries>=0 and new_cannibals>=0):
                    if (new_missionaries>=new_cannibals or new_missionaries==0):
                        if(other_missionaries>=other_cannibals or other_missionaries==0):
                            actions_s.append(action)
        return actions_s
    def getNextState(self,state,action):
        return ()
    def getActionCost(self,state,action):
        return 0
    def transition(self, state, action):
        if(state[0]=="I"):
            new_state=("D",state[1]-action[0],state[2]-action[1],state[3]+action[0],state[4]+action[1])
        else:
            new_state=("I",state[1]+action[0],state[2]+action[1],state[3]-action[0],state[4]-action[1])
        return new_state
    def expand(self, state):
        childs = []
        for action in self.getActions(state):
            new_node = self.transition(state, action)
            childs.append((new_node,action))
        return childs


def search(problem,frontier):
     #(state, actions)
    root = (problem.initialState, [])  
    frontier.push(root)
    explored = []
    while not frontier.isEmpty():
        current_state, path = frontier.pop()
        if problem.isGoal(current_state):
            return path
        if current_state not in explored:
            explored.append(current_state)
            for new_state, action in problem.expand(current_state):
                frontier.push((new_state, path + [action]))
                print(new_state,path+[action])
    return None

DESIRED_STATE=("I",3,3,0,0)
INITIAL_STATE=("D",0,0,3,3)


p=Problem(INITIAL_STATE,DESIRED_STATE)

#solutionBFS=search(p,Queue())
solutionDFS=search(p,Stack())

#print(solutionBFS)
print(solutionDFS)