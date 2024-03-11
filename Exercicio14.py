import numpy as np
import matplotlib.pyplot as plt

def mobius_transform(z):
    return z / (1 * z)

theta = np.linspace(0, 2 * np.pi, 100)
circle_points = np.exp(1j * theta)

transformed_points = mobius_transform(circle_points)

plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.plot(np.real(circle_points), np.imag(circle_points), label='Círculo Original')
plt.title('Círculo Original')
plt.axis('equal')
plt.legend()

# Novo
plt.subplot(122)
plt.plot(np.real(transformed_points), np.imag(transformed_points), label='Círculo Transformado')
plt.title('Círculo Transformado pela Transformação de Möbius')
plt.axis('equal')
plt.legend()

plt.show()
