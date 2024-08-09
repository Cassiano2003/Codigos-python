import numpy as np


m_1 = np.array([[-2,0,-1],[-1,0,-1],[-4,1,-2]])

m = np.array([[-1,1,0],[-2,0,1],[1,-2,0]])

ori = np.array([[10,0,6],[24,-2,12],[-12,0,-8]])

o = m_1@ori

print(o@m)