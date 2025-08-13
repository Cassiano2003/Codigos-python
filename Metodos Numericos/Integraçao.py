import numpy as np

a,b = map(int, input("Limitantes manor e maior: ").split())
n = int(input("Numero de espaços: "))

x = []
if(b >= a):
    h = (b - a)/n
    for i in range(a,b+1):
        x.append(i)
else:
    h = (a - b)/n
    for i in range(b,a+1):
        x.append(i)
f_x = []
for i in x:
    f = (1/i)* np.exp(i/2)
    f_x.append(f)

print(x)
print(f_x)

soma = 0
for i in range(len(f_x)):
    if (i == 0) or (i == len(f_x)-1): 
        soma += (f_x[i]/2)
    else:
        soma += (f_x[i])

print(f'{soma:.4f}')

