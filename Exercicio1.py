## Provar que não tem solução nos reais: X^4 + 2X^2 + 1 = 0
import math
print('Provando que não tem solução nos reais: x^4 + 2x^2 + 1 = 0')
print('Convertendo: y^2 + 2y + 1 = 0')

def bhaskara(a, b, c):
    global delta
    delta = b*b - 4*a*c
    print(delta)
    if(delta < 0):
        print(f'{a}y²+{b}y+{c} = 0 nao tem raizes reais, portanto a original tambem nao')
    elif(delta == 0):
        print(f'{a}y²+{b}y+{c} tem uma raiz real de multiplicidade 2')
        raiz = -b/ 2 * a
        print(f'a raiz nesse caso é {raiz}')
        if(raiz < 0):
            print('mas x² = y, então se y eh negativo, x nao eh real. nao ha raizes reais. provado.')
    else:
        print('tem varias raizes reais')

bhaskara(1, 2, 1)
