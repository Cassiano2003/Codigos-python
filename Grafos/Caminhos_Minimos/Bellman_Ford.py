from calendar import c
import Biblioteca_Geral.Basico_Grafos as bg
import matplotlib.pyplot as plt
import networkx as nx

def Bellman_Ford(G:nx.DiGraph,pos:dict,s):
    G = bg.Cor_Caminho(G,True)
    G.nodes[s]["valor"] = 0
    G.nodes[s]["cor"] = "red"
    plt.ion()
    _,ax = plt.subplots()
    bg.desenha(G,pos,plt,ax)
    for  u in G.nodes:
        for v in G.neighbors(u):
            G.edges[(u,v)]["cor"] = "green"
            bg.desenha(G,pos,plt,ax)
            bg.Relachamento(G,u,v,G.edges[(u,v)]["peso"])
            bg.desenha(G,pos,plt,ax)
    plt.ioff()
    plt.show()
    for u,v in G.edges:
        if G.nodes[v]["valor"] > G.nodes[u]["valor"]+G.edges[(u,v)]["peso"]:
            return False
    return True 