from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Creamos un circuito con 1 qubit y 1 bit clásico para medir
qc = QuantumCircuit(1, 1)

# Aplicamos la puerta Hadamard al qubit
qc.h(0)

# Medimos el qubit en el bit clásico
qc.measure(0, 0)

# Usamos el simulador de Qiskit Aer
simulator = AerSimulator()

# Ejecutamos el circuito 1000 veces
job = simulator.run(qc, shots=1000)
result = job.result()

# Mostramos los resultados
counts = result.get_counts()
print("Resultados de la medición:", counts)
