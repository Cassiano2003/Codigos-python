import numpy as np
def transformation(sx,sy,vertices):
    #-----IMPLEMENTE A FUNÇÃO--------#
    escala = np.array([[sx,0,0],[0,sy,0],[0,0,1]])
    new_vertices = vertices @ escala
    new_vertices1 = np.array(new_vertices)
    return new_vertices1

vertices = np.array([[1,1,1],[3,1,1],[2,3,1]])
print(transformation(2,2,vertices))