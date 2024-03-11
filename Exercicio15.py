import numpy as np

# Função para receber uma matriz complexa do usuário, semelhante com 16 a 20.
def obter_matriz_complexa_do_usuario(tamanho):
    try:
        print(f"Digite os termos da matriz complexa {tamanho}x{tamanho} (parte real + parte imaginária j):")
        matriz = np.zeros((tamanho, tamanho), dtype=complex)

        for i in range(tamanho):
            for j in range(tamanho):
                real = float(input(f"Parte real do termo ({i + 1}, {j + 1}): "))
                imaginaria = float(input(f"Parte imaginária do termo ({i + 1}, {j + 1}): "))
                matriz[i, j] = real + imaginaria * 1j

        return matriz
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números válidos.")

# Exercício 15 - Função de adição de matrizes complexas
def adicao_matrizes_complexas(matriz1, matriz2):
    return np.add(matriz1, matriz2)

# Exercício 15 - Função de inversa de matriz complexa
def inversa_matriz_complexa(matriz):
    return np.linalg.inv(matriz)

# Exercício 15 - Função de multiplicação escalar complexa
def multiplicacao_escalar_complexa(matriz, escalar):
    return np.multiply(escalar, matriz)

tamanho_matriz = int(input("Digite o tamanho das matrizes (um número inteiro): "))
matriz1 = obter_matriz_complexa_do_usuario(tamanho_matriz)
matriz2 = obter_matriz_complexa_do_usuario(tamanho_matriz)
resultado_adicao = adicao_matrizes_complexas(matriz1, matriz2)
print("Adição de Matrizes Complexas:\n", resultado_adicao)
resultado_inversa = inversa_matriz_complexa(matriz1)
print("Inversa da Matriz Complexa 1:\n", resultado_inversa)
escalar_complexo = complex(input("Digite o escalar complexo para a multiplicação: "))
resultado_multiplicacao_escalar = multiplicacao_escalar_complexa(matriz1, escalar_complexo)
print(f"Multiplicação Escalar da Matriz Complexa 1 pelo escalar {escalar_complexo}:\n", resultado_multiplicacao_escalar)
