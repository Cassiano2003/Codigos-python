import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import math
def getImage(path):# Obter uma imagem do arquivo e retornar a imagem no formato aceito para plot
   return OffsetImage(plt.imread(path), zoom=.2)

def drawOBJ(path,v,ax,color='k'):# Desenhando uma imagem do arquivo path na localização do vetor v no gráfico ax
  ax.plot([0,v[0]],[0,v[1]],'--'+color) #Desenha uma linha tracejada (--) de cor preta (k) da origem (0,0) até v.
  ab = AnnotationBbox(getImage(path), (v[0],v[1]), frameon=True)
  ax.add_artist(ab)

def escala(vertices, sx, sy):
    #MEDIA DOS PONTOS X E Y.
    mx = (vertices[0][0] + vertices[1][0] + vertices[2][0]) / 3
    my = (vertices[0][1] + vertices[1][1] + vertices[2][1]) / 3
    #JOGA PARA O PONTO DE ORIGEM.
    transformacao0 = np.array([[1, 0, 0], [0, 1, 0], [-mx, -my, 1]])
    #VOLTA PARA OS PONTOS INICIAS.
    transformacao1 = np.array([[1, 0, 0], [0, 1, 0], [mx, my, 1]])
    escala = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

    t = transformacao0 @ escala
    t = t @ transformacao1
    new_vertices = vertices @ t
    return new_vertices
def rotacao(vertices, ang,tx, ty, sx, sy):
    cos = np.cos(ang)
    sin = np.sin(ang)

    rot = np.array([[cos, sin, 0], [-sin, cos, 0], [0, 0, 1]])
    trn = np.array([[1, 0, 0], [0, 1, 0], [tx, ty, 1]])
    scl = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

    trans = trn @ rot
    trans = scl @ trans
    new_vertices = vertices @ trans
    return new_vertices

    '''cosA = math.cos(ang)
    sinA = math.sin(ang)
    for r in range(len(vertices)):
        vertices[r] = (vertices[r] * cosA) + (vertices[r] * sinA)'''
    return resultado

def translate(tx,ty,vertices):
    new_vertices = np.array([[1,0,0],[0,1,0],[tx,ty,0]])
    new_vertices = vertices @ new_vertices
    return new_vertices

fig, ax = plt.subplots(figsize=(3, 3)) #criado o gráfico e referenciado na variavel ax
vHouse = np.array([2,4]) #Coordenada da CASA
vMoon = np.array([8,9]) #Coordenada da LUA
drawOBJ(r"C:\Users\cassi\Downloads\casa.png",vHouse,ax)
drawOBJ(r"C:\Users\cassi\Downloads\lua.png",vMoon,ax)
plt.show()

'''#VERTICES ORIGINAL.
vertices = np.array([[1,1,1],[3,1,1],[2,3,1]])
#PARAMETROS FUNCAO ROTACAO, TRANSLACAO, ESCALA.
tx, ty = 2, 2
sx, sy = 2, 2
ang = 10
#PARAMETROS DA FUNCAO ESCALA.
new_scale = escala(vertices,sx,sy)
#PARAMETROS DA FUNCAO ROTACAO.
new_rotation = rotacao(vertices, ang, tx, ty, sx, sy)
#PARAMETROS FUNCAO TRANSLACAO.
new_translate = translate(tx,ty,vertices)

#IMPRIMI OS VALORE DOS VERTICES ORIGINAIS, ESCALADO, ROTACIONADO E TRANSLADADO(MUDADO PARA COMPOSITION(escala,rotacao e translacaos)).
print(f"Vertices originais:\n{vertices}\n")

print(f"Vertices escalado:\n{new_scale}\n")

print(f"Vertices rotacionado:\n{new_rotation}\n")

print(f"Vertices transladado:\n{new_translate}\n")

#PLOTANDO AS FIGURAS.
#FIGURA VERTICES ORIGINAIS.
ori = plt.figure(figsize=(3,3))
plt.plot(vertices, color='black')
plt.title('Original')

#FIGURA ESCALA.
esc = plt.figure(figsize=(3,3))
plt.plot(new_scale, color='purple')
plt.title('escala')

#FIGURA ROTACIOANDA.
rot = plt.figure(figsize=(3,3))
plt.plot(new_rotation, color='yellow')
plt.title('rotacionada')

#FIGURA TRANSLADADA.
tr = plt.figure(figsize=(3,3))
plt.plot(new_translate, color='blue')
plt.title('translation')'''