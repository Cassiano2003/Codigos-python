import numpy as np

def escalona(vet, i):
    mult = vet[i+1][i]/vet[i][i]
    for j in range(len(vet)):
        lista = []
        for c in range(len(vet)):
            if j > c:
                vet[j] = vet[j] - (mult*vet[i])

    print(vet)

def sobe(vet,j):
    maior = -1
    j_1 = -1
    for i in range(j,):
        if vet[i][j] >= maior and i != j:
            maior = vet[i][j]
            j_1 = i

    aux = []
    for i in range(len(vet)):
        aux.append(vet[j][i])
    vet[j] = vet[j_1]
    vet[j_1] = aux
    
'''mat = []

for i in range(2):
    l = []
    for j in range(2):
        l.append(int(input()))

    mat.append(l)

mat = np.array(mat)'''

mat = np.array([[1,2,3],[3,4,5],[6,7,8]])
print(mat)
for i in range(2):
    sobe(mat,i)
    escalona(mat,i)
    print(mat)
