__author__ = 'leonardo.distasio'

dictConnections = {}
dictPositions = {}

def positionsParse(positions):
    lines = positions.split("\n")

    for line in lines:
        word = line.split(" ")
        dictPositions[word[0]] = {"x" : word[1], "y" : word[2]}

def connectionsParse(connections):
    lines = connections.split("\n")

    for line in lines:
        word = line.split(" ")

        if(word[0] in dictConnections):
            dictConnections[word[0]].update({word[1] : word[2]})
        else:
            dictConnections[word[0]] = {word[1] : word[2]}

if __name__ == "__main__":

    fileConnections = open("data/connections.txt", "r")
    filePositions = open("data/positions.txt", "r")

    connections = fileConnections.read()
    positions = filePositions.read()

    connectionsParse(connections)
    positionsParse(positions)

