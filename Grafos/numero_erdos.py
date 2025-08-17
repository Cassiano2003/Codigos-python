#Vai buscar o qual longe esta de Erdos
import json
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

G = nx.Graph()
tam = 10

def Cria_Grafo(lista,dici):
    for i, nome in enumerate(lista):
        if i > tam:  # limita para não explodir na visualização
            break
        G.add_node(nome)  # adiciona o vértice
        for j, arestas in dici[nome]:
            G.add_edge(nome,arestas[j])

    nx.draw(G, with_labels=True, font_size=8)
    plt.show()


def Cria_Dicionario(lista,file,dicionarios):
    with open(file, 'r', encoding='utf-8') as f:
        for linha in f:
            try:
                obj = json.loads(linha)
                nomes_autores = [autor["name"] for autor in obj.get("authors", [])]
                print(nomes_autores)
            except json.JSONDecodeError:
                continue
    

def Cria_Lista_Nomes(file):
    lista_nome = []
    try:
        with open(file, 'r', encoding='utf-8') as f:
            i = 0
            for linha in f:
                try:
                    obj = json.loads(linha)
                    lista_nome.append(obj["name"])
                except json.JSONDecodeError:
                    continue  # pula linhas inválidas
                i += 1
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado")
    return lista_nome


n = 'v5_oag_author.json'
p = 'v5_oag_publication_1.json'

print("Criando lista de nomes")
nomes = Cria_Lista_Nomes(n)

print("Criando primeiro dicionario ",len(nomes))
dicionario = {nome: " " for nome in nomes}
print(dicionario)

'''print("Criando segundo dicionario")
dicionario2 = Cria_Dicionario(nomes,p,dicionario1)
print(dicionario2)
Cria_Grafo(nomes,dicionario)
'''
