import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes import graph

from readInstance import getInstance
from classes import Graph,Node,Edge

#myInstance = getInstance('inst4linearperturbacaoA')
#print(myInstance.weights)

def drawGraph():
    rgb_color = ['gray','r','g','b','y','m','brown']
    H = nx.Graph()
    for node in graph.nodes:
        H.add_node(node.name)
    for edge in graph.edges:
        u = edge.nodes[0].name
        v = edge.nodes[1].name
        color = edge.color
        H.add_edge(u,v,color=rgb_color[color])
    edges = H.edges()
    colors = [H[u][v]['color'] for u,v in edges]
    nx.draw(H, pos=nx.spring_layout(H),edge_color=colors, with_labels=True)
    plt.show()

def chain(v0,w):
    # Escolho uma cor para beta
    for beta_color in w.free_color:
        for vizinho in v0.neighbour:
            pass

    print(v0.free_color,w.free_color)


n = 5
G = nx.complete_graph(n)
graph = Graph()

# n cores disponiveis para cada no
all_colors = [x for x in range(1,n+1)]

for i in range (n):
    u = Node(i,set(all_colors))
    graph.nodes.append(u)

for edge in G.edges():
    u = graph.nodes[edge[0]]
    v = graph.nodes[edge[1]]
    edge = Edge(u,v)
    graph.edges.append(edge)
    u.neighbour.append(v)
    v.neighbour.append(u)

for edge in graph.edges:
    v0,w = edge.nodes
    common_color = v0.free_color.intersection(w.free_color)
    if common_color:
        color = common_color.pop()
        edge.color = color
        v0.free_color.remove(color)
        w.free_color.remove(color)
        #print(u.name,v.name)
    else:
        chain(v0,w)

# print(all_colors)
# for e in graph.edges:
#     print(e.nodes[0].name,e.nodes[1].name,'color:', e.color)
# for node in graph.nodes:
#     print('node:',node.name, node.free_color)
drawGraph()