import networkx as nx
import matplotlib.pyplot as plt

#G = nx.graph()
arquivo = "facebook_combined.txt"

def cria_lendo_arquivo_manualmente(arquivo):
    G = nx.Graph()
    with open(arquivo,"r") as arq:
        for linha in arq:
            v1,v2 = linha.split()
            G.add_edge(v1,v2)
    print("Foi criado o arquivo!!!")
    print(f"O diametro é: {nx.diameter(G)}")
    pos = nx.spring_layout(G,k=20, seed=500)
    nx.draw(G,pos,with_labels=True)
    plt.show()
    

def cria_por_funçao(arquivo):
    print("Criando pro funçao!!!")
    try:
        G = nx.read_adjlist(arquivo,nodetype=int)
        print("Foi criado o arquivo!!!")
        print(f"O diametro é: {nx.diameter(G)}")
        pos = nx.spring_layout(G,k=20, seed=500)
        nx.draw(G,pos,with_labels=True)
        #nx.draw(G,with_labels=True)
        plt.show()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
    

cria_lendo_arquivo_manualmente(arquivo)