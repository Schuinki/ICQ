import numpy as np

def cartesian_to_polar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

x = int(input('Digite o valor de x:'))
y = int(input('Digite o valor de y:'))
r_resultante, theta_resultante = cartesian_to_polar(x, y)

print(f"Coordenadas Cartesianas: ({x}, {y})")
print(f"Coordenadas Polares: (r = {r_resultante}, θ = {theta_resultante})")
