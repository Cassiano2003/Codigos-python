import networkx as nx
import matplotlib.pyplot as plt
import random

#Funçao que faz a animação das trocas de cores
def desenha(G:nx.Graph,pos:dict,plt:plt.figure,ax:plt.axes):
        ax.clear()
        # Converte dicionário de cores em lista ordenada pelos nós
        cores_nodes = [G.nodes[u]["cor"] for u in G.nodes]
        cores_edge = [G.edges[u]["cor"] for u in G.edges]
        labels = nx.get_edge_attributes(G, "peso")
        nx.draw(G, pos, with_labels=False, node_size=600, node_color=cores_nodes,
                edge_color=cores_edge, font_size=8, ax=ax)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        labels = {n: G.nodes[n]["valor"] for n in G.nodes}
        nx.draw_networkx_labels(G, pos, labels=labels, font_color="black")
        plt.draw()
        plt.pause(1)  # controla a velocidade da animação


#----Basico para as aresas e vertices-----
#Funçao que gera pesos para as arestas
def Gera_pesos() -> int:
    return random.randint(1, 10)
#Funçao que gera os pesos para as arestas e as cores para os nodes e as arestas
def Cor_Caminho(G,negativo:bool=False):
    for v in G.nodes:
        G.nodes[v]["cor"] = "blue"
        G.nodes[v]["caminho"] = None
        G.nodes[v]["valor"] = float('inf')
    for e in G.edges:
        G.edges[e]["cor"] = "gray"
        if negativo:
            G.edges[e]["peso"] = -Gera_pesos()
            negativo = False if random.random() < 0.4 else True
        else:
            G.edges[e]["peso"] = Gera_pesos()
    return G

    
#----Criaçao de Grafo qualquer sem direção-----
#Funçao q usa a lista e o dicionario para criar o grafo
def Cria_Grafo_Sem_Direcao(G:nx.Graph,lista:list, dici:dict):
    for nome in lista:
        G.add_node(nome)  
        for aresta in dici[nome]:
            G.add_edge(nome, aresta)

def Cria_Grafo_Com_Direcao(G:nx.DiGraph,lista:list, dici:dict):
    for nome in lista:
        G.add_node(nome)  
        for aresta in dici[nome]:
            G.add_edge(nome, aresta)

def Relachamento(G:nx.Graph,u,v,c):
    if G.nodes[v]["valor"] > G.nodes[u]["valor"]+c:
        G.nodes[v]["valor"] = G.nodes[u]["valor"]+c
        G.nodes[v]["caminho"] = u
        G.nodes[v]["cor"] = "red"
        G.edges[(u,v)]["cor"] = "black"


#Funçao q gera algumas aresta aleatoriamente (OBS: Chat q fez)
def Gera_arestas(meu_numero:int, vertices:list, qtd:int=3):
    # escolhe 'qtd' vértices aleatórios diferentes de 'meu_numero'
    possiveis = [v for v in vertices if v != meu_numero]
    return random.sample(possiveis, k=min(qtd, len(possiveis)))

#Vai gerar um grafo aleatorio, entao ele pode ser qualquer grafo
def Gera_Vertices_E_Arestas_Para_Um_Grafo_Qualquer(tam:int,quant:int):
     #Cria os vetices e as arestas
    vertices = [i for i in range(tam)]
    arestas = {a: Gera_arestas(a, vertices, qtd=quant) for a in vertices}
    return vertices,arestas

