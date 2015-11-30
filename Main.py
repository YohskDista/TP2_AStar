__author__ = 'leonardo.distasio'

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

def astar(villeA, villeB, heuristique):
    print("astar")

if __name__ == "__main__":

    fileConnections = open("data/connections.txt", "r")
    filePositions = open("data/positions.txt", "r")

    connections = fileConnections.read()
    positions = filePositions.read()

    positionsParse(positions)
    connectionsParse(connections)

    astar("Munich", "Trieste", None)

