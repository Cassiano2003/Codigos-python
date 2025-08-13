def cria_lista(num):
    num_lista = []
    while num != 0:
        num_lista.append(num%10)
        num = num//10
    return num_lista

def ordena(num_lista):
    tamanho = len(num_lista)
    for i in range(tamanho-1):
        for j in range(i+1,tamanho):
            if(num_lista[i] > num_lista[j]):
                temp = num_lista[i]
                num_lista[i] = num_lista[j]
                num_lista[j] = temp
                #print(num_lista)
    return num_lista

num = int(input("Digite o seu numero: "))
lista = cria_lista(num)

print(lista)
print(ordena(lista))