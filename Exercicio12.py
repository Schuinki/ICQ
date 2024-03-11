import matplotlib.pyplot as plt
import cmath
def operador(z,n) :
    r =z
    while n>1 :
        r *=z
        n-=1
    return r
num_complexo_str = input("Digite o primeiro número complexo a+bj no formato (a, b): ")
num_complexo_str = num_complexo_str.replace('(', '').replace(')', '')
partes = num_complexo_str.split(',')

if len(partes) != 2:
    print("Número complexo inválido. Certifique-se de que está no formato (a, b).")
else:
    parte_real = float(partes[0])
    parte_imaginaria = float(partes[1])
z=complex(parte_real,parte_imaginaria)
pontos_real = []
pontos_imaginarios = []
for n in range(1, 11):
    resultado = operador(z, n)
    pontos_real.append(resultado.real)
    pontos_imaginarios.append(resultado.imag)

plt.figure(figsize=(8, 6))
plt.plot(pontos_real, pontos_imaginarios, 'bo-', label='z^n')
plt.plot([0], [0], 'ro', label='Origem (0, 0)')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title(f'Potências de {z}')
plt.legend()
plt.grid(True)
plt.show()