#Cassiano Carvalho de Souza.

#bibliotecas.
import random#gerador de numeros aleatorios.
import time#contador de tempo.

def Bolha(bolha):#ordenar por Bolhas.
    for num in range(len(bolha)-1,0,-1):
        #num recebe o valor maximo de ordenar.
        for i in range(num):
            #esse for vai percorer varias vezez a lista para ordenar ela.
            if bolha[i]>bolha[i+1]:
                #ira verificar se o numero na posiçao i é maior que o i+1,
                #para poder subistituir ele na lista.
                Quarda = bolha[i]
                bolha[i] = bolha[i+1]
                bolha[i+1] = Quarda


def Selecao(selecao):#ordenar por seleçao.
    n = len(selecao)
    # Percorre a lista selecao.
    for i in range(n):
        # Encontra o elemento mínimo em selecao.
        minimo = i
        for j in range(i + 1, n):
            if selecao[minimo] > selecao[j]:
                minimo = j
        # Coloca o elemento mínimo na posição correta.
        selecao[i], selecao[minimo] = selecao[minimo], selecao[i]


def Insercao(insercao):#ordenar por incercao
    n = len(insercao)
    # Percorre a lista ordenar.
    for j in range(1, n):
        chave = insercao[j]
        i = j - 1
        # Insere o elemento ordenar[j] na posição correta.
        while i >= 0 and insercao[i] > chave:
            insercao[i + 1] = insercao[i]
            i = i - 1
        insercao[i + 1] = chave


def Sort(sort_1):#ordenar por sort
    sort_1.sort()

ordenar = 0
print("TAMANHOS: ")
print("100")
print("1000")
print("10000")
print()
print("COMANDOS: ")
print("Bolha = 1")
print("Selecao = 2")
print("Incercao = 3")
print("Sort = 4")
print("Parada/voutar para o menu inicial = 5")
print()
def Lista():#vai criar as listas.
    num_or = int(input("Digite o tamanho da lista: "))
    global ordenar
    if num_or==100:#tamho de 100 numeros
        ordenar = list(range(1,100))#gera os numeros.
        random.shuffle(ordenar)#enbaralha os numnero.
    elif num_or==1000:#tamho de 1000 numeros
        ordenar = list(range(1,1000))#gera os numeros.
        random.shuffle(ordenar)#enbaralha os numnero.
    elif num_or==10000:#tamho de 10000 numeros
        ordenar = list(range(1,10000))#gera os numeros.
        random.shuffle(ordenar)#enbaralha os numnero.


#escolher qual o tamanho da lista.
Lista()

#menu de escolha de ordenacao, para melhorar a imterface entre o usuario.
while True:
    menu = int(input("Qual comando vai usar: "))
    if menu==5:#Parada
        ordenar = 0
        print("Deseja encerar mesmo o programa ou fazer mais casos de testes?")
        print("sim ou não")
        #pergunta para o usuario se ele deseja continuar ou nao.
        res = input("R:")
        if res == "sim":
            print("Obrigado por usar")
            break
        elif res == "nao":
            #vai para a funcao, que faz a lista.
            print("vamos continuar")
            Lista()
    elif menu==1:#Bolha
        bolha = ordenar.copy()#faz acopia da lista principal
        ini = time.perf_counter()#contador
        Bolha(bolha)#chama a funçao
        fim = time.perf_counter()#contador
        print ("Função Bolha: ", fim-ini)
        
    elif menu==2:#selecao
        selecao = ordenar.copy()#faz acopia da lista principal
        ini = time.perf_counter()#contador
        Selecao(selecao)#chama a funçao
        fim = time.perf_counter()#contador
        print ("Função Seleção: ", fim-ini)
        
    elif menu==3:#incercao
        insercao = ordenar.copy()#faz acopia da lista principal
        ini = time.perf_counter()#contador
        Insercao(insercao)#chama a funçao
        fim = time.perf_counter()#contador
        print ("Função Inserção: ", fim-ini)
        
    elif menu==4:#sort
        sort_1 = ordenar.copy()#faz acopia da lista principal
        ini = time.perf_counter()#contador
        Sort(sort_1)#chama a funçao
        fim = time.perf_counter()#contador
        print ("Função Sort: ", fim-ini)
