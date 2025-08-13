#Biliotecas
import os
#Comando para limpar o terminal para ficar mais legivel as instruçoes
os.system("clear")
#Listas de x e y, que iram guardar os valores 
x = []
y = []

#Quantidade de valores
quanti =3 #int(input("Digite a quantidade dados: "))
poli = quanti - 1

#Pede os valores de X
print("Digite os valores de X:")
for i in range(quanti):
    print("Digite o ",i+1,"°",end=": ")
    aux = float(input())
    x.append(aux)

#Pede os valores de Y
print("Digite os valores de Y:")
for i in range(quanti):
    print("Digite o ",i+1,"°",end=": ")
    aux = float(input())
    y.append(aux)

#Tabela de valore
tabela = []
#Ja coloco os valores de y
tabela.append(y)


#For que faz o caminhar nas ordens
for i in range(1,quanti):
    lista = []
    #Calcula cada coluda da orden que i coloca
    for j in range(len(tabela[i-1])-1):
        #Adiciona em uma lista auciliar para depois colocar na matriz
        lista.append((tabela[i-1][j+1]-tabela[i-1][j])/(x[j+i]-x[j]))

    tabela.append(lista)

#Pede o valor que o usuario queira encontrar
x_valor = float(input("Insira o valor que queira calcular no polinomio: "))

#Cria uma lista q vai compor o valores do polinomio
polinomio = []
for i in range(quanti):
    polinomio.append(tabela[i][0])

#Faz os calculos com os valores e gera o resultado
soma = 0
for i in range(quanti):
    s = 1
    for j in range(i):
        s *= (x_valor - x[j])
    soma += (polinomio[i] * s)

#Imprime a tabela para ficar mais legivel 
print("Tabela: ")
esp = " "
num = 31
for i in range(quanti):
    print(esp * (i*2),"Ordem:",i,end="")
    for j in range(len(tabela[i])):
        print(esp * (i),f'\033[{num}m{tabela[i][j]:.4f}\033[0m', end=" ")
    num += 1
    print(esp * (200))

print(f'\033[31mValor do \033[0mX = {x_valor}\033[31m no polinomio é: \033[0m{soma:.4f}')
#px = f[x0] + f[x1,x0](x - x0) + + f[x1,x0,x2](x - x0)(x - x1)