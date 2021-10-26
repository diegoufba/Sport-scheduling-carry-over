import networkx as nx
import matplotlib.pyplot as plt

def circle_method(n):

    def schedule_function(t,r):
        if t == n:
            return r
        if t == r:
            return n
        equation = (2*r-t) % (n-1)
        if equation == 0:
            return n-1
        else:
            return equation

    schedule = []

    for t in range(1,n+1):
        schedule.append([schedule_function(t,r)-1 for r in range(1,n)])

    # def desenhaGrafo(r):
    #     G = nx.Graph()
    #     G.add_nodes_from(range(1,n+1))
    #     for t in range(1,n+1):
    #         G.add_edge(t,schedule[t-1][r-1])
    #     nx.draw(G, pos=nx.circular_layout(G), with_labels=True)
    #     plt.show()
    

    return schedule
    #desenhaGrafo(1)
