import random

quant = int(input())
lista = []
sim = True
i = 0

while i < quant:
    #print("teste")
    num = random.randrange(1,1000)
    for j in lista:
        if(j == num):
            sim = False
            break
    if(sim):
        lista.append(num)
        i += 1
    sim = True
print(lista)
print(i)