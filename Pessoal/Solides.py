import random

def Solides_Meio(V,p,q,r):
    s = V[q]
    z1 = V[q]
    for i in range(q-1,p,-1):
        s = s + V[i]
        if s > z1 :
            z1 = s
    z2 = V[q+1]
    s = V[q+1]
    for i in range(q+2,r):
        s = s+V[i]
        if s > z2:
            z2 = s
    return z1+z2


def Solides2(V,p,r):
    if p == r:
        return V[p]
    else:
        q = (p + r ) // 2
        x = Solides2(V,p,q)
        y = Solides2(V,q+1,r)
        z = Solides_Meio(V,p,q,r)
        return max(x,y,z)
    

random_numbers = [random.randint(-100, 100) for _ in range(50)]
print(Solides2(random_numbers,0,len(random_numbers)-1))
