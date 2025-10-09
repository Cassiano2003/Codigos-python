import networkx as nx
import matplotlib.pyplot as plt
import xml.etree.ElementTree as EL
from multiprocessing import Pool,cpu_count
import time


#Funçoes que faz a ciraçao em paralelo
def processa_artigo_paralelo(artigo):
    """
    Processa um único artigo e retorna os autores
    Esta função será executada em paralelo
    """
    autores = []
    for autor_elem in artigo.findall('author'):
        if autor_elem.text:
            autores.append(autor_elem.text.strip())
    return autores

def Gera_discionario(autores,nomes):
    dic = {}
    for i, lista_autores in enumerate(autores):
        print(f"Tem quantos numeros {len(str(i+1))} {i+1}: {len(lista_autores)} autores")
        
        for autor in lista_autores:
            if autor not in nomes:
                nomes.append(autor)
                dic[autor] = []
            
            # Adicionar coautores (excluindo o próprio autor)
            coautores = [coautor for coautor in lista_autores if coautor != autor]
            dic[autor].extend(coautores)
    return dic

def Cria_parentesco_paralelo(arquivo:str) -> dict[str:list[str]]:
    xml = EL.parse(arquivo)
    root = xml.getroot()
    artigo = list(root)
    with Pool(processes=4,maxtasksperchild=10) as p:
        autores = p.map(processa_artigo_paralelo,artigo)
    print(f"Processando {len(artigo)} artigos em paralelo...")
    time.sleep(10)
   # Construir o dicionário final
    dic = {}
    nomes = []

    with Pool(processes=4,maxtasksperchild=10) as p:
        dis = p.map(Gera_discionario,autores,nomes)
    return dis
#--------------------------------------------------------------------------------------------


#Funçoes para criar com um arquivo um puco menor
def Cria_parentesco(arquivo:str) -> dict[str:list[str]]:
    dic = {}
    autores = []
    xml = EL.parse(arquivo)
    root = xml.getroot()
    for artigos in root:
        for elementos in artigos.findall("author"):
            autor = elementos.text
            lista_autores = artigos.findall("author")
            lista_autores.remove(elementos)
            if autor not in autores:
                dic[autor] = [arestas.text for arestas in lista_autores]
            else:
                autores.append(autor)
                for arestas in lista_autores:
                    dic[autor].append(arestas.text)
            

    return dic


#---------------------------------------------------------------------------------------------

#Funçao generica para criar um garafo generico apartir de um dicionario
def Cria_Grafo(dic:dict):
    G = nx.Graph()
    for nome in dic:
        G.add_node(nome)
        for amigos in dic[nome]:
            if amigos != None:
                G.add_edge(nome,amigos)
    return G

def Imprime_dicionario(Dicionario:dict):
    for nome,ligados in Dicionario.items():
        print(f"Autor {nome} é ligado a esses outros autores {ligados}")

#Minha MAIN
arquivo_grande = "dblp-2025-09-01-articles.xml"
arquivo_pequeno = "dblp-2025-09-01-articles-mhc.xml"

dic_nomes = Cria_parentesco(arquivo_pequeno)
G = Cria_Grafo(dic_nomes)
Imprime_dicionario(dic_nomes)
print(f"O diametro é: {nx.diameter(G)}")
pos = nx.spring_layout(G,k=20, seed=500)
nx.draw(G,pos,with_labels=True)
plt.show()

#------------------------------------------------------------------------------------------

#A quantidade de artigos = 3.902.753