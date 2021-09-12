#Aquí va el punto 4

"""
Considere el problema de navegar en un laberinto que se puede representa como un arreglo
bidimensional. En el laberinto existen algunas celdas que se consideran obstáculos y no es posible
atravesarlas. Inicialmente un agente que se encuentra en una celda específica del laberinto puede moverse
a cualquiera de las 8 direcciones adyacentes siempre y cuando la celda no sea un obstáculo y no esté por
fuera de los límites del laberinto. En este caso, podemos representar la posición del agente como una
coordenada (x, y). Por ejemplo, la coordenada (4,2). Adicionalmente, las acciones posibles pueden
representarse como conjunto de parejas (dx, dy) en el cual dx representa la variación de la posición en
x y dy representa la variación de la posición en y. Por ejemplo, (0,-1) representa dejar la coordenada x
tal como está y disminuir la actual coordenada en y en una unidad. A continuación, se presenta un ejemplo
de un posible laberinto
"""
import random 
from PriorityQueue import Stack,Queue

def generateObstacles(number=5):
    tuples=[]
    i=0
    while (i<number):
        if(number >34):
            return None     
        rand = (random.randint(0, 5), random.randint(0,5))
        if rand not in tuples and rand not in [(0,0), (5,5)]:
            tuples.append(rand)
            i+=1
        else:
            i-=1
    return tuples

class Problem():
    def __init__(self,initialState,desiredState,obstaculos,tablero):
        self.initialState = initialState
        self.desiredState = desiredState
        self.obstaculos = obstaculos
        self.tablero = tablero
    def isGoal(self,state):
        return state==self.desiredState
    def getActions(self,state):
        #Obtener los movimientos S segun el estado A
        actions = [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
        allow_action = []
        for action in actions :
            dx,dy = action
            nx,ny = state[0]+dx,state[1]+dy
            new_State =(nx,ny)
            if (new_State not in self.obstaculos and nx < len(self.tablero[0]) and ny < len(self.tablero[0]) and nx >= 0 and ny >= 0) :
                allow_action.append((dx,dy))
        return allow_action
    def expand(self, state):
        childs = []
        actions = self.getActions(state)
        for action in actions:
            new_c = self.transition(state,action)
            childs.append((new_c, action))
        return childs
    def transition(self,state,action):
        new_state = (state[0]+action[0],state[1]+action[1])
        return new_state

maze = []
obsList = []
for i in range (6):
    maze.append([])
    for j in range (6):
        maze[i].append((i,j))

obsList = generateObstacles(7)

def search(problem,frontier):
    initialState = problem.initialState
    root = (initialState, [])  
    frontier.push(root)
    explored = []

    while not frontier.isEmpty():
        current_state, path = frontier.pop()
        if problem.isGoal(current_state):
            return path        
        if current_state not in explored:
            explored.append(current_state)
            for new_state,action in problem.expand(current_state):
                frontier.push((new_state, path + [action]))
    return None

problema = Problem((5,5),(0,0),obsList,maze)
print(search(problema,Queue()))