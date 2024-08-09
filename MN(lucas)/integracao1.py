from sympy import *

def f(X):
    x = Symbol('x')
    #r = sqrt(6*x - 5)
    r = exp(x)
    r = lambdify(x, r)
    return r(X)

def f2(X):
    x = Symbol('x')
    #f = sqrt(6*x - 5)
    f = exp(x)
    f1 = diff(f, x)
    r = diff(f1, x)
    r = lambdify(x, r)
    return r(X)

def Integracao(x0, x1, n):
    h = (x1 - x0)/n
    xn = x0 + h
    x = 0
    for i in range(n - 1):
        x += f(xn)
        xn += h
    I = h/2 * (f(x0) + 2*x + f(x1))
    fx0 = f2(x0)
    fx1 = f2(x1)
    m = max(abs(fx0), abs(fx1))
    E = (n * h**3)/12 * abs(m)
    return I, E


def main():
    print("==================== INTEGRAÇÃO ====================")
    print()
    while True:
        print("[1] Regra do Trapézio  [2] Regra dos Trapézios Generalizada")
        print("                 [3] Sair")
        e = '/'
        while '1' != e != '2' and e != '3':
            print("-> ", end="")
            e = input()
        print()
        if e == '3':
            print("ENCERRANDO PROGRAMA...")
            break
        else:
            print("Informe o intervalo da Integral:")
            print("Valor Inferior = ", end="")
            x0 = int(input())
            print("Valor Superior = ", end="")
            x1 = int(input())
            if e == '1':
                n = 1
            else:
                print("Informe o número de subintervalos:")
                print("-> ", end="")
                n = int(input())
            I, E = Integracao(x0, x1, n)
            print()
            print("O valor da Integração é aproximadamente: %.5f" %I)
            print("O ERRO cometido será, no máximo: %.5f" %E)
            print()
main()