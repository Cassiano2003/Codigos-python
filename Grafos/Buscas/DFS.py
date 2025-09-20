import Biblioteca_Geral.Basico_Grafos as bg
import matplotlib.pyplot as plt
import networkx as nx

def DFS_Visita(G:nx.Graph,u:int,pos:dict,ax:plt.axes):
    G.nodes[u]["cor"] = "red"
    bg.desenha(G,pos,plt,ax)
    for v in G.neighbors(u):
        ed = (u, v)
        if G.nodes[v]["cor"] == "blue":
            G.edges[ed]["cor"] = "green"
            G.nodes[v]["caminho"] = u
            bg.desenha(G,pos,plt,ax)
            G = DFS_Visita(G,v,pos,ax)
        G.edges[ed]["cor"] = "black"
    G.nodes[u]["cor"] = "black"
    bg.desenha(G,pos,plt,ax)
    return G

def DFS(G:nx.Graph,pos:dict):
    plt.ion()
    _,ax = plt.subplots()
    G = bg.Cor_Caminho(G)
    bg.desenha(G,pos,plt,ax)
    for u in G.nodes:
        if G.nodes[u]["cor"] == "blue":
            G = DFS_Visita(G,u,pos,ax)
    plt.ioff()
    plt.show(block=False)
    plt.pause(2)
    plt.close()
    return G
