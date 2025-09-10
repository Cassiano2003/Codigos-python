import networkx as nx
import matplotlib.pyplot as plt
import random

#Funçao que faz a animação das trocas de cores
def desenha(G,pos,plt,ax,node,edges):
        ax.clear()
        # Converte dicionário de cores em lista ordenada pelos nós
        cores_nodes = [node[u] for u in G.nodes]
        cores_edge = [edges[u] for u in G.edges]
        nx.draw(G, pos, with_labels=True, node_size=600, node_color=cores_nodes,
                edge_color=cores_edge, font_size=8, ax=ax)
        plt.draw()
        plt.pause(1)  # controla a velocidade da animação


def Cor_Caminho(G):
    # Inicializa cores e caminhos
    vertices = {u: "blue" for u in G.nodes}
    #Cores das arestas
    aresestas = {u: "gray" for u in G.edges}
    pais = {u: None for u in G.nodes}
    return vertices,aresestas,pais

#Funçao q usa a lista e o dicionario para criar o grafo
def Cria_Grafo(G,lista, dici):
    for nome in lista:
        G.add_node(nome)  
        for aresta in dici[nome]:
            G.add_edge(nome, aresta)

#Funçao q gera algumas aresta aleatoriamente (OBS: Chat q fez)
def Gera_arestas(meu_numero, vertices, qtd=3):
    # escolhe 'qtd' vértices aleatórios diferentes de 'meu_numero'
    possiveis = [v for v in vertices if v != meu_numero]
    return random.sample(possiveis, k=min(qtd, len(possiveis)))

#Vai gerar um grafo aleatorio, entao ele pode ser qualquer grafo
def Gera_Vertices_E_Arestas_Para_Um_Grafo_Qualquer(tam,quant):
     #Cria os vetices e as arestas
    vertices = [i for i in range(tam)]
    arestas = {a: Gera_arestas(a, vertices, qtd=quant) for a in vertices}
    return vertices,arestas

