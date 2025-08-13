import math as ma

e = 10**(-4)
k = 0
v_1 = 0
v_2 = 1
n = 10
es = 2.71828
t = '\t'

while k < n:
    f_1 = (v_1**3) - (9 * v_1) + 3
    f_2 = (v_2**3) - (9 * v_2) + 3
    xk = ((v_1*f_2)-(v_2*f_1))/(f_2-f_1)
    print("Interaçao",k+1,"\n","x",k,"=",v_1,"\n","x",k+1,"=",v_2,"\n",
          "f",k,"=",f_1,"\n","f",k+1,"=",f_2,"\n","xk = ",xk,"\n",
          "Erro:",abs(xk-v_2),"\n")
    if(abs(xk-v_2) < e):
        break
    
    v_1 = v_2
    v_2 = xk
    k+=1