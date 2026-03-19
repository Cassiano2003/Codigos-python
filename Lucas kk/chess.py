################################
# EM DESENVOLVIMENTO AINDA!!!! #
################################
import os
os.system('color')

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
    invi = '\033[08m'
    fim = '\033[0m'

class Peao():
    def __init__(self, tipo, cor, pos_x, pos_y, mov):
        self.img = '♙'
        self.Pts = 1
        self.tipo = tipo
        self.cor = cor
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mov = mov
        self.lista = []

    def mudaTipo(self, atk):
        if atk:
            self.tipo = self.tipo.lower()
        else:
            self.tipo = self.tipo.upper()

    def setPos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def getMove(self, tab):
        self.lista = []
        if self.cor == colors.red:
            #Ataque
            if self.pos_y != 0 and tab[self.pos_x+1][self.pos_y-1].cor == colors.green:
                self.lista.append([self.pos_x+1, self.pos_y-1])
            if self.pos_y != 7 and tab[self.pos_x+1][self.pos_y+1].cor == colors.green:
                self.lista.append([self.pos_x+1, self.pos_y+1])
            #Movimento
            if tab[self.pos_x+1][self.pos_y].tipo == 'N':
                self.lista.append([self.pos_x+1, self.pos_y])
                if self.mov == 0 and tab[self.pos_x+2][self.pos_y].tipo == 'N':
                    self.lista.append([self.pos_x+2, self.pos_y])
        else:
            #Ataque
            if self.pos_y != 0 and tab[self.pos_x-1][self.pos_y-1].cor == colors.red:
                self.lista.append([self.pos_x-1, self.pos_y-1])
            if self.pos_y != 7 and tab[self.pos_x-1][self.pos_y+1].cor == colors.red:
                self.lista.append([self.pos_x-1, self.pos_y+1])
            #Movimento
            if tab[self.pos_x-1][self.pos_y].tipo == 'N':
                self.lista.append([self.pos_x-1, self.pos_y])
                if self.mov == 0 and tab[self.pos_x-2][self.pos_y].tipo == 'N':
                    self.lista.append([self.pos_x-2, self.pos_y])
        
        return tab

    def setMove(self, tab):
        for i in self.lista:
            tab[i[0]][i[1]].mudaTipo(1)

    def Promo(self, tab):
        print("Promoção do Peão - Escolha qual usar:")
        print("[1] " + self.cor + "♞" + colors.fim + "    [2] " + self.cor + "♝" + colors.fim + "    [3] " + self.cor + "♜" + colors.fim + "    [4] " + self.cor + "♛" + colors.fim)
        e = Escolha(4)
        if e == '1':
            tab[self.pos_x][self.pos_y] = Cavalo(self.tipo, self.cor, self.pos_x, self.pos_y, 1)
        elif e == '2':
            tab[self.pos_x][self.pos_y] = Bispo(self.tipo, self.cor, self.pos_x, self.pos_y, 1)
        elif e == '3':
            tab[self.pos_x][self.pos_y] = Torre(self.tipo, self.cor, self.pos_x, self.pos_y, 1)
        else:
            tab[self.pos_x][self.pos_y] = Rainha(self.tipo, self.cor, self.pos_x, self.pos_y, 1)
        
        return tab

    def Movimento(self, tab, x, y):
        self.mov = 1

        tab[x][y] = tab[self.pos_x][self.pos_y]
        tab[self.pos_x][self.pos_y] = Vazio(self.pos_x, self.pos_y)
        tab[x][y].setPos(x, y)
        if x == 0 or x == 7:
            tab = tab[x][y].Promo(tab)
        
        return tab

class Rei():
    def __init__(self, tipo, cor, pos_x, pos_y, mov):
        self.img = '♚'
        self.Pts = 0
        self.tipo = tipo
        self.cor = cor
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mov = mov
        self.lista = []

    def mudaTipo(self, atk):
        if atk:
            self.tipo = self.tipo.lower()
        else:
            self.tipo = self.tipo.upper()

    def setPos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def getMove(self, tab):
        self.lista = []
        if not self.mov: # Não moveu o Rei
            if tab[self.pos_x][self.pos_y+1].tipo == tab[self.pos_x][self.pos_y+2].tipo == 'N' and not tab[self.pos_x][self.pos_y+3].mov:
                tab[self.pos_x][self.pos_y+2].tipo = 'r'
                tab[self.pos_x][self.pos_y+2].img = '○'
                self.lista.append([self.pos_x, self.pos_y+2])
            if tab[self.pos_x][self.pos_y-1].tipo == tab[self.pos_x][self.pos_y-2].tipo == tab[self.pos_x][self.pos_y-3].tipo == 'N' and not tab[self.pos_x][self.pos_y-4].mov:
                tab[self.pos_x][self.pos_y-2].tipo = 'R'
                tab[self.pos_x][self.pos_y-2].img = '○'
                self.lista.append([self.pos_x, self.pos_y-2])

        if self.pos_y != 0 and tab[self.pos_x][self.pos_y-1].cor != self.cor: #Esquerda
            self.lista.append([self.pos_x, self.pos_y-1])
        if self.pos_x != 0 and tab[self.pos_x-1][self.pos_y].cor != self.cor: #Cima
            self.lista.append([self.pos_x-1, self.pos_y])
        if self.pos_y != 7 and tab[self.pos_x][self.pos_y+1].cor != self.cor: #Direita
            self.lista.append([self.pos_x, self.pos_y+1])
        if self.pos_x != 7 and tab[self.pos_x+1][self.pos_y].cor != self.cor: #Baixo
            self.lista.append([self.pos_x+1, self.pos_y])

        if self.pos_y != 0 and self.pos_x != 0 and tab[self.pos_x-1][self.pos_y-1].cor != self.cor: #Diagonal Superior Esquerda
            self.lista.append([self.pos_x-1, self.pos_y-1])
        if self.pos_x != 0 and self.pos_y != 7 and tab[self.pos_x-1][self.pos_y+1].cor != self.cor: #Diagonal Superior Direita
            self.lista.append([self.pos_x-1, self.pos_y+1])
        if self.pos_y != 7 and self.pos_x != 7 and tab[self.pos_x+1][self.pos_y+1].cor != self.cor: #Diagonal Inferior Direita
            self.lista.append([self.pos_x+1, self.pos_y+1])
        if self.pos_x != 7 and self.pos_y != 0 and tab[self.pos_x+1][self.pos_y-1].cor != self.cor: #Diagonal Inferior Esquerda
            self.lista.append([self.pos_x+1, self.pos_y-1])
        
        return tab
    
    def setMove(self, tab):
        for i in self.lista:
            if tab[i[0]][i[1]].img != '○':
                tab[i[0]][i[1]].mudaTipo(1)

    def Movimento(self, tab, x, y):
        self.mov = 1
        if tab[x][y].img == '○':
            if tab[x][y].tipo == 'r':
                tab[x][y-1] = tab[x][y+1]
                tab[x][y-1].setPos(x, y-1)
                tab[x][y-1].mov = 1
                tab[x][y+1] = Vazio(x, y+1)
            else:
                tab[x][y+1] = tab[x][y-2]
                tab[x][y+1].setPos(x, y+1)
                tab[x][y+1].mov = 1
                tab[x][y-2] = Vazio(x, y-2)

        tab[x][y] = tab[self.pos_x][self.pos_y]
        tab[self.pos_x][self.pos_y] = Vazio(self.pos_x, self.pos_y)
        tab[x][y].setPos(x, y)

        return tab

class Cavalo():
    def __init__(self, tipo, cor, pos_x, pos_y, mov):
        self.img = '♞'
        self.Pts = 3
        self.tipo = tipo
        self.cor = cor
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mov = mov
        self.lista = []

    def mudaTipo(self, atk):
        if atk:
            self.tipo = self.tipo.lower()
        else:
            self.tipo = self.tipo.upper()

    def setPos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def getMove(self, tab):
        self.lista = []
        #    x─┐
        #      │
        #      C
        if self.pos_x > 1 and self.pos_y != 0 and tab[self.pos_x-2][self.pos_y-1].cor != self.cor:
            self.lista.append([self.pos_x-2, self.pos_y-1])
        #      ┌─x
        #      │ 
        #      C
        if self.pos_x > 1 and self.pos_y != 7 and tab[self.pos_x-2][self.pos_y+1].cor != self.cor:
            self.lista.append([self.pos_x-2, self.pos_y+1])
        #      ┌───x
        #      C
        if self.pos_x != 0 and self.pos_y < 6 and tab[self.pos_x-1][self.pos_y+2].cor != self.cor:
            self.lista.append([self.pos_x-1, self.pos_y+2])
        #      C
        #      └───x
        if self.pos_x != 7 and self.pos_y < 6 and tab[self.pos_x+1][self.pos_y+2].cor != self.cor:
            self.lista.append([self.pos_x+1, self.pos_y+2])
        #      C
        #      │  
        #      └─x
        if self.pos_x < 6 and self.pos_y != 7 and tab[self.pos_x+2][self.pos_y+1].cor != self.cor:
            self.lista.append([self.pos_x+2, self.pos_y+1])
        #      C
        #      │  
        #    x─┘ 
        if self.pos_x < 6 and self.pos_y != 0 and tab[self.pos_x+2][self.pos_y-1].cor != self.cor:
            self.lista.append([self.pos_x+2, self.pos_y-1])
        #      C
        #  x───┘
        if self.pos_x != 7 and self.pos_y > 1 and tab[self.pos_x+1][self.pos_y-2].cor != self.cor:
            self.lista.append([self.pos_x+1, self.pos_y-2])
        #  x───┐   
        #      C
        if self.pos_x != 0 and self.pos_y > 1 and tab[self.pos_x-1][self.pos_y-2].cor != self.cor:
            self.lista.append([self.pos_x-1, self.pos_y-2])
        
        return tab

    def setMove(self, tab):
        for i in self.lista:
            tab[i[0]][i[1]].mudaTipo(1)

    def Movimento(self, tab, x, y):
        tab[x][y] = tab[self.pos_x][self.pos_y]
        tab[self.pos_x][self.pos_y] = Vazio(self.pos_x, self.pos_y)
        tab[x][y].setPos(x, y)

        return tab


class Bispo():
    def __init__(self, tipo, cor, pos_x, pos_y, mov):
        self.img = '♝'
        self.Pts = 3
        self.tipo = tipo
        self.cor = cor
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mov = mov
        self.lista = []

    def mudaTipo(self, atk):
        if atk:
            self.tipo = self.tipo.lower()
        else:
            self.tipo = self.tipo.upper()

    def setPos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def getMove(self, tab):
        self.lista = []
        for i in range(1,8): #Diagonal Superior Direita
            if (self.pos_x - i) < 0 or (self.pos_y + i) > 7 or tab[self.pos_x-i][self.pos_y+i].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x-i, self.pos_y+i])
                if tab[self.pos_x-i][self.pos_y+i].tipo != 'N':
                    break
        for i in range(1,8): #Diagonal Inferior Direita
            if (self.pos_x + i) > 7 or (self.pos_y + i) > 7 or tab[self.pos_x+i][self.pos_y+i].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x+i, self.pos_y+i])
                if tab[self.pos_x+i][self.pos_y+i].tipo != 'N':
                    break
        for i in range(1,8): #Diagonal Inferior Esquerda
            if (self.pos_x + i) > 7 or (self.pos_y - i) < 0 or tab[self.pos_x+i][self.pos_y-i].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x+i, self.pos_y-i])
                if tab[self.pos_x+i][self.pos_y-i].tipo != 'N':
                    break
        for i in range(1,8): #Diagonal Superior Esquerda
            if (self.pos_x - i) < 0 or (self.pos_y - i) < 0 or tab[self.pos_x-i][self.pos_y-i].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x-i, self.pos_y-i])
                if tab[self.pos_x-i][self.pos_y-i].tipo != 'N':
                    break

        return tab
    
    def setMove(self, tab):
        for i in self.lista:
            tab[i[0]][i[1]].mudaTipo(1)

    def Movimento(self, tab, x, y):
        tab[x][y] = tab[self.pos_x][self.pos_y]
        tab[self.pos_x][self.pos_y] = Vazio(self.pos_x, self.pos_y)
        tab[x][y].setPos(x, y)

        return tab
    
class Torre():
    def __init__(self, tipo, cor, pos_x, pos_y, mov):
        self.img = '♜'
        self.Pts = 5
        self.tipo = tipo
        self.cor = cor
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mov = mov
        self.lista = []

    def mudaTipo(self, atk):
        if atk:
            self.tipo = self.tipo.lower()
        else:
            self.tipo = self.tipo.upper()

    def setPos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def getMove(self, tab):
        self.lista = []
        for i in range(1,8): #Cima
            if (self.pos_x - i) < 0 or tab[self.pos_x-i][self.pos_y].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x-i, self.pos_y])
                if tab[self.pos_x-i][self.pos_y].tipo != 'N':
                    break
        for i in range(1,8): #Esquerda
            if (self.pos_y - i) < 0 or tab[self.pos_x][self.pos_y-i].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x, self.pos_y-i])
                if tab[self.pos_x][self.pos_y-i].tipo != 'N':
                    break
        for i in range(1,8): #Baixo
            if (self.pos_x + i) > 7 or tab[self.pos_x+i][self.pos_y].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x+i, self.pos_y])
                if tab[self.pos_x+i][self.pos_y].tipo != 'N':
                    break
        for i in range(1,8): #Direita
            if (self.pos_y + i) > 7 or tab[self.pos_x][self.pos_y+i].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x, self.pos_y+i])
                if tab[self.pos_x][self.pos_y+i].tipo != 'N':
                    break

        return tab
    
    def setMove(self, tab):
        for i in self.lista:
            tab[i[0]][i[1]].mudaTipo(1)

    def Movimento(self, tab, x, y):
        self.mov = 1
        tab[x][y] = tab[self.pos_x][self.pos_y]
        tab[self.pos_x][self.pos_y] = Vazio(self.pos_x, self.pos_y)
        tab[x][y].setPos(x, y)

        return tab

class Rainha():
    def __init__(self, tipo, cor, pos_x, pos_y, mov):
        self.img = '♛'
        self.Pts = 9
        self.tipo = tipo
        self.cor = cor
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mov = mov
        self.lista = []

    def mudaTipo(self, atk):
        if atk:
            self.tipo = self.tipo.lower()
        else:
            self.tipo = self.tipo.upper()

    def setPos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def getMove(self, tab):
        self.lista = []
        for i in range(1,8): #Cima
            if (self.pos_x - i) < 0 or tab[self.pos_x-i][self.pos_y].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x-i, self.pos_y])
                if tab[self.pos_x-i][self.pos_y].tipo != 'N':
                    break
        for i in range(1,8): #Esquerda
            if (self.pos_y - i) < 0 or tab[self.pos_x][self.pos_y-i].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x, self.pos_y-i])
                if tab[self.pos_x][self.pos_y-i].tipo != 'N':
                    break
        for i in range(1,8): #Baixo
            if (self.pos_x + i) > 7 or tab[self.pos_x+i][self.pos_y].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x+i, self.pos_y])
                if tab[self.pos_x+i][self.pos_y].tipo != 'N':
                    break
        for i in range(1,8): #Direita
            if (self.pos_y + i) > 7 or tab[self.pos_x][self.pos_y+i].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x, self.pos_y+i])
                if tab[self.pos_x][self.pos_y+i].tipo != 'N':
                    break

        for i in range(1,8): #Diagonal Superior Direita
            if (self.pos_x - i) < 0 or (self.pos_y + i) > 7 or tab[self.pos_x-i][self.pos_y+i].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x-i, self.pos_y+i])
                if tab[self.pos_x-i][self.pos_y+i].tipo != 'N':
                    break
        for i in range(1,8): #Diagonal Inferior Direita
            if (self.pos_x + i) > 7 or (self.pos_y + i) > 7 or tab[self.pos_x+i][self.pos_y+i].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x+i, self.pos_y+i])
                if tab[self.pos_x+i][self.pos_y+i].tipo != 'N':
                    break
        for i in range(1,8): #Diagonal Inferior Esquerda
            if (self.pos_x + i) > 7 or (self.pos_y - i) < 0 or tab[self.pos_x+i][self.pos_y-i].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x+i, self.pos_y-i])
                if tab[self.pos_x+i][self.pos_y-i].tipo != 'N':
                    break
        for i in range(1,8): #Diagonal Superior Esquerda
            if (self.pos_x - i) < 0 or (self.pos_y - i) < 0 or tab[self.pos_x-i][self.pos_y-i].cor == self.cor:
                break
            else:
                self.lista.append([self.pos_x-i, self.pos_y-i])
                if tab[self.pos_x-i][self.pos_y-i].tipo != 'N':
                    break

        return tab
    
    def setMove(self, tab):
        for i in self.lista:
            tab[i[0]][i[1]].mudaTipo(1)

    def Movimento(self, tab, x, y):
        tab[x][y] = tab[self.pos_x][self.pos_y]
        tab[self.pos_x][self.pos_y] = Vazio(self.pos_x, self.pos_y)
        tab[x][y].setPos(x, y)

        return tab

class Vazio():
    def __init__(self, pos_x, pos_y):
        self.img = ' '
        self.tipo = 'N'
        self.cor = colors.purple
        self.pos_x = pos_x
        self.pos_y = pos_y

    def mudaTipo(self, atk):
        if atk:
            self.tipo = self.tipo.lower()
            self.img = '•'
        else:
            self.tipo = self.tipo.upper()
            if self.tipo == 'R':
                self.tipo = 'N'
            self.img = ' '

    def setPos(self, x, y):
        self.pos_x = x
        self.pos_y = y

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
                if jg[lin][col].cor == v:
                    break 
                else:
                    print("A coordenada inserida não pode ser usada.")
            else:
                print("Insira uma coordenada dentro do intervalo.") 
        else:
            print("Insira a coordenada corretamente.")

    return col, lin

def Posicao2(tab, t):
    while True:
        print("-> ", end="")
        p1 = input()
        if len(p1) == 2:
            if 65 <= ord(p1[0]) <= 72 and 48 <= ord(p1[1]) <= 55:
                col = ord(p1[0]) - 65
                lin = int(p1[1])
                if (tab[lin][col].tipo.islower() or tab[lin][col].tipo == 'R') and tab[lin][col].cor != t:
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

def verificaXeque(tab, x, y):
    verifica = Peao(tab[x][y].tipo, tab[x][y].cor, x, y, tab[x][y].mov)
    verifica.getMove(tab)
    for i in verifica.lista:
        if tab[i[0]][i[1]].img != '♜' and tab[i[0]][i[1]].img != '♞' and tab[i[0]][i[1]].cor != colors.purple:
            tab[x][y].mudaTipo(1)
            return 0
        
    verifica = Cavalo(tab[x][y].tipo, tab[x][y].cor, x, y, tab[x][y].mov)
    verifica.getMove(tab)
    for i in verifica.lista:
        if tab[i[0]][i[1]].img == '♞':
            tab[x][y].mudaTipo(1)
            return 0
        
    verifica = Torre(tab[x][y].tipo, tab[x][y].cor, x, y, tab[x][y].mov)
    verifica.getMove(tab)
    for i in verifica.lista:
        if tab[i[0]][i[1]].img == '♜' or tab[i[0]][i[1]].img == '♛' or tab[i[0]][i[1]].img == '♚':
            if tab[i[0]][i[1]].img == '♚' and (abs(i[0]-x) > 1 or abs(i[1]-y) > 1):
                return 1
            tab[x][y].mudaTipo(1)
            return 0
        
    verifica = Bispo(tab[x][y].tipo, tab[x][y].cor, x, y, tab[x][y].mov)
    verifica.getMove(tab)
    for i in verifica.lista:
        if tab[i[0]][i[1]].img == '♝' or tab[i[0]][i[1]].img == '♛' or tab[i[0]][i[1]].img == '♚':
            if tab[i[0]][i[1]].img == '♚' and abs(i[0]-x) != abs(i[1]-y) != 1:
                return 1
            tab[x][y].mudaTipo(1)
            return 0

    return 1

def ImprimeJogo(tab, p1, p2):
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
            if tab[i][j].tipo == 'w' or tab[i][j].tipo == 'b':
                print(colors.BLUE + colors.white + " %s " %tab[i][j].img + colors.fim, end="")
            else:
                if tab[i][j].tipo == 'kw' or tab[i][j].tipo == 'kb':
                    print(colors.YELLOW, end="")
                print("%s %s " %(tab[i][j].cor, tab[i][j].img) + colors.fim, end="")

        print("║", end="")
        if 0 <= i <= 2:
            for v in range(5):
                if pt2 == len(p2)-1:
                    break
                pt2 += 1
                print(colors.green + " %s" %p2[pt2], end="")
        elif 5 <= i <= 7:
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
            peças = ['♜','♞','♝','♛','♚','♝','♞','♜']
            pts1 = [0]
            pts2 = [0]
            tab = []
            t = [colors.red, 'B', 'KB']
            print(colors.yellow + "            PLACAR")
            if pts1[0] > 9:
                print(colors.green + "          %d" %pts1[0], end="")
            else:
                print(colors.green + "           %d" %pts1[0], end="")
            print(colors.yellow + "  --" + colors.red + "  %d" %pts2[0] + colors.fim)
            print("    A  B  C  D  E  F  G  H")
            print("  ╔════════════════════════╗")
            for i in range(8):
                tab.append([])
                print("%d ║" %i, end="")
                for j in range(8):
                    if i == 0 or i == 7:
                        if peças[j] == '♜':
                            tab[i].append(Torre(t[1], t[0], i, j, 0))
                        elif peças[j] == '♞':
                            tab[i].append(Cavalo(t[1], t[0], i, j, 1))
                        elif peças[j] == '♝':
                            tab[i].append(Bispo(t[1], t[0], i, j, 1))
                        elif peças[j] == '♛':
                            tab[i].append(Rainha(t[1], t[0], i, j, 1))
                        else:
                            tab[i].append(Rei(t[2], t[0], i, j, 0))
                            if t[0] == colors.red:
                                bx = i
                                by = j
                            else:
                                wx = i
                                wy = j
                    elif i == 1 or i == 6:
                        tab[i].append(Peao(t[1], t[0], i, j, 0))
                    else:
                        t = [colors.green, 'W', 'KW']
                        tab[i].append(Vazio(i, j))

                    if (j % 2 == 0 and i % 2 == 0) or (j % 2 != 0 and i % 2 != 0):
                        print(colors.WHITE, end="")
                    print("%s %s " %(tab[i][j].cor, tab[i][j].img) + colors.fim, end="")
                print("║")
            print("  ╚════════════════════════╝")
            print(colors.green + "VERDES COMEÇAM" + colors.fim)
            while True:
                print("Escolha as coordenadas que deseja jogar: (letra primeiro, depois o número)")
                while True:
                    y, x = Posicao(tab, t[0])
                    tab[x][y].getMove(tab)
                    if len(tab[x][y].lista) > 0:
                        break
                    print("A peça escolhida não tem como se mover.")
                tab[x][y].setMove(tab)
                ImprimeJogo(tab, pts1, pts2)
                print("Informe a próxima jogada ou digite 'V' para voltar e escolher outra peça")
                y2, x2 = Posicao2(tab, t[0])
                if x2 == y2 == -1:
                    for i in range(8):
                        for j in range(8):
                            if tab[i][j].img != '♚':
                                tab[i][j].mudaTipo(0)
                    ImprimeJogo(tab, pts1, pts2)
                    #print(colors.yellow + "O Rei não pode ser colocar em Xeque!! Jogue novamente!" + colors.fim)
                    continue
                
                if tab[x2][y2].cor == colors.green:
                    pts2.append(tab[x2][y2].img)
                    pts2[0] += tab[x2][y2].Pts
                elif tab[x2][y2].cor == colors.red:
                    pts1.append(tab[x2][y2].img)
                    pts1[0] += tab[x2][y2].Pts

                if tab[x][y].img == '♚':
                    if tab[x][y].cor == colors.green:
                        bx = x2
                        by = y2
                    else:
                        wx = x2
                        wy = y2
                tab[x][y].Movimento(tab, x2, y2)
                for i in range(8):
                    for j in range(8):
                        tab[i][j].mudaTipo(0)
                        if tab[i][j].tipo == 'KW':
                            x = i
                            y = j
                        elif tab[i][j].tipo == 'KB':
                            x2 = i
                            y2 = j
                verificaXeque(tab, x, y)
                verificaXeque(tab, x2, y2)
                for i in range(8):
                    for j in range(8):
                        if tab[i][j].img != '♚':
                            tab[i][j].mudaTipo(0)
                ImprimeJogo(tab, pts1, pts2)

                if '♚' in pts2:
                    print(colors.red + "VITÓRIA DAS VERMELHAS!!" + colors.fim)
                    break
                elif '♚' in pts1:
                    print(colors.green + "VITÓRIA DAS VERDES!!" + colors.fim)
                    break
                else:
                    if t[0] == colors.green:
                        t = [colors.red]
                        print(colors.red + "VERMELHAS JOGAM" + colors.fim)
                    else:
                        t = [colors.green]
                        print(colors.green + "VERDES JOGAM" + colors.fim)
        
            print("[1] Jogar Novamente   [2] Sair")
            if Escolha(2) == '2':
                print("ENCERRANDO JOGO...")
                break
            else:
                print("INICIANDO NOVO JOGO...")
                print()

main()