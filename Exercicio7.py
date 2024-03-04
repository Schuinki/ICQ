def calcular_conjugado(numero_complexo):
    return complex(numero_complexo.real, -numero_complexo.imag)

def verificar_propriedades(c1, c2):

    lado_esquerdo_1 = calcular_conjugado(c1) + calcular_conjugado(c2)
    lado_direito_1 = calcular_conjugado(c1 + c2)

    lado_esquerdo_2 = calcular_conjugado(c1) * calcular_conjugado(c2)
    lado_direito_2 = calcular_conjugado(c1 * c2)

    propriedade_1 = lado_esquerdo_1 == lado_direito_1
    propriedade_2 = lado_esquerdo_2 == lado_direito_2

    print("Conjugado(c1) + Conjugado(c2) =", lado_esquerdo_1)
    print("Conjugado(c1 + c2) =", lado_direito_1)
    print("Propriedade 1 é verdadeira:", propriedade_1)

    print("\nConjugado(c1) * Conjugado(c2) =", lado_esquerdo_2)
    print("Conjugado(c1 * c2) =", lado_direito_2)
    print("Propriedade 2 é verdadeira:", propriedade_2)

c1_str = input("Digite a parte real e imaginária de c1 separadas por espaço (por exemplo, '3 -2'): ")
c2_str = input("Digite a parte real e imaginária de c2 separadas por espaço (por exemplo, '1 4'): ")

c1 = complex(*map(float, c1_str.split()))
c2 = complex(*map(float, c2_str.split()))

verificar_propriedades(c1, c2)