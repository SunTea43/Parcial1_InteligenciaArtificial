from PriorityQueue import Stack,Queue
from graphviz import Digraph, Source
#Aquí va el punto 3
class Problem():
    def __init__(self,initialState,desiredState):
        self.goal=desiredState
        self.initialState=initialState
        self.tree = ""
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
    
        for action in actions:
            if(state[0]=='I'): #Left to right
                new_missionaries=state[1]-action[0]
                new_cannibals = state[2]-action[1]
                other_missionaries= state[3]+action[0]
                other_cannibals= state[4]+action[1]
            else: #Right to left
                new_missionaries=state[3]-action[0]
                new_cannibals = state[4]-action[1]
                other_missionaries= state[1]+action[0]
                other_cannibals= state[2]+action[1]
            if(new_missionaries>=0 and new_cannibals>=0 ):
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
    def get_sequence_of_state(self,initial_state, action_sequence):
        sequence = [initial_state]
        for action in action_sequence:
            new_state = self.transition(sequence[-1], action)
            sequence.append(new_state)
        return sequence 

def search(problem,frontier):
     #(state, actions)
    root = (problem.initialState, [])  
    frontier.push(root)
    explored = []
    counter=0
    while not frontier.isEmpty():
        current_state, path = frontier.pop()
        if problem.isGoal(current_state):
            return path
        if current_state not in explored:
            explored.append(current_state)
            posPrev,M_lPrev,C_lPrev,M_rPrev,C_rPrev=current_state
            strNode= posPrev+str(M_lPrev)+ str(C_lPrev)+str(M_rPrev)+str(C_rPrev)
            for new_state, action in problem.expand(current_state):
                pos,M_l,C_l,M_r,C_r = new_state
                strNextNode=pos+str(M_l)+ str(C_l)+str(M_r)+str(C_r)
                if (new_state not in explored and strNextNode not in problem.tree):
                    problem.tree += strNode+'->'+strNextNode+' [label="'+ str(action[0]) +',' +str(action[1])+ '"] \n '
                frontier.push((new_state, path + [action]))
    return None
def add_solution_to_graph(tree, solution):
    """
    Definition thats shows in green color the solution of the problem 

    Parameters:

    - tree: that is an string that represents the expanded tree in graphviz format
    - solution: that is the sequence of states that solves the problem

    taken from: https://colab.research.google.com/drive/1J4BSIxptd2yi0Jtz_7OVJUBG56ZqGDfN?authuser=1#scrollTo=n8LUdC_OpPki
    """
    solution_path = ""
    for state in solution:
        pos,M_l,C_l,M_r,C_r = state
        solution_path += pos+str(M_l)+ str(C_l)+str(M_r)+str(C_r)+ ' [color=green] \n'
    return solution_path + tree


DESIRED_STATE=("I",3,3,0,0)
INITIAL_STATE=("D",0,0,3,3)


pBFS=Problem(INITIAL_STATE,DESIRED_STATE)
pDFS=Problem(INITIAL_STATE,DESIRED_STATE)
solutionBFS=search(pBFS,Queue())
solutionDFS=search(pDFS,Stack())

sequence_of_BFS=pBFS.get_sequence_of_state(INITIAL_STATE,solutionBFS)
sequence_of_DFS=pDFS.get_sequence_of_state(INITIAL_STATE,solutionDFS)

obj=Source("digraph A {" + add_solution_to_graph(pBFS.tree, sequence_of_BFS) + "}")
