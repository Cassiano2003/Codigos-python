import Biblioteca_Geral.Basico_Grafos as bg
import os
import Buscas.DFS as DFS
import Buscas.BFS as BFS
import Caminhos_Minimos.Bellman_Ford as bf

def main():
    os.system("clear")
    G = bg.nx.Graph()
    opcoes = ["[0] BFS","[1] DFS","[2] Bellman Ford","[3] Dijkstra","[4] Sair"]
    tipos_grafos = ["[0] Sem diresção","[1] Com direção"]
    print("--------------------------------------------")
    for o in tipos_grafos:
        print(o)
    qual_tipo = int(input("Como sera o seu grafo COM ou SEM direção:"))
    if qual_tipo <= len(tipos_grafos)-1:
        print("--------------------------------------------")
        vertices,arestas = [], {} 
        if input("Criar grafo manualment s ou n: ") == "s":
            print("Os valores das arestas se o grafo for direcinal vai ser a direçao das arestas!!!")
            v = input("Digite os nomes dos vetices separados por uma virgula: ")
            v = v.split(',')
            vertices = [int(i) for i in v]
            print("Seus vertices é ",vertices)
            for v in vertices:
                print("O vertice ",v,"vai ser ligados a quantos vertices: ",end="")
                quant_v = int(input())
                l = []
                for _ in range(quant_v):
                    print("Digite a qual node o vertice",v,"ele vai se conectar: ",end="")
                    l.append(int(input()))
                arestas[v] = l
            print(vertices,"\n",arestas)
        else:
            tam = int(input("Digite a quantidade de nodes: "))
            quant = int(input("Digite a quantidade maxima de edges por nodes: "))
            print("--------------------------------------------")
            #Cria os vetices e as arestas
            vertices, arestas = bg.Gera_Vertices_E_Arestas_Para_Um_Grafo_Qualquer(tam,quant)
        match qual_tipo:
            case 0:
                bg.Cria_Grafo_Sem_Direcao(G,vertices, arestas)
            case 1:
                G = bg.nx.DiGraph()
                bg.Cria_Grafo_Com_Direcao(G,vertices, arestas)
            case _:
                bg.Cria_Grafo_Sem_Direcao(G,vertices, arestas)
        pos = bg.nx.spring_layout(G, k=10, seed=500)

        print("Grafo ",tipos_grafos[qual_tipo]," foi criado!!!")
        print("--------------------------------------------")
        print("Escolha uma opção")
        for o in opcoes:
            print(o)
        escolha = int(input("Digite o numero de escolha: "))
        if escolha <= len(opcoes)-1:
            match escolha:
                case 0:
                    inicio = int(input("Em qual node vai começar: "))
                    G = BFS.BFS(G, inicio, pos)
                case 1:
                    G = DFS.DFS(G,pos)
                case 2:
                    inicio = int(input("Em qual node vai começar: "))
                    if bf.Bellman_Ford(G,pos,inicio):
                        print("Caminha negativo não encontrado")
                    else:
                        print("Caminha negativo encontrado")
                case 3:
                    print("nao esta pronto")
                case 4:
                    return False
            print("--------------------------------------------")
            print("Pais na árvore de ",opcoes[escolha],": \n","\n",G.nodes(data=True),"\n",G.edges(data=True))
            print("--------------------------------------------")
        else:
            print("Numero de escolha invalido!!!")
    else:
        print("Numero de escolha invalido!!!")
    input("precione enter para continuar")
    return True

continua = True
while continua:
    continua = main()

    

