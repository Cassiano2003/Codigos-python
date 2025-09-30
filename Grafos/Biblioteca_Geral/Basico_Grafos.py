import networkx as nx
import matplotlib.pyplot as plt
import random
import time

#Funçao que faz a animação das trocas de cores
def desenha(G:nx.Graph,pos:dict,plt:plt.figure,ax:plt.axes,seleciona:bool=False):
        ax.clear()
        # Converte dicionário de cores em lista ordenada pelos nós
        cores_nodes = [G.nodes[u]["cor"] for u in G.nodes]
        cores_edge = [G.edges[u]["cor"] for u in G.edges]
        labels = nx.get_edge_attributes(G, "peso")
        nx.draw(G, pos, with_labels=seleciona, node_size=600, node_color=cores_nodes,
                edge_color=cores_edge, font_size=8,connectionstyle='arc3,rad=0.1', ax=ax)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        labels = {n: G.nodes[n]["valor"] for n in G.nodes}
        if(not seleciona):
           nx.draw_networkx_labels(G, pos, labels=labels, font_color="black")
        plt.draw()
        plt.pause(2)  # controla a velocidade da animação

#Cria minhas seeds
def Cria_seed(deslocamento:int=32):
    segundos = int(time.time())
    nano = int(time.time_ns())
    seed1 = str(segundos ^ (nano >> deslocamento))
    print(seed1)
    seed2 = str(nano ^ (segundos >> deslocamento))
    print(seed2)
    print(int(seed1+seed2) % (2**32))
    return int(seed1+seed2) % (2**32)

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
def Cria_Grafo_Sem_Direcao(G:nx.Graph,vetices:list, arestas:dict):
    for v in vetices:
        G.add_node(v)  
        for a in arestas[v]:
            G.add_edge(v, a)

def Cria_Grafo_Com_Direcao(G:nx.DiGraph,vetices:list, arestas:dict):
    for v in vetices:
        G.add_node(v)  
        for a in arestas[v]:
            G.add_edge(v, a)

def Relachamento(G:nx.Graph,u,v,c):
    if G.nodes[v]["valor"] > G.nodes[u]["valor"]+c:
        G.nodes[v]["valor"] = G.nodes[u]["valor"]+c
        if G.nodes[v]["caminho"] != None:
            no = G.nodes[v]["caminho"]
            ed = (no,v)
            G.edges[ed]["cor"] = "gray"
        G.nodes[v]["caminho"] = u    
        G.nodes[v]["cor"] = "red"
        G.edges[(u,v)]["cor"] = "black"


def Gera_sub_Grafo(G:nx.Graph,s = 0,direcinal:bool=False):
    H = nx.Graph()
    if direcinal:
        H = nx.DiGraph()
    vertices = []
    arestas = []
    for v in G.nodes:
        no = G.nodes[v]["caminho"]
        if no != None or v == s:
            vertices.append(v)
            arestas.append((no,v))
    print(vertices,"\n",arestas)
    H.add_nodes_from((n, G.nodes[n]) for n in vertices)
    H.add_edges_from((u, v, G.edges[u, v]) for (u, v) in arestas if u is not None)
    return H


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
