import random
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
from pylab import rcParams

def vizing(n):

  def add_final_vertex(n,aresta,lista,adjacencia):
    for i in range(n):
      cor = disponivel[i].pop()
      aresta[i,n] = cor
      lista.append((i,n))
      adjacencia[i,cor] = n
      adjacencia[n,cor] = i
    #aresta = dict(sorted(aresta.items(), key=lambda item: item[1]))

  def check(n,aresta,disponivel,adjacencia):
    for a in aresta:
      u,v = a[0],a[1]
      if aresta[a] != None:
        c = aresta[a]
        if adjacencia[u,c] != v or adjacencia[v,c] != u:
          w1,w2 = adjacencia[v,c],adjacencia[u,c]
          if w1 > w2:
            w1,w2 = w2,w1
          print('e',u,v,c,'-', w1,w2,aresta[w1,w2])
          break
    
    for v in range(n):
      a = [0]*n
      for c in range(n):
        if adjacencia[v,c] != None: 
          a[adjacencia[v,c]]+=1
          if(a[adjacencia[v,c]] == 2):
            a = adjacencia[v,c]
            for c in range(n):
              if adjacencia[v,c] == a:
                print('a',v,adjacencia[v,c],c)
            break

  def getColor(s,proibida):
      for e in s:
        if e != proibida:
          return e
      
  def desenha(n,aresta):
    G = nx.complete_graph(n) 
    pos = nx.circular_layout(G,scale=2) 

    cm = plt.get_cmap('gist_rainbow')
    low,high = 0,n
    norm = mpl.colors.Normalize(vmin=low, vmax=high, clip=True)
    mapper = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.coolwarm)
    edge_colors = []
    for i in aresta:
      if aresta[i] == None: 
        G.remove_edge(*i)
      else:
        edge_colors.append(cm(1.*aresta[i]/(n)))
        # edge_colors.append(mapper.to_rgba(aresta[i]))
    
    edge_labels = dict([((i[0],i[1]), aresta[i]) for i in aresta if aresta[i]!= None])

    plt.clf()
    clear_output(wait=True)
    nx.draw(G, pos=pos, edge_color = edge_colors, with_labels=True, width=4)
    # nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=edge_labels)
    plt.show()
    plt.pause(.01)
          

  # Entrada: o valor de n, em K_n
  #n = int(input())

  # Determina a quantidade de arestas do grafo
  e = n*(n-1)//2

  # Declarar as estruturas de dados
  # Lista de Arestas
  aresta = dict()
  lista = []
  for v in range(n):
    for w in range(n):
      if w > v:
        aresta[v,w] = None
        lista.append((v,w))

  # Estrutura de cores disponives nos vertices
  disponivel = {}
  for v in range(n):
    disponivel[v] = {c for c in range(n)}

  # Adjacencia de cores
  adjacencia = {}
  for v in range(n):
    for c in range(n):
        adjacencia[v,c] = None
  
  # desenha(n,aresta)
  random.shuffle(lista)
  k=0
  proibida = None
  while k < len(lista):
    
    u,v = lista[k][0],lista[k][1]
    # Verificar se a aresta não está colorida
    if aresta[u,v] == None:
      # Identificar uma cor disponivel nos extremos da aresta
      c = disponivel[u].intersection(disponivel[v])
      isEmpty = (0 == len(c))
      if not isEmpty:
        # Colorir a aresta com a primeira cor encontra
        cor = c.pop()
        # cor = random.choice(c)
        # Atualizar as 3 estruturas de dados
        aresta[u,v] = cor
        # desenha(n,aresta)
        disponivel[u].remove(cor)
        disponivel[v].remove(cor)
        adjacencia[u,cor] = v
        adjacencia[v,cor] = u
        proibida = None
      else:
        
        # Identificar cor alfa, disponivel em v e presente em u
        lf = getColor(disponivel[v],proibida)
        # Identificar cor beta, disponivel em u e presente em v
        bt = getColor(disponivel[u],proibida)

        alfa,beta = lf,bt

        if alfa == None or beta == None:
          print(proibida)

        # Construir o caminho alternado alfa-beta partindo de u com a cor alfa
        w = [u]
        for i in w:
          # Interrompe se nao for possivel extender o caminho
          if adjacencia[i,alfa] == None:
            break
          # Apaga o caminho se este chegar em v
          if adjacencia[i,alfa] == v:
            w = []
            break
          w.append(adjacencia[i,alfa])
          alfa,beta = beta,alfa

        # Alterna as cores do caminho alfa-beta
        if w:
          
          # Recupera os valores das cores alfa e beta
          alfa,beta = lf,bt

          # Alterna as cores do caminho se este nao terminar em v
          for i in range(len(w)-1):
            wi, wj = w[i],w[i+1]

            
            # Atualiza as cores disponíveis
            adjacencia[wi,beta] = wj
            adjacencia[wj,beta] = wi
            # Atualiza a matriz de adjacencia
            if i == 0:
              adjacencia[wi,alfa] = None
              if beta in disponivel[wi]:
                disponivel[wi].remove(beta)
              if alfa not in disponivel[wi]:
                disponivel[wi].add(alfa)
            if i == len(w)-2:
              adjacencia[wj,alfa] = None
              if beta in disponivel[wj]:
                disponivel[wj].remove(beta)
              if alfa not in disponivel[wj]:
                disponivel[wj].add(alfa)
            
            # Atualiza a cor da aresta
            if wi > wj:
              wi,wj = wj,wi
            aresta[wi,wj] = beta
            # desenha(n,aresta)

            # Alterna as cores
            alfa,beta = beta,alfa
          
          # Colore a aresta u,v com a cor alfa
          cor = lf
          disponivel[u].remove(cor)
          disponivel[v].remove(cor)
          adjacencia[u,cor] = v
          adjacencia[v,cor] = u
          aresta[u,v] = cor
          # desenha(n,aresta)
          proibida = None
        else:
          # Ramon, termine a função que verifica as inconsistências das estruturas de dados
          # Utilize essa estrutura em toda iteração do while.
          # Corrija qualquer bug que apareça no código
          
          # Identifica o vertice w2 que está adjacente a u=w1 pela aresta de cor alfa
          alfa = lf
          w1 = u
          w2 = adjacencia[w1,alfa]
          
          # Atualizar as estruturas de dados colorindo a aresta uv com a cor alfa e remover a cor alfa da aresta uw
          disponivel[w2].add(alfa)
          adjacencia[w2,alfa] = None
          adjacencia[w1,alfa] = v
          adjacencia[v,alfa] = u
          disponivel[v].remove(alfa)

          if w1 > w2:
            w1,w2 = w2,w1
          aresta[w1,w2] = None
          # desenha(n,aresta)
          
          aresta[u,v] = alfa
          # desenha(n,aresta)

          proibida = alfa

          # Retomar a execução do algoritmo a partir da aresta uw
          k = lista.index((w1,w2))
          # desenha(n,aresta)
          continue
    k+=1
  print(disponivel)
  add_final_vertex(n,aresta,lista,adjacencia)
  print(aresta)
  desenha(n+1,aresta)
  return aresta

a = vizing(5)