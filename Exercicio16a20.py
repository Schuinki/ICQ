import numpy as np

# Função para receber uma matriz complexa do usuário
def obter_matriz_do_usuario(tamanho):
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

# Exercício 16
def encontrar_transposta_conjugada(matriz):
    transposta = np.transpose(matriz)
    conjugada = np.conjugate(matriz)
    dagger = np.transpose(conjugada)
    return transposta, conjugada, dagger

# Exercício 17
def produto_cartesiano(matriz1, matriz2):
    return np.outer(matriz1, matriz2)

# Exercício 18
def produto_interno(matriz1, matriz2):
    return np.inner(matriz1, matriz2)

# Exercício 19
def verificar_hermitiana(matriz):
    return np.allclose(matriz, np.conjugate(np.transpose(matriz)))

# Exercício 20
def verificar_unitaria(matriz):
    identidade = np.identity(matriz.shape[0])
    produto1 = np.dot(matriz, np.conjugate(np.transpose(matriz)))
    produto2 = np.dot(np.conjugate(np.transpose(matriz)), matriz)
    return np.allclose(produto1, identidade) and np.allclose(produto2, identidade)

tamanho_matriz = int(input("Digite o tamanho das matrizes (um número inteiro): "))

matriz_complexa1 = obter_matriz_do_usuario(tamanho_matriz)
matriz_complexa2 = obter_matriz_do_usuario(tamanho_matriz)

# Exercício 16 (Matriz 1)
transposta, conjugada, dagger = encontrar_transposta_conjugada(matriz_complexa1)
print("Matriz 1 - Transposta:\n", transposta)
print("Matriz 1 - Conjugada:\n", conjugada)
print("Matriz 1 - Dagger:\n", dagger)

# Exercício 17 (Matrizes 1 e 2)
resultado_produto_cartesiano = produto_cartesiano(matriz_complexa1, matriz_complexa2)
print("Produto Cartesiano das Matrizes 1 e 2:\n", resultado_produto_cartesiano)

# Exercício 18 (Matrizes 1 e 2)
resultado_produto_interno = produto_interno(matriz_complexa1.flatten(), matriz_complexa2.flatten())
print("Produto Interno das Matrizes 1 e 2:\n", resultado_produto_interno)

# Exercício 19 (Matriz 1)
hermitiana = verificar_hermitiana(matriz_complexa1)
print("Matriz 1 é hermitiana:", hermitiana)

# Exercício 20 (Matriz 1)
unitaria = verificar_unitaria(matriz_complexa1)
print("Matriz 1 é unitária:", unitaria)
