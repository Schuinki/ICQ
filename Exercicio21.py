import numpy as np

def calculadora_tensor_prod(matrix_a:np.array, matrix_b:np.array):
    return np.kron(matrix_a, matrix_b)


print(calculadora_tensor_prod(
    np.array([
        [1, complex(1, 2)],
        [complex(3, 4), 2]
    ]),
    np.array([
        [complex(0, 1), 3],
        [0, complex(1, 3)]
    ])
))