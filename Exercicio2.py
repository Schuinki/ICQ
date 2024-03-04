def calcular_potencia_i(n):
    # Encontrar k e r
    k = n // 4
    r = n % 4

    # Calcular i^r
    if r == 0:
        return 1
    elif r == 1:
        return "i"
    elif r == 2:
        return "-1"
    else:  # r == 3
        return "-i"


entrada = int(input('Digite o n:'))
resultado = calcular_potencia_i(entrada)
print("O resultado é:", resultado)