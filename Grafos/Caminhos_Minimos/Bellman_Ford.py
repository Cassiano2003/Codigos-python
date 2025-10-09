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
    for  i in range(len(G.nodes)-1):
        print(f"Em qual interaçao estamos {i+1}!!!")
        for u,v in G.edges:
            cor_original = G.edges[(u,v)]["cor"]
            G.edges[(u,v)]["cor"] = "green"
            bg.desenha(G,pos,plt,ax)
            bg.Relachamento(G,u,v,G.edges[(u,v)]["peso"])
            bg.desenha(G,pos,plt,ax)
            G.edges[(u,v)]["cor"] = cor_original
    plt.ioff()
    plt.show(block=False)
    plt.pause(2)
    plt.close()
    plt.ion()
    _,ax = plt.subplots()
    H = bg.Gera_sub_Grafo(G,s,True)
    bg.desenha(H,pos,plt,ax)
    plt.ioff()
    plt.show(block=False)
    plt.pause(5)
    plt.close()
    for u,v in G.edges:
        if G.nodes[v]["valor"] > G.nodes[u]["valor"]+G.edges[(u,v)]["peso"]:
            return False
    return True 