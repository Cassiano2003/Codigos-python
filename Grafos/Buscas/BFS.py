import Biblioteca_Geral.Basico_Grafos as bg
import matplotlib.pyplot as plt

#Busca em largura
def BFS(G, s, pos):
    cor, ares,caminho = bg.Cor_Caminho(G)
    Qfila = []

    # Inicia matplotlib no modo interativo
    plt.ion()
    fig, ax = plt.subplots()
        
    # Marca nó inicial
    cor[s] = "red"
    Qfila.append(s)
    bg.desenha(G,pos,plt,ax,cor,ares)
    # Loop da BFS
    while Qfila:
        u = Qfila[0]
        for v in G.neighbors(u):
            edges = (u, v) # Vai gerar qual é aresta q estamos visitando
            if cor[v] == "blue":
                ares[edges] = "green" #Muda a cor de uma aresta caso ache um node q nao foi explorado 
                cor[v] = "red"
                caminho[v] = u
                Qfila.append(v)
                bg.desenha(G,pos,plt,ax,cor,ares)
            ares[edges] = "black" #Muda a cor das arestas que ja foram visitadas
        Qfila.pop(0)
        cor[u] = "black"
        bg.desenha(G,pos,plt,ax,cor,ares)
        
    plt.ioff()
    plt.show()
    return caminho

#print(int(input("Cassiano, digite sua senha por favor: ")))
