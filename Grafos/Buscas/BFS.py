import Biblioteca_Geral.Basico_Grafos as bg
import matplotlib.pyplot as plt
import networkx as nx

#Busca em largura
def BFS(G:nx.Graph, s, pos):
    G = bg.Cor_Caminho(G)
    Qfila = []

    # Inicia matplotlib no modo interativo
    plt.ion()
    _, ax = plt.subplots()
        
    # Marca nó inicial
    G.nodes[s]["cor"] = "red"
    Qfila.append(s)
    bg.desenha(G,pos,plt,ax)
    # Loop da BFS
    while Qfila:
        u = Qfila[0]
        for v in G.neighbors(u):
            edges = (u, v) # Vai gerar qual é aresta q estamos visitando
            if G.nodes[v]["cor"] == "blue":
                G.edges[edges]["cor"] = "green" #Muda a cor de uma aresta caso ache um node q nao foi explorado 
                G.nodes[v]["cor"] = "red"
                G.nodes[v]["caminho"] = u
                Qfila.append(v)
                bg.desenha(G,pos,plt,ax)
            G.edges[edges]["cor"] = "black" #Muda a cor das arestas que ja foram visitadas
        Qfila.pop(0)
        G.nodes[u]["cor"] = "black"
        bg.desenha(G,pos,plt,ax)
        
    plt.ioff()
    plt.show()
    return G
