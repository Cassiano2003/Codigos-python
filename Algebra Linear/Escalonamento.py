import os
import numpy as np

#Define se a matriz é quadrada ou nao
def modelamento(matriz):
    mat = []
    for chave in matriz:
        lista = []
        for letra in chave:
            if(letra != " "):
               lista.append(letra) 
        mat.append(lista)
    
    mat = np.array(mat)
    tamnho_x = len(mat)
    for frase in mat:
        tamnho_y = len(frase)
        if(tamnho_x != tamnho_y):
            print("A matriz nao é quadrada")
            return False
    return mat



def main():
    l = []
    os.system("clear")
    #Le a matriz do usuario
    while(True):
        variavel = input()
        if(variavel == ""):
            print("Fim!!!")
            break
        else:
            l.append(variavel)
    mat = modelamento(l)
    if(mat == False):
        return

main()