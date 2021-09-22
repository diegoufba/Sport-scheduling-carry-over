import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes import graph

from readInstance import getInstance

#myInstance = getInstance('inst4linearperturbacaoA')
#print(myInstance.weights)

def drawGraph():
    global color
    rgb_color = ['gray','r','g','b','y','m','brown']
    H = nx.Graph()
    for node in range(n):
        H.add_node(node)
    
    for c in color:
        for edge in color[c]:
            u,v = edge
            H.add_edge(u,v,color=rgb_color[c])

    edges = H.edges()
    colors = [H[u][v]['color'] for u,v in edges]
    nx.draw(H, pos=nx.spring_layout(H),edge_color=colors, with_labels=True)
    plt.show()

def find_next(c,x):
    edge = [node for node in color[c] if x in node]
    if edge:
        if edge[0].index(x) == 0:
            next_edge = edge[0][1]
        else:
            next_edge = edge[0][0]
        return next_edge
    else:
        return -1 

visited = set()
def run_chain(v0,w,c,i):
    visited.add(v0)
    node = find_next(v0,c[i%2])
    print(node)
    if node == -1:
        return
    i += 1
    run_chain(node,w,c,i)

def has_chain(beta_color,alpha_color,v0):
    node = find_next(beta_color,v0)
    if find_next(alpha_color,node) != -1:
        return True
    else:
        return False    

n = 5
G = nx.complete_graph(n)

# n cores disponiveis para cada no
all_colors = [x for x in range(1,n+1)]

# Guarda Cores dos nos
free_color = []
for i in range(n):
    free_color.append(set(all_colors))

# Guarda cores das arestas
color = {}
for i in range (n+1):
    color[i] = []

for edge in G.edges():
    color[0].append(edge)

for edge in G.edges():
    v0,w = edge
    common_color = free_color[v0].intersection(free_color[w])
    if common_color:
        c = common_color.pop()
        color[0].remove(edge)
        color[c].append(edge)
        free_color[v0].remove(c)
        free_color[w].remove(c)
    else:
        beta_colors = list(free_color[w])
        alpha_colors = list(free_color[v0])
        for beta_color in beta_colors:
            for alpha_color in alpha_colors:
                if(has_chain(beta_color,alpha_color,v0)):
                    i = 0
                    #run_chain(v0,w,(beta_color,alpha_color),i)

print(color)
drawGraph()


