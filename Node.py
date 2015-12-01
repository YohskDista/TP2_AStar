__author__ = 'leonardo.distasio & kevin.vulliemin'

class Node(object):

    def __init__(self, city, x, y):
        self.city = city
        self.x = x
        self.y = y
        self.listChild = []

    def __repr__(self):
        return self.city

    def __lt__(self, node):
        return self.quality < node.quality

    def addChild(self, node):
        self.listChild.append(node)