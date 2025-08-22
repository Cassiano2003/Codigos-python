import networkx as nx
import matplotlib.pyplot as plt
import random
import time

#Variaveis globais(Pretendo mudar)
G = nx.Graph()
tam = 10

def BFS(G, s, pos):
    # Inicializa cores e caminhos
    cor = {u: "white" for u in G.nodes}
    caminho = {u: None for u in G.nodes}
    Qfila = []

    # Inicia matplotlib no modo interativo
    plt.ion()
    fig, ax = plt.subplots()

    def desenha():
        ax.clear()
        # Converte dicionário de cores em lista ordenada pelos nós
        cores = [cor[u] for u in G.nodes]
        nx.draw(G, pos, with_labels=True, node_color=cores,
                edge_color="gray", font_size=8, ax=ax)
        plt.draw()
        plt.pause(0.8)  # controla a velocidade da animação

    # Marca nó inicial
    cor[s] = "red"
    Qfila.append(s)
    desenha()

    # Loop da BFS
    while Qfila:
        u = Qfila[0]
        for v in G.neighbors(u):
            if cor[v] == "white":
                cor[v] = "red"
                caminho[v] = u
                Qfila.append(v)
                desenha()
        Qfila.pop(0)
        cor[u] = "black"
        desenha()

    plt.ioff()
    plt.show()
    return caminho

#Funçao q usa a lista e o dicionario para criar o grafo
def Cria_Grafo(lista, dici):
    for nome in lista:
        G.add_node(nome)  
        for aresta in dici[nome]:
            G.add_edge(nome, aresta)


#Funçao de busca sem animaçao no plot
#OBS: a animaçao eu pedi pro chat fazer, mais essa funçao é criaçao propria combase no pesuldo codigo do professor
'''def BFS(G,s):
    cor = {u : "white" for u in G.nodes}
    caminho = {u : 0 for u in G.nodes}
    Qfila = []
    cor[s] = "red"
    Qfila.append(s)
    while(len(Qfila) != 0):
        u = Qfila[0]
        for v in G.neighbors(u):
            if cor[v] == "white":
                cor[v] = "red"
                caminho[v] = u
                Qfila.append(v)
        Qfila.pop(0)
        cor[u] = "black"'''


#Funçao q gera algumas aresta aleatoriamente (OBS: Chat q fez)
def Gera_arestas(meu_numero, vertices, qtd=3):
    # escolhe 'qtd' vértices aleatórios diferentes de 'meu_numero'
    possiveis = [v for v in vertices if v != meu_numero]
    return random.sample(possiveis, k=min(qtd, len(possiveis)))


#Cria os vetices e as arestas
vertices = [i for i in range(tam)]
arestas = {a: Gera_arestas(a, vertices, qtd=3) for a in vertices}

#Chama as funçoes
Cria_Grafo(vertices, arestas)
pos = nx.spring_layout(G)  # layout fixo para não "pular"
caminho = BFS(G, 1, pos)
print("Pais na árvore de BFS:", caminho)