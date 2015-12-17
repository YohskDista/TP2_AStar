__author__ = 'leonardo.distasio'

class State:

    def __init__(self, node, quality, parent):
        self.node = node
        self.g = quality
        self.parent = parent

        self.f = 0

    # Fonction de comparaison
    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return self.node.city

    def __contains__(self, item):
        return self.node.city == item.node.city

    # Affichage du chemin avec les enfants
    def printChemin(self):
        par = self
        while(par != None):
            print(par.node.city, end="")
            if(par.parent) : print(" <- ", end="")
            par = par.parent
        print("")

    # Renvoi les enfants du Node
    def getChild(self):
        return self.node.getChild()

    def apply(self, node):
        newState = State(node, self.g, self)
        newState.f = 0

        return newState