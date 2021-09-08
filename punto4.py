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
print(generateObstacles())

class Problem():
    def __init__(self,initialState,desiredState):
        self.initialState = initialState
        self.desiredState = desiredState
    def isGoal(self,state):
        return state==self.desiredState
    def getActions(self, state):
        return []
    def getNextState(self,state,action):
        return ()
    