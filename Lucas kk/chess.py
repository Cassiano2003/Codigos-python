################################
# EM DESENVOLVIMENTO AINDA!!!! #
################################
import os
import random
import time
#os.system('color')

'''
class Peao():
    def __init__(self, cor, pos_x, pos_y, mov):
        self.img = '♙'
        self.cor = cor
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mov = mov

    def movimento(pos_x, pos_y, mov, cor):
        
    elif pe == '♙' or pe == '♟':
        if t[0] == 'B':
            #Ataque
            if y != 0:
                if jg[x+1][y-1] == 'W':
                    jg[x+1][y-1] = 'w'
            if y != 7:
                if jg[x+1][y+1] == 'W':
                    jg[x+1][y+1] = 'w'
            #Movimento
            if jg[x+1][y] == 'N':
                jg[x+1][y] = 'n'
                if pe == '♟' and jg[x+2][y] == 'N':
                    jg[x+2][y] = 'n'
        else:
            #Ataque
            if y != 0:
                if jg[x-1][y-1] == 'B':
                    jg[x-1][y-1] = 'b'
            if y != 7:
                if jg[x-1][y+1] == 'B':
                    jg[x-1][y+1] = 'b'
            #Movimento
            if jg[x-1][y] == 'N':
                jg[x-1][y] = 'n'
                if pe == '♟' and jg[x-2][y] == 'N':
                    jg[x-2][y] = 'n'    

p = Peao('W', i, j, 0)

lista.append(Peao('W', i, j, 0))

p.setMov(1)
'''

class colors:
    red = '\033[91m'
    RED = '\033[41m'
    green = '\033[32m'
    YELLOW = '\033[103m'
    yellow = '\033[33m'
    BLUE = '\033[46m'
    blue = '\033[94m'
    purple = '\033[95m'
    grey = '\033[90m'
    WHITE = '\033[107m'
    white = '\033[37m'
    fim = '\033[0m'

class Peao():
    def __init__(self, tipo, pos_x, pos_y, mov):
        self.img = '♙'
        self.tipo = tipo
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mov = mov

    def getTipo(self):
        return self.tipo
    
    def mudaTipo(self, atk):
        if atk:
            self.tipo = self.tipo.lower()
        else:
            self.tipo = self.tipo.upper()

    def getMove(self, tab):
        if self.tipo == 'B':
            #Ataque
            if self.pos_y != 0 and tab[self.pos_x+1][self.pos_y-1].getTipo() == 'W':
                tab[self.pos_x+1][self.pos_y-1].mudaTipo(1)
            if self.pos_y != 7 and tab[self.pos_x+1][self.pos_y+1].getTipo() == 'W':
                tab[self.pos_x+1][self.pos_y+1].mudaTipo(1)
            #Movimento
            if tab[self.pos_x+1][self.pos_y].getTipo() == 'N':
                tab[self.pos_x+1][self.pos_y].mudaTipo(1)
                if self.mov == 0 and tab[self.pos_x+2][self.pos_y].getTipo() == 'N':
                    tab[self.pos_x+2][self.pos_y].mudaTipo(1)
        else:
            #Ataque
            if self.pos_y != 0 and tab[self.pos_x-1][self.pos_y-1].getTipo() == 'B':
                tab[self.pos_x-1][self.pos_y-1].mudaTipo(1)
            if self.pos_y != 7 and tab[self.pos_x-1][self.pos_y+1].getTipo() == 'B':
                tab[self.pos_x-1][self.pos_y+1].mudaTipo(1)
            #Movimento
            if tab[self.pos_x-1][self.pos_y].getTipo() == 'N':
                tab[self.pos_x-1][self.pos_y].mudaTipo(1)
                if self.mov == 0 and tab[self.pos_x-2][self.pos_y].getTipo() == 'N':
                    tab[self.pos_x-2][self.pos_y].mudaTipo(1)
        
        return tab

def Escolha(n):
    e = 0
    l = []
    for i in range(1, n+1):
        l.append(str(i))
    while e not in l:
        print("-> ", end="")
        e = input()
    print()
    return e

def Posicao(jg, v):
    while True:
        print("-> ", end="")
        p1 = input()
        if len(p1) == 2:
            if 65 <= ord(p1[0]) <= 72 and 48 <= ord(p1[1]) <= 55:
                col = ord(p1[0]) - 65
                lin = int(p1[1])
                if jg[lin][col] in v:
                    break 
                else:
                    print("A coordenada inserida não pode ser usada.")
            else:
                print("Insira uma coordenada dentro do intervalo.") 
        else:
            print("Insira a coordenada corretamente.")

    return col, lin

def Verifica(jg, jg2, x, y, t):
    pe = jg2[x][y]
    #CAVALO
    if pe == '♞':
        #    x─┐
        #      │
        #      C
        if x > 1 and y != 0 and jg[x-2][y-1] not in t:
            jg[x-2][y-1] = jg[x-2][y-1].lower()
        #      ┌─x
        #      │ 
        #      C
        if x > 1 and y != 7 and jg[x-2][y+1] not in t:
            jg[x-2][y+1] = jg[x-2][y+1].lower()
        #      ┌───x
        #      C
        if x != 0 and y < 6 and jg[x-1][y+2] not in t:
            jg[x-1][y+2] = jg[x-1][y+2].lower()
        #      C
        #      └───x
        if x != 7 and y < 6 and jg[x+1][y+2] not in t:
            jg[x+1][y+2] = jg[x+1][y+2].lower()
        #      C
        #      │  
        #      └─x
        if x < 6 and y != 7 and jg[x+2][y+1] not in t:
            jg[x+2][y+1] = jg[x+2][y+1].lower()
        #      C
        #      │  
        #    x─┘ 
        if x < 6 and y != 0 and jg[x+2][y-1] not in t:
            jg[x+2][y-1] = jg[x+2][y-1].lower()
        #      C
        #  x───┘
        if x != 7 and y > 1 and jg[x+1][y-2] not in t:
            jg[x+1][y-2] = jg[x+1][y-2].lower()
        #  x───┐   
        #      C
        if x != 0 and y > 1 and jg[x-1][y-2] not in t:
            jg[x-1][y-2] = jg[x-1][y-2].lower()
    #PEÃO
    elif pe == '♙' or pe == '♟':
        if t[0] == 'B':
            #Ataque
            if y != 0:
                if jg[x+1][y-1] == 'W':
                    jg[x+1][y-1] = 'w'
            if y != 7:
                if jg[x+1][y+1] == 'W':
                    jg[x+1][y+1] = 'w'
            #Movimento
            if jg[x+1][y] == 'N':
                jg[x+1][y] = 'n'
                if pe == '♟' and jg[x+2][y] == 'N':
                    jg[x+2][y] = 'n'
        else:
            #Ataque
            if y != 0:
                if jg[x-1][y-1] == 'B':
                    jg[x-1][y-1] = 'b'
            if y != 7:
                if jg[x-1][y+1] == 'B':
                    jg[x-1][y+1] = 'b'
            #Movimento
            if jg[x-1][y] == 'N':
                jg[x-1][y] = 'n'
                if pe == '♟' and jg[x-2][y] == 'N':
                    jg[x-2][y] = 'n'
    #REI
    elif pe == '♔' or pe == '♚':
        if pe == '♔': # Não moveu o Rei
            if jg[x][y+1] == jg[x][y+2] == 'N' and jg2[x][y+3] == '♖':
                jg[x][y+2] = 'r'
            if jg[x][y-1] == jg[x][y-2] == jg[x][y-3] == 'N' and jg2[x][y-4] == '♖':
                jg[x][y-2] = 'R'

        if y != 0 and jg[x][y-1] not in t: #Esquerda
            jg[x][y-1] = jg[x][y-1].lower()
        if x != 0 and jg[x-1][y] not in t: #Cima
            jg[x-1][y] = jg[x-1][y].lower()
        if y != 7 and jg[x][y+1] not in t: #Direita
            jg[x][y+1] = jg[x][y+1].lower()
        if x != 7 and jg[x+1][y] not in t: #Baixo
            jg[x+1][y] = jg[x+1][y].lower()
    else:
        #TORRE OU RAINHA
        if pe != '♝':
            for i in range(1,8): #Cima
                if (x - i) < 0 or jg[x-i][y] in t:
                    break
                else:
                    jg[x-i][y] = jg[x-i][y].lower()
                    if jg[x-i][y] != 'n':
                        break
            for i in range(1,8): #Esquerda
                if (y - i) < 0 or jg[x][y-i] in t:
                    break
                else:
                    jg[x][y-i] = jg[x][y-i].lower()
                    if jg[x][y-i] != 'n':
                        break
            for i in range(1,8): #Baixo
                if (x + i) > 7 or jg[x+i][y] in t:
                    break
                else:
                    jg[x+i][y] = jg[x+i][y].lower()
                    if jg[x+i][y] != 'n':
                        break
            for i in range(1,8): #Direita
                if (y + i) > 7 or jg[x][y+i] in t:
                    break
                else:
                    jg[x][y+i] = jg[x][y+i].lower()
                    if jg[x][y+i] != 'n':
                        break
        #BISPO OU RAINHA
        if pe != '♜' and pe != '♖':
            for i in range(1,8): #Diagonal Superior Direita
                if (x - i) < 0 or (y + i) > 7 or jg[x-i][y+i] in t:
                    break
                else:
                    jg[x-i][y+i] = jg[x-i][y+i].lower()
                    if jg[x-i][y+i] != 'n':
                        break
            for i in range(1,8): #Diagonal Inferior Direita
                if (x + i) > 7 or (y + i) > 7 or jg[x+i][y+i] in t:
                    break
                else:
                    jg[x+i][y+i] = jg[x+i][y+i].lower()
                    if jg[x+i][y+i] != 'n':
                        break
            for i in range(1,8): #Diagonal Inferior Esquerda
                if (x + i) > 7 or (y - i) < 0 or jg[x+i][y-i] in t:
                    break
                else:
                    jg[x+i][y-i] = jg[x+i][y-i].lower()
                    if jg[x+i][y-i] != 'n':
                        break
            for i in range(1,8): #Diagonal Superior Esquerda
                if (x - i) < 0 or (y - i) < 0 or jg[x-i][y-i] in t:
                    break
                else:
                    jg[x-i][y-i] = jg[x-i][y-i].lower()
                    if jg[x-i][y-i] != 'n':
                        break
    return jg

def Posicao2(jg, t):
    while True:
        print("-> ", end="")
        p1 = input()
        if len(p1) == 2:
            if 65 <= ord(p1[0]) <= 72 and 48 <= ord(p1[1]) <= 55:
                col = ord(p1[0]) - 65
                lin = int(p1[1])
                if (jg[lin][col].islower() or jg[lin][col] == 'R') and jg[lin][col] != t[2]:
                    break 
                else:
                    print("A coordenada inserida não pode ser usada.")
            else:
                print("Insira uma coordenada dentro do intervalo.") 
        else:
            if p1 == 'V':
                col = lin = -1
                break
            else:
                print("Insira a coordenada corretamente.")

    return col, lin

def Verifica2(jg, jg2, x, y, x2, y2, p1, p2):
    if jg2[x][y] == '♟':
        jg2[x][y] = '♙'
    elif jg2[x][y] == '♔':
        jg2[x][y] = '♚'
    elif jg2[x][y] == '♖':
        jg2[x][y] = '♜'

    if jg[x2][y2] == 'r' or jg[x2][y2] == 'R':
        if jg[x2][y2] == 'r':
            jg[x2][y2-1] = jg[x2][y2+1]
            jg[x2][y2+1] = 'N'
            jg2[x2][y2-1] = '♜'
            jg2[x2][y2+1] = ' '
        else:
            jg[x2][y2+1] = jg[x2][y2-2]
            jg[x2][y2-2] = 'N'
            jg2[x2][y2+1] = '♜'
            jg2[x2][y2-2] = ' '
    elif jg[x2][y2] == 'w' or jg[x2][y2] == 'b':
        if jg[x2][y2] == 'w':
            p2.append(jg2[x2][y2])
            if jg2[x2][y2] == '♟' or jg2[x2][y2] == '♙':
                p2[0] += 1
            elif jg2[x2][y2] == '♞' or jg2[x2][y2] == '♝':
                p2[0] += 3
            elif jg2[x2][y2] == '♖' or jg2[x2][y2] == '♜':
                p2[0] += 5
            elif jg2[x2][y2] == '♛':
                p2[0] += 9
        elif jg[x2][y2] == 'b':
            if jg2[x2][y2] == '♟' or jg2[x2][y2] == '♙':
                jg2[x2][y2] = '♙'
                p1[0] += 1
            elif jg2[x2][y2] == '♞' or jg2[x2][y2] == '♝':
                p1[0] += 3
            elif jg2[x2][y2] == '♖' or jg2[x2][y2] == '♜':
                jg2[x2][y2] == '♜'
                p1[0] += 5
            elif jg2[x2][y2] == '♛':
                p1[0] += 9
            p1.append(jg2[x2][y2])
    jg[x2][y2] = jg[x][y]
    jg[x][y] = 'N'
    jg2[x2][y2] = jg2[x][y]
    jg2[x][y] = ' '

    for i in range(8):
        for j in range(8):
            if jg[i][j] == 'n' or jg[i][j] == 'r' or jg[i][j] == 'R':
                jg[i][j] = 'N'
            else:
                jg[i][j] = jg[i][j].upper()

    return jg, jg2, p1, p2

def ImprimeJogo(jg, jg2, p1, p2):
    pt1 = 0
    pt2 = 0
    print(colors.yellow + "            PLACAR")
    if p1[0] > 9:
        print(colors.green + "          %d" %p1[0], end="")
    else:
        print(colors.green + "           %d" %p1[0], end="")
    print(colors.yellow + "  --" + colors.red + "  %d" %p2[0] + colors.fim)
    print("    A  B  C  D  E  F  G  H")
    print("  ╔════════════════════════╗")
    for i in range(8):
        print("%d ║" %i, end="")
        for j in range(8):
            if (j % 2 == 0 and i % 2 == 0) or (j % 2 != 0 and i % 2 != 0):
                print(colors.WHITE, end="")
            if jg[i][j] == 'B' or jg[i][j] == 'KB':
                print(colors.red, end="")
            elif jg[i][j] == 'W' or jg[i][j] == 'KW':
                print(colors.green, end="")
            elif jg[i][j] == 'b' or jg[i][j] == 'w':
                print(colors.BLUE + colors.white, end="")
            elif jg[i][j] == 'kb' or jg[i][j] == 'kw':
                print(colors.YELLOW, end="")
                if jg[i][j] == 'kb':
                    print(colors.red, end="")
                else:
                    print(colors.green, end="")
            if jg2[i][j] == '♖':
                print(" ♜ " + colors.fim, end="")
            elif jg2[i][j] == '♔':
                print(" ♚ " + colors.fim, end="")
            elif jg2[i][j] == '♟':
                print(" ♙ " + colors.fim, end="")
            elif jg[i][j] == 'n':
                print(colors.purple + " • " + colors.fim, end="")
            elif jg[i][j] == 'r' or jg[i][j] == 'R':
                print(colors.purple + " ○ " + colors.fim, end="")
            else:
                print(" %s " %jg2[i][j] + colors.fim, end="")
        print("║", end="")
        if 0 <= i <= 2:
            if len(p2)-1 < 5 and i == 0:
                for v in range(len(p2)-1):
                    pt2 += 1
                    print(colors.green + " %s" %p2[pt2], end="")
            elif len(p2)-1 >= 5:
                for v in range(5):
                    if pt2 == len(p2)-1:
                        break
                    pt2 += 1
                    print(colors.green + " %s" %p2[pt2], end="")
        elif 5 <= i <= 7:
            if len(p1)-1 < 5 and i == 5:
                for v in range(len(p1)-1):
                    pt1 += 1
                    print(colors.red + " %s" %p1[pt1], end="")
            elif len(p1)-1 >= 5:
                for v in range(5):
                    if pt1 == len(p1)-1:
                        break
                    pt1 += 1
                    print(colors.red + " %s" %p1[pt1], end="")
        print(colors.fim)            
    print("  ╚════════════════════════╝")

def main():
    print("------ XADREZ ------")
    print()
    while True:
        print("========= OPÇÕES =========")
        print("[1] Jogar   [2] Instruções")
        print("        [3] Sair")
        e = Escolha(3)
        if e == '3':
            print("ENCERRANDO JOGO...")
            break
        elif e == '2':
            print("========== INSTRUÇÕES ==========")
            print()
            print("- Batalha Naval é um jogo onde ambos os jogadores deverão posicionar suas frotas navais em diferentes")
            print("  coordenadas, e após isso cada um deverá adivinhar onde o outro jogador posicionou sua frota. Ganha quem")
            print("  encontrar todas as frotas do outro jogador.")
            print("- Para começar, o jogador será apresentado a quantidade de unidades sua frota possui, juntamente também")
            print("  do tamanho que aquela unidade ocupará no mapa, sendo representado pelo símbolo (O), onde o número de")
            print("  'O's indica o tamanho que a unidade ocupa.")
            print("- Para posicionar sua frota é necessário fornecer as coordenadas em que sua unidade será posicionada, o")
            print("  posicionamento ocorre sempre da esquerda para a direita ou de cima para baixo, ou seja, caso você")
            print("  escolha uma unidade de tamanho 4 e escolha a coordenada 'B3' na vertical, isso significa que a unidade")
            print("  ocupará os espaços B3, B4, B5 e B6, e caso você escolha a coordenada 'B3' na horizontal, a unidade ocupará")
            print("  os espaços B3, C3, D3 e E3.")
            print()
        elif e == '1':
            '''
            jg1 = [['♙', 0,6, 0], ['♙', 1,6, 0], ['♙', 2,6, 0], ['♙', 3,6, 0], ['♙', 4,6, 0], ['♙', 5,6, 0], ['♙', 6,6, 0], ['♙', 7,6, 0],
                   ['♜', 0,7, 0], ['♞', 1,7, 0], ['♝', 2,7, 0], ['♛', 3,7, 0], ['♚', 4,7, 0], ['♝', 5,7, 0], ['♞', 6,7, 0], ['♜', 7,7, 0]]
            jg2 = [['♙', 0,1, 0], ['♙', 1,1, 0], ['♙', 2,1, 0], ['♙', 3,1, 0], ['♙', 4,1, 0], ['♙', 5,1, 0], ['♙', 6,1, 0], ['♙', 7,1, 0],
                   ['♜', 0,0, 0], ['♞', 1,0, 0], ['♝', 2,0, 0], ['♛', 3,0, 0], ['♚', 4,0, 0], ['♝', 5,0, 0], ['♞', 6,0, 0], ['♜', 7,0, 0]]
            '''
            peças = ['♖','♞','♝','♛','♔','♝','♞','♖']
            pts1 = [0]
            pts2 = [0]
            jg = []
            jg2 = []
            print(colors.yellow + "            PLACAR")
            if pts1[0] > 9:
                print(colors.green + "          %d" %pts1[0], end="")
            else:
                print(colors.green + "           %d" %pts1[0], end="")
            print(colors.yellow + "  --" + colors.red + "  %d" %pts2[0] + colors.fim)
            print("    A  B  C  D  E  F  G  H")
            print("  ╔════════════════════════╗")
            for i in range(8):
                jg.append([])
                jg2.append([])
                print("%d ║" %i, end="")
                for j in range(8):
                    if i < 2:
                        jg[i].append('B')
                        jg2[i].append('♟')
                        if i == 0:
                            jg2[i][j] = peças[j]
                            if jg2[i][j] == '♔':
                                jg[i][j] = 'KB'
                    elif i > 5:
                        jg[i].append('W')
                        jg2[i].append('♟')
                        if i == 7:
                            jg2[i][j] = peças[j]
                            if jg2[i][j] == '♔':
                                jg[i][j] = 'KW'
                    else:
                        jg[i].append('N')
                        jg2[i].append(' ')
                    if (j % 2 == 0 and i % 2 == 0) or (j % 2 != 0 and i % 2 != 0):
                        print(colors.WHITE, end="")
                    if jg[i][j] == 'B' or jg[i][j] == 'KB':
                        print(colors.red, end="")
                    elif jg[i][j] == 'W' or jg[i][j] == 'KW':
                        print(colors.green, end="")
                    if jg2[i][j] == '♖':
                        print(" ♜ " + colors.fim, end="")
                    elif jg2[i][j] == '♔':
                        print(" ♚ " + colors.fim, end="")
                    elif jg2[i][j] == '♟':
                        print(" ♙ " + colors.fim, end="")
                    else:
                        print(" %s " %jg2[i][j] + colors.fim, end="")
                print("║")
            print("  ╚════════════════════════╝")
            print(colors.green + "VERDES COMEÇAM" + colors.fim)
            t = ['W', 'KW', 'kw']
            while True:
                print("Escolha as coordenadas que deseja jogar: (letra primeiro, depois o número)")
                while True:
                    conf = 0
                    y, x = Posicao(jg, t)
                    jg = Verifica(jg, jg2, x, y, t)
                    for i in jg:
                        if 'n' in i or 'b' in i or 'w' in i:
                            conf = 1
                            break
                    if conf:
                        break
                    print("A peça escolhida não tem como se mover.")
                ImprimeJogo(jg, jg2, pts1, pts2)
                print("Informe a próxima jogada ou digite 'V' para voltar e escolher outra peça")
                y2, x2 = Posicao2(jg, t)
                if x2 == y2 == -1:
                    for i in range(8):
                        for j in range(8):
                            if jg[i][j] == 'n' or jg[i][j] == 'r' or jg[i][j] == 'R':
                                jg[i][j] = 'N'
                            else:
                                jg[i][j] = jg[i][j].upper()
                    ImprimeJogo(jg, jg2, pts1, pts2)
                    continue
                jg, jg2, pts1, pts2 = Verifica2(jg, jg2, x, y, x2, y2, pts1, pts2)
                ImprimeJogo(jg, jg2, pts1, pts2)

                conf = 0
                for i in jg:
                    if 'KW' in i:
                        conf += 1
                    if 'KB' in i:
                        conf += 2
                    if conf == 3:
                        break
                if conf == 3:
                    if t[0] == 'W':
                        t = ['B', 'KB', 'kb']
                        print(colors.red + "VERMELHAS JOGAM" + colors.fim)
                    else:
                        t = ['W', 'KW', 'kw']
                        print(colors.green + "VERDES JOGAM" + colors.fim)
                elif conf == 2:
                    print(colors.red + "VITÓRIA DAS VERMELHAS!!" + colors.fim)
                    break
                elif conf == 1:
                    print(colors.green + "VITÓRIA DAS VERDES!!" + colors.fim)
                    break

            print("[1] Jogar Novamente   [2] Sair")
            if Escolha(2) == '2':
                print("ENCERRANDO JOGO...")
                break
            else:
                print("INICIANDO NOVO JOGO...")
                print()

main()