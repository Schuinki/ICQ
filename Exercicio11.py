import matplotlib.pyplot as plt

def plot_complex_multiplication_constant(c):
    num_fixo = complex(2, -1)
    mult_real = num_fixo.real * c
    num_real = complex(mult_real, num_fixo.imag)
    mult_imag = num_fixo.imag * c
    num_imag = complex(num_fixo.real, mult_imag)
    mult_total = num_fixo * c

    plt.figure(figsize=(8, 4))

    plt.plot(num_fixo.real, num_fixo.imag, 'ro', label='(2, -1)')
    plt.plot(num_real.real, num_real.imag, 'go', label=f'Multiplicação da parte real por {c}: ({mult_real}, {num_fixo.imag})')
    plt.plot(num_imag.real, num_imag.imag, 'bo', label=f'Multiplicação da parte imaginária por {c}: ({num_fixo.real}, {mult_imag})')
    plt.plot(mult_total.real, mult_total.imag, 'yo', label=f'Multiplicação total por {c}: ({mult_total.real:.2f}, {mult_total.imag:.2f})')

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    plt.grid(True)
    plt.legend()

    plt.show()

# Exemplo
plot_complex_multiplication_constant(3)