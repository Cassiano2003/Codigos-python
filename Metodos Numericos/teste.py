e = 10**(-4)
k = 0
xk = 0.5
n = 10
es = 2.71828

while k < n:
    f = (xk**3)-(9*xk)+3
    f_1 = (3*(xk**2))-9
    xk_1 = xk - (f/f_1)
    print(k+1,xk,f,f_1,abs(xk_1-xk))
    
    if(abs(xk_1-xk) < e):
        break
    
    xk = xk_1
    k+=1