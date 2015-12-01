__author__ = 'leonardo.distasio & kevin.vulliemin'

# frontière : liste des villes à visiter
# historique : liste des villes visitées

from Node import Node

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

        parentNode = dictNodes[word[0]]
        nodeChild = dictNodes[word[1]]

        parentNode.addChild(nodeChild)

        if(word[0] in dictConnectionsQuantity):
            dictConnectionsQuantity[word[0]].update({word[1] : word[2]})
        else:
            dictConnectionsQuantity[word[0]] = {word[1] : word[2]}

def h0(node1, node2):
    print("h0")

def h1(node1, node2):
    print("h1")

def h2(node1, node2):
    print("h2")

def h3(node1, node2):
    print("h3")

def h4(node1, node2):
    print("h4")

def astar(villeA, villeB, heuristique):
    print("astar")
    initNode = dictNodes[villeA]
    endNode = dictNodes[villeB]

    heuristique(initNode, endNode)

if __name__ == "__main__":

    fileConnections = open("data/connections.txt", "r")
    filePositions = open("data/positions.txt", "r")

    connections = fileConnections.read()
    positions = filePositions.read()

    positionsParse(positions)
    connectionsParse(connections)

    astar("Munich", "Trieste", h0)
    astar("Munich", "Trieste", h1)
    astar("Munich", "Trieste", h2)
    astar("Munich", "Trieste", h3)
    astar("Munich", "Trieste", h4)

