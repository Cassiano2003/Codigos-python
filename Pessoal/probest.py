x = [1,3,5,7,9]
f = [4,12,15,13,6]
f_ac = [4,16,31,44,50]
n = 50

soma = 0
soma_2 = 0
for i in range(len(x)):
    soma += (x[i]*f[i])
    soma_2 += f[i]


soma_f = 0
for i in f:
    soma_f += i/soma_2
    print((i/soma_2)*100,end=" ")

print(" = ",soma_f*100)

for i in f_ac:
    print((i/soma_2)*100,end=" ")

print()
print(soma/soma_2)