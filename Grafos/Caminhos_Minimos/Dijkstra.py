import Biblioteca_Geral.Basico_Grafos as bg
import matplotlib.pyplot as plt
import networkx as nx
import heapq

def Retorna_min_heap(G:nx.Graph):
    min_heap = []
    for v in G.nodes:
        min_heap.append(G.nodes[v]["valor"])
    heapq.heapify(min_heap)
    return min_heap

def Busca_por_Valor(G:nx.Graph,valor):
    for v in G.nodes:
        if G.nodes[v]["valor"] == valor:
            return v

def Atualiza_Valores(Q:list,valor_antigo,valor_atual):
    na_onde_esta = Q.index(valor_antigo)
    Q[na_onde_esta] = valor_atual
    heapq.heapify(Q)

def Dijkstra(G:nx.Graph,pos:dict,s):
    G = bg.Cor_Caminho(G)
    G.nodes[s]["valor"] = 0
    G.nodes[s]["cor"] = "red"
    plt.ion()
    _,ax = plt.subplots()
    bg.desenha(G,pos,plt,ax)
    S = []
    Q = Retorna_min_heap(G)
    while len(Q) > 0:
        print(Q)
        u = Busca_por_Valor(G,Q[0])
        Q.pop(0)
        S.append(u)
        for vizinho in G.neighbors(u):
            valor_antigo = G.nodes[vizinho]["valor"]
            ed = (u,vizinho)
            cor_original = G.edges[ed]["cor"]
            G.edges[ed]["cor"] = "green"
            bg.desenha(G,pos,plt,ax)
            bg.Relachamento(G,u,vizinho,G.edges[ed]["peso"])
            valor_atual = G.nodes[vizinho]["valor"]
            bg.desenha(G,pos,plt,ax)
            G.edges[ed]["cor"] = cor_original
            if valor_antigo in Q:
                Atualiza_Valores(Q,valor_antigo,valor_atual)
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


