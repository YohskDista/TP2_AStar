__author__ = 'leonardo.distasio & kevin.vulliemin'

# frontière : liste des villes à visiter
# historique : liste des villes visitées

from Node import Node
from State import State
from math import sqrt

dictConnectionsQuantity = {}
dictNodes = {}

def positionsParse(positions):
    lines = positions.split("\n")

    for line in lines:
        word = line.split(" ")
        node = Node(word[0], word[1], word[2])
        dictNodes[word[0]] = node

def connectionsParse(connections):
    lines = connections.split("\n")

    for line in lines:
        word = line.split(" ")

        if(word[0] in dictConnectionsQuantity and word[1] in dictConnectionsQuantity):
            dictConnectionsQuantity[word[0]].update({word[1] : word[2]})
            dictConnectionsQuantity[word[1]].update({word[0] : word[2]})
        else:
            if(word[0] in dictConnectionsQuantity):
                dictConnectionsQuantity[word[0]].update({word[1] : word[2]})
            else:
                dictConnectionsQuantity[word[0]] = {word[1] : word[2]}
            if(word[1] in dictConnectionsQuantity):
                dictConnectionsQuantity[word[1]].update({word[0] : word[2]})
            else:
                dictConnectionsQuantity[word[1]] = {word[0] : word[2]}

def insertChild():
    for city in dictConnectionsQuantity.keys():
        node = dictNodes[city]
        for child in dictConnectionsQuantity[city]:
            node.addChild(dictNodes[child])

def connection(node1, node2):
    return int(dictConnectionsQuantity[node1.city][node2.city])

def h0(node1, node2):
    return 0

def h1(node1, node2):
    return int(node2.x) - int(node1.x)

def h2(node1, node2):
    return int(node2.y) - int(node1.y)

def h3(node1, node2):
    return sqrt((int(node2.x) - int(node1.x))**2 + (int(node2.y) - int(node1.y))**2)

def h4(node1, node2):
    return abs(int(node2.x) - int(node1.x)) + abs(int(node2.y) - int(node1.y))

def astar(villeA, villeB, heuristique):
    initNode = dictNodes[villeA]
    endNode = dictNodes[villeB]

    state0 = State(initNode, 0, None)

    frontiere = [state0]
    history = []

    while frontiere :
        etat = frontiere.pop(0)
        history.append(etat.node)

        if etat.node == endNode:
            return etat

        child = etat.getChild()

        for op in child :
            new = etat.apply(op)
            new.g = new.g + connection(etat.node, new.node)
            new.f = new.g + heuristique(new.node, endNode)

            if (not isInFrontiere(frontiere, new)) and (op not in history):
                frontiere.append(new)

        frontiere.sort()
    return "Pas de solution"

def isInFrontiere(frontiere, state):
    for s in frontiere:
        if s.node.city == state.node.city :
            return True
    return False

def verifyAndPrintHeuristique(state, h):
    if(state != "Pas de solution"):
        print("\nHeuristique %s" % h)
        state.printChemin()
    else:
        print("Pas de solution pour %s" % h)

if __name__ == "__main__":

    fileConnections = open("data/connections.txt", "r")
    filePositions = open("data/positions.txt", "r")

    connections = fileConnections.read()
    positions = filePositions.read()

    positionsParse(positions)
    connectionsParse(connections)
    insertChild()

    ville1 = "Lisbon"
    ville2 = "Munich"

    etat0 = astar(ville1, ville2, h0)
    etat1 = astar(ville1, ville2, h1)
    etat2 = astar(ville1, ville2, h2)
    etat3 = astar(ville1, ville2, h3)
    etat4 = astar(ville1, ville2, h4)

    verifyAndPrintHeuristique(etat0, "H0")
    verifyAndPrintHeuristique(etat1, "H1")
    verifyAndPrintHeuristique(etat2, "H2")
    verifyAndPrintHeuristique(etat3, "H3")
    verifyAndPrintHeuristique(etat4, "H4")

