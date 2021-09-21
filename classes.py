class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

class Node:
    def __init__(self,name,free_color):
        self.name = name
        self.neighbour = []
        self.free_color = free_color

class Edge:
    def __init__(self,u,v):
        self.nodes = (u,v)
        self.color = 0