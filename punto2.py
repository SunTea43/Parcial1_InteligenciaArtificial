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

INITIAL_STATE="4321"
DESIRED_STATE="1234"

class Problem():
    def __init__(self,initialState,desiredState=DESIRED_STATE):
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