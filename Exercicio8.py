import numpy as np
import matplotlib.pyplot as plt

# Definir vetores
vetor_a = np.array([2, -1])
vetor_b = np.array([1, 1])

# a) Adição de vetores
soma = vetor_a + vetor_b

# b) Subtração de vetores
subtracao = vetor_a - vetor_b

fig, ax = plt.subplots()
ax.quiver(0, 0, vetor_a[0], vetor_a[1], angles='xy', scale_units='xy', scale=1, color='r', label='a')
ax.quiver(0, 0, vetor_b[0], vetor_b[1], angles='xy', scale_units='xy', scale=1, color='b', label='b')
ax.quiver(0, 0, soma[0], soma[1], angles='xy', scale_units='xy', scale=1, color='g', label='a + b')
ax.quiver(0, 0, subtracao[0], subtracao[1], angles='xy', scale_units='xy', scale=1, color='y', label='a - b')
lim = max(np.max(np.abs(soma)), np.max(np.abs(subtracao))) + 1
ax.set_xlim([-lim, lim])
ax.set_ylim([-lim, lim])
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.legend()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()
