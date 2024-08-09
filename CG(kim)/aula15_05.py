import matplotlib.pyplot as plt
import numpy as np

#COHEN-SUTHERLAND - IMPLEMENTACAO.
#AS LINHAS QUE NAO PODEM SER IDENTIFICADAS FORA OU DENTRO COMPLEMETAMENTE DA JANELA DE RECORTE
#ELAS SAO ENTAO PROCESSADAS PARA VERIFICAR INTERSECOES, PARA ISSO USAMOS OS CODIGOS ABAIXO, PARA FAZER
#AS INTERSECOES Y E X.

#DIREITA E ESQUERDA.
def valorY_inters_reta(x_inicio, y_inicio, x_end, y_end):
  #VARIAVEL m SIGNIFICA INCLINACAO (COEFICIENTE ANGULAR), EQUACAO m = y0-y/x0-x.
  #Em outras palavras, a cada três unidades que andamos verticalmente para baixo,
  #andamos quatro unidades horizontalmente para a direita.
  m = y_end-y_inicio/x_end - x_inicio
  #PARA ENCONTRAR OS VALORES DE Y NA INTERSECAO, BASTA USAR A EQUACAO y = y0 + m(x-x0).
  #ENTAO:
  y = y_inicio + m*(x_inicio-x_end)
  return y

#TOPO E INFERIOR.
def valorX_inters_reta(x_inicio, y_inicio, x_end, y_end):
  m = y_end-y_inicio/x_end - x_inicio
  x = (x_inicio+((y_end-y_inicio)/m))
  return x

def encodeVert(point,rect):
  xmin,ymin = np.min(rect,axis=0)
  xmax,ymax = np.max(rect,axis=0)
  code = 0
  if(point[0] < xmin):
    code = code | codeLEFT
  elif(point[0] > xmax):
    code = code | codeRIGHT
  if(point[1] < ymin):
    code = code | codeBTM
  elif(point[1] > ymax):
    code = code | codeTOP
  return code

#função para desenhar as arestas e vertices
def drawObjectEdges(vertices,arestas,ax,color='b'):

  ax.scatter(vertices[:, 0], vertices[:, 1], c='r', marker='o')
  for i,p in enumerate(vertices):
    x,y,_ = p
    ax.text(x, y-1, str(i),ha='center')
  for edge in arestas:
    ax.plot(vertices[edge, 0],vertices[edge, 1], c=color)
  ax.set_xlim(-1, 5)
  ax.set_ylim(-1, 5)

  ax.set_xlabel('X')
  ax.set_ylabel('Y')


#MAIN
#Objeto Triangulo
arestas = np.array([(0,1),(1,2),(2,0)])
vertices = np.array([[1,1,1],[3,1,1],[2,3,1]])

#Area de recorte
verticesCLIP = np.array([[2,0,1] ,[4,0,1],[4,4,1],[2,4,1]])
arestasCLIP = np.array([(0,1),(1,2),(2,3),(3,0)])

fig, ax = plt.subplots(figsize=(3, 3))
drawObjectEdges(vertices,arestas,ax,'k') #Cor preta o Triângulo
drawObjectEdges(verticesCLIP,arestasCLIP,ax, 'orange') #Cor laranja o Recorte
plt.show()
#Codificação das áreas
#FAZER TABELA BINARIO PARA DECIMAL PARA MELHOR ENTEDIMENTO.
#0000 indica que a parte da figura esta dentro do quadrante(area de recorte).
codeTOP=1<<3#DESLOCA O 1 E O MOVE 3 BIT A ESQUERDA.
codeBTM=1<<2
codeLEFT=1
codeRIGHT=1<<1
print('TOP',codeTOP,bin(codeTOP))
print('BTM',codeBTM,bin(codeBTM))
print('LEFT',codeLEFT,bin(codeLEFT))
print('RIGHT',codeRIGHT,bin(codeRIGHT))
print("-----------------------------------------------")
#Teste 1000 | 0100 = 1100
x= codeTOP | codeBTM
print(x,bin(x))
print("-----------------------------------------------")

listCodes = []
for p in vertices:
  code = encodeVert(p[:-1],verticesCLIP[:,:-1])
  listCodes.append(code)
  print(p[:-1],code,bin(code))
print("-----------------------------------------------")
listCodes = np.array(listCodes)
for ar in arestas:
  pairCodes = listCodes[ar]
  print(pairCodes, vertices[ar[0]], vertices[ar[1]])
  #verificando os pares
  if(pairCodes[0] | pairCodes[1] == 0):
    print('dentro')
  elif(pairCodes[0] & pairCodes[1] != 0):
    print('fora')
  else:
    print('parcialmente')