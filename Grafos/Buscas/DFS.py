import Biblioteca_Geral.Basico_Grafos as bg
import matplotlib.pyplot as plt

def DFS_Visita(G,u,node,edge,caminho,pos,ax):
    node[u] = "red"
    bg.desenha(G,pos,plt,ax,node,edge)
    for v in G.neighbors(u):
        ed = (u, v)
        if node[v] == "blue":
            edge[ed] = "green"
            caminho[v] = u
            bg.desenha(G,pos,plt,ax,node,edge)
            node, edge, caminho = DFS_Visita(G,v,node,edge,caminho,pos,ax)
    node[u] = "black"
    edge[ed] = "black"
    bg.desenha(G,pos,plt,ax,node,edge)
    return node, edge, caminho

def DFS(G,pos):
    plt.ion()
    fig, ax = plt.subplots()
    node, edge, caminho = bg.Cor_Caminho(G)
    bg.desenha(G,pos,plt,ax,node,edge)
    for u in G.nodes:
        if node[u] == "blue":
            node, edge, caminho = DFS_Visita(G,u,node,edge,caminho,pos,ax)
    return caminho
