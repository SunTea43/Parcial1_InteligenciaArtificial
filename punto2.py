#Aquí va el punto 2
"""
    Problema del rompecabezas lineal de 4 piezas
    Implemente la solución óptima mediante el algoritmo de búsqueda de costo uniforme. La
    implementación debe funcionar con cualquier estado inicial

    Contexto:
    Con el ánimo de hacer el juego más interesante usted decide cambiar el costo de cada movimiento y
    propone las siguientes reglas: si la suma de los dos números en las fichas que desea mover es impar, el
    movimiento constará 2 puntos; si es par, entonces constará 1 punto. El objetivo es completar el juego con
    la menor cantidad de puntos posibles.
""" 
from PriorityQueue import PriorityQueue
INITIAL_STATE= '4231' #[1,2,4,3]
DESIRED_STATE= '1234' #[1,2,3,4]

class Problem():
    def __init__(self,initialState,desiredState=DESIRED_STATE):
        self.goal=desiredState
        self.initialState=initialState

    def isGoal(self, state):
        return self.goal==state

    def expand(self, state):
        childs = []
        #print("Evaluo")
        for action in self.getActions(state):
            new_node = self.transition(state, action)
            cost = self.getActionCost(state, action)
            childs.append((new_node, action, cost))
            #print("Action: ",action, "--> " ,new_node,cost)
        return childs

    def getActions(self, state = None):
        return ['I', 'C', 'D']

    def getNextState(self, state, action):
        return ()

    def getActionCost(self, state, action):
        if action == 'I':
            if ((int(state[0]) + int(state[1])) % 2) == 0:
                return 1
            else:
                return 2
        if action == 'C':
            if ((int(state[1]) + int(state[2])) % 2) == 0:
                return 1
        else:
            return 2
        if action == 'D':
            if ((int(state[2]) + int(state[3])) % 2) == 0:
                return 1
        else:
            return 2

    def transition(self, state, action):
        if action == 'I':
            return (state[1] + state[0] + state[2] + state[3])
        if action == 'C':
            return (state[0] + state[2] + state[1] + state[3])
        if action == 'D':
            return (state[0] + state[1] + state[3] + state[2])    


def search(problem):
    frontier = PriorityQueue() #(state, actions, cost)
    root = (problem.initialState, [], 0)  
    frontier.push(root)
    explored = []

    while frontier:
        current_state, path, cost = frontier.pop()
        if problem.isGoal(current_state):
            return ((path,cost))
        if current_state not in explored:
            explored.append(current_state)
        for new_state, action, new_cost in problem.expand(current_state):
            frontier.push((new_state, path + [action], new_cost + cost))
    return None

print("Estado inicial: ", INITIAL_STATE)
print("Estado deseado: ", DESIRED_STATE)
print(search(Problem(INITIAL_STATE, DESIRED_STATE)))
