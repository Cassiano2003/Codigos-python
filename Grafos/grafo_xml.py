import networkx as nx
import matplotlib.pyplot as plt
import itertools
from lxml import etree as ET

# Cria grafo
G = nx.Graph()

# Limite de artigos a processar (para não lotar a memória)
parada = 500   # <<< muda aqui conforme a força do teu notebook
j = 0

# Leitura em streaming
context = ET.iterparse("dblp-2025-08-01.xml", events=("end",), tag="incollection")

for event, elem in context:
    if j >= parada:
        break

    # Pega todos os autores desse artigo
    autores = [a.text.strip() for a in elem.findall("author") if a.text]

    # Adiciona nós
    for autor in autores:
        G.add_node(autor)

    # Cria arestas entre coautores
    for a1, a2 in itertools.combinations(autores, 2):
        if G.has_edge(a1, a2):
            G[a1][a2]["weight"] += 1
        else:
            G.add_edge(a1, a2, weight=1)

    j += 1

    # Libera memória (descarta o elemento já processado)
    elem.clear()

# Desenha o grafo
pos = nx.spring_layout(G, seed=42)
nx.draw(
    G, pos,
    with_labels=True,
    node_color="lightblue",
    font_size=7,
    edge_color="gray"
)

plt.show()
