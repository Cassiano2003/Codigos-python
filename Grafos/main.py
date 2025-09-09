import Biblioteca_Geral.Basico_Grafos as bg
import os
import Buscas.DFS as DFS
import Buscas.BFS as BFS

def main():
    os.system("clear")
    G = bg.nx.Graph()
    opcoes = ["[0] BFS","[1] DFS","[2] Sair"]
    print("--------------------------------------------")
    print("Escolha uma opção")
    for o in opcoes:
        print(o)
    escolha = int(input("Digite o numero de escolha: "))
    if escolha != len(opcoes)-1:
        print("OBS: Só tem o grafo nao oritentado")
        print("--------------------------------------------")
        tam = int(input("Digite a quantidade de nodes: "))
        quant = int(input("Digite a quantidade maxima de edges por nodes: "))
        print("--------------------------------------------")
        #Cria os vetices e as arestas
        vertices, arestas = bg.Gera_Dicionarios(tam,quant)
        bg.Cria_Grafo(G,vertices, arestas)
        pos = bg.nx.spring_layout(G, k=10, seed=42)
    caminho = 0
    match escolha:
        case 0:
            inicio = int(input("Em qual node vai começar: "))
            caminho = BFS.BFS(G, inicio, pos)
        case 1:
            caminho = DFS.DFS(G,pos)
        case 2:
            sim_ou_nao = input("Deseja mesmo encerar o programa (S ou N): ")
            if sim_ou_nao == "S" or sim_ou_nao == "s":
                return False
        case _:
            print("Entrada invalida!!!!")
            return False
    print("--------------------------------------------")
    print("Pais na árvore de ",opcoes[escolha],": \n", caminho)
    print("--------------------------------------------")
    input("precione enter para continuar")
    return True

continua = True
while continua:
    continua = main()

    

