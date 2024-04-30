from qiskit import BasicAer, execute
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.tools.visualization import plot_histogram
import math

# Registro quântico e clássico
q = QuantumRegister(5, 'q')
c = ClassicalRegister(3, 'c')

# Circuito quântico
shor = QuantumCircuit(q, c)


# Função para calcular a operação a**x mod 15
def circuito_amod15(qc, qr, cr, a):
    if a == 2:
        qc.cswap(qr[4], qr[3], qr[2])
        qc.cswap(qr[4], qr[2], qr[1])
        qc.cswap(qr[4], qr[1], qr[0])
    elif a == 7:
        qc.cswap(qr[4], qr[1], qr[0])
        qc.cswap(qr[4], qr[2], qr[1])
        qc.cswap(qr[4], qr[3], qr[2])
        qc.cx(qr[4], qr[3])
        qc.cx(qr[4], qr[2])
        qc.cx(qr[4], qr[1])
        qc.cx(qr[4], qr[0])
    elif a == 8:
        qc.cswap(qr[4], qr[1], qr[0])
        qc.cswap(qr[4], qr[2], qr[1])
        qc.cswap(qr[4], qr[3], qr[2])
    elif a == 11:
        qc.cswap(qr[4], qr[2], qr[0])
        qc.cswap(qr[4], qr[3], qr[1])
        qc.cx(qr[4], qr[3])
        qc.cx(qr[4], qr[2])
        qc.cx(qr[4], qr[1])
        qc.cx(qr[4], qr[0])
    elif a == 13:
        qc.cswap(qr[4], qr[3], qr[2])
        qc.cswap(qr[4], qr[2], qr[1])
        qc.cswap(qr[4], qr[1], qr[0])
        qc.cx(qr[4], qr[3])
        qc.cx(qr[4], qr[2])
        qc.cx(qr[4], qr[1])
        qc.cx(qr[4], qr[0])


# Função para criar o circuito quântico para a**x mod 15
def circuito_aperiod15(qc, qr, cr, a):
    if a == 11:
        circuito_11period15(qc, qr, cr)
        return

    # Inicializar q[0] para |1>
    qc.x(qr[0])

    # Aplicar a**4 mod 15
    qc.h(qr[4])
    # controlled identity nos 4 qubits restantes, o que é equivalente a não fazer nada
    qc.h(qr[4])
    # medir
    qc.measure(qr[4], cr[0])
    # redefinir q[4] para |0>
    qc.reset(qr[4])

    # Aplicar a**2 mod 15
    qc.h(qr[4])
    # controlled unitary
    qc.cx(qr[4], qr[2])
    qc.cx(qr[4], qr[0])
    # feed forward
    qc.u1(math.pi / 2., qr[4]).c_if(cr, 1)
    qc.h(qr[4])
    # medir
    qc.measure(qr[4], cr[1])
    # redefinir q[4] para |0>
    qc.reset(qr[4])

    # Aplicar a mod 15
    qc.h(qr[4])
    # controlled unitary.
    circuito_amod15(qc, qr, cr, a)
    # feed forward
    qc.u1(3. * math.pi / 4., qr[4]).c_if(cr, 3)
    qc.u1(math.pi / 2., qr[4]).c_if(cr, 2)
    qc.u1(math.pi / 4., qr[4]).c_if(cr, 1)
    qc.h(qr[4])
    # medir
    qc.measure(qr[4], cr[2])


# Função específica para criar o circuito quântico para 11**x mod 15
def circuito_11period15(qc, qr, cr):
    # Inicializar q[0] para |1>
    qc.x(qr[0])

    # Aplicar a**4 mod 15
    qc.h(qr[4])
    # controlled identity nos 4 qubits restantes, o que é equivalente a não fazer nada
    qc.h(qr[4])
    # medir
    qc.measure(qr[4], cr[0])
    # redefinir q[4] para |0>
    qc.reset(qr[4])

    # Aplicar a**2 mod 15
    qc.h(qr[4])
    # controlled identity nos 4 qubits restantes, o que é equivalente a não fazer nada
    # feed forward
    qc.u1(math.pi / 2., qr[4]).c_if(cr, 1)
    qc.h(qr[4])
    # medir
    qc.measure(qr[4], cr[1])
    # redefinir q[4] para |0>
    qc.reset(qr[4])

    # Aplicar 11 mod 15
    qc.h(qr[4])
    # controlled unitary.
    qc.cx(qr[4], qr[3])
    qc.cx(qr[4], qr[1])
    # feed forward
    qc.u1(3. * math.pi / 4., qr[4]).c_if(cr, 3)
    qc.u1(math.pi / 2., qr[4]).c_if(cr, 2)
    qc.u1(math.pi / 4., qr[4]).c_if(cr, 1)
    qc.h(qr[4])
    # medir
    qc.measure(qr[4], cr[2])


# Aplicar a função circuito_aperiod15 com a = 7
circuito_aperiod15(shor, q, c, 7)

# Executar o circuito no simulador
backend = BasicAer.get_backend('qasm_simulator')
sim_job = execute([shor], backend)
sim_result = sim_job.result()
sim_data = sim_result.get_counts(shor)

# Plotar o histograma dos resultados
plot_histogram(sim_data)
