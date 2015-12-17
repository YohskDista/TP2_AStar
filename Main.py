__author__ = 'leonardo.distasio & kevin.vulliemin'

# frontière : liste des villes à visiter
# historique : liste des villes visitées

from Node import Node
from State import State
from math import sqrt

dictConnectionsQuantity = {}
dictNodes = {}

# Fonction d'analyse du fichier "position.txt"
def positionsParse(positions):
    lines = positions.split("\n")

    for line in lines:
        word = line.split(" ")
        node = Node(word[0], word[1], word[2])
        dictNodes[word[0]] = node

# Fonction d'analyse du fichier "connections.txt"
# Fichier "connections.txt" exemple ligne : "ville1 ville2 distanceVille1Ville2"
def connectionsParse(connections):
    lines = connections.split("\n")

    # Parcours du fichier
    for line in lines:
        word = line.split(" ")

        # Si les villes sont déjà dans le dictionnaire alors on lui rajoute la connexion avec la ville
        if(word[0] in dictConnectionsQuantity and word[1] in dictConnectionsQuantity):
            # Connexion ville 1 (word[0]) à ville 2 (word[1]) avec distance (word[2])
            dictConnectionsQuantity[word[0]].update({word[1] : word[2]})
            # Connexion ville 2 (word[1]) à ville 1 (word[0]) avec distance (word[2])
            dictConnectionsQuantity[word[1]].update({word[0] : word[2]})
        else:
            # Si la ville 1 est dans le dictionnaire on la met à jour
            if(word[0] in dictConnectionsQuantity):
                dictConnectionsQuantity[word[0]].update({word[1] : word[2]})
            # Sinon on l'ajoute au dictionnaire
            else:
                dictConnectionsQuantity[word[0]] = {word[1] : word[2]}
            # Si la ville 2 est dans le dictionnaire on la met à jour
            if(word[1] in dictConnectionsQuantity):
                dictConnectionsQuantity[word[1]].update({word[0] : word[2]})
            # Sinon on l'ajoute au dictionnaire
            else:
                dictConnectionsQuantity[word[1]] = {word[0] : word[2]}

# Création des Node des villes et insertion des enfants
def insertChild():
    for city in dictConnectionsQuantity.keys():
        node = dictNodes[city]
        for child in dictConnectionsQuantity[city]:
            node.addChild(dictNodes[child])

# Distance entre les deux villes
def connection(node1, node2):
    return int(dictConnectionsQuantity[node1.city][node2.city])

# Heuristique 0 : 0
def h0(node1, node2):
    return 0

# Heuristique 1 : position x
def h1(node1, node2):
    return int(node2.x) - int(node1.x)

# Heuristique 2 : position y
def h2(node1, node2):
    return int(node2.y) - int(node1.y)

# Heuristique 3 : distance Euclidienne
def h3(node1, node2):
    return sqrt(h1(node1, node2)**2 + h2(node1, node2)**2)

# Heuristique 4 : distance city-block
def h4(node1, node2):
    return abs(h1(node1, node2)) + abs(h2(node1, node2))

"""
    Fonction algorithme A*

    Paramètres : nom ville A, nom ville B et fonction heuristique
                 à utiliser

    Return : s'il n'y a pas de solution on retourne une String
             sinon on retourne le noeud final pour pouvoir dérouler
                   le chemin inverse
"""
def astar(villeA, villeB, heuristique):
    initNode = dictNodes[villeA]
    endNode = dictNodes[villeB]

    # Création d'un State
    state0 = State(initNode, 0, None)

    # Initialisation frontière et histoire
    frontiere = [state0]
    history = []

    # Parcours des frontières
    while frontiere :
        etat = frontiere.pop(0)
        history.append(etat.node)

        if etat.node == endNode:
            return etat

        child = etat.getChild()

        for op in child :
            new = etat.apply(op)
            new.g = new.g + connection(etat.node, new.node) # Distance entre ville 1 et ville 2
            new.f = new.g + heuristique(new.node, endNode)

            # Si il n'est pas dans la frontière et qu'il n'est pas dans l'histoire
            if (not isInFrontiere(frontiere, new)) and (op not in history):
                frontiere.append(new)

        # Sort des frontières selon la distance
        frontiere.sort()
    return "Pas de solution"

# Test si l'état se trouve déjà dans la frontière
def isInFrontiere(frontiere, state):
    for s in frontiere:
        if s.node.city == state.node.city :
            return True
    return False

# Test s'il y a une solution et l'affiche
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

    ville1 = "Warsaw"
    ville2 = "Lisbon"

    # Calcul de toutes les heuristiques
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

