import numpy as np
import matplotlib.pyplot as plt

def plot_vector(ax, r, theta, color, label):
    ax.quiver(0, 0, r * np.cos(theta), r * np.sin(theta), color=color, angles='xy', scale_units='xy', scale=1, label=label)

vetor_a = (np.sqrt(2**2 + (-1)**2), np.arctan2(-1, 2))
vetor_b = (np.sqrt(1**2 + 1**2), np.arctan2(1, 1))
soma_r = vetor_a[0] + vetor_b[0]
soma_theta = vetor_a[1] + vetor_b[1]
subtracao_r = vetor_a[0] - vetor_b[0]
subtracao_theta = vetor_a[1] - vetor_b[1]
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
plot_vector(ax, *vetor_a, color='r', label='a')
plot_vector(ax, *vetor_b, color='b', label='b')
plot_vector(ax, soma_r, soma_theta, color='g', label='a + b')
plot_vector(ax, subtracao_r, subtracao_theta, color='y', label='a - b')
ax.legend()
plt.title('Operações com Vetores em Coordenadas Polares')
plt.show()
