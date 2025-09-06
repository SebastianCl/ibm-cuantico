from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Creamos un circuito con 2 qubits y 2 bits clásicos
qc = QuantumCircuit(2, 2)

# Paso 1: ponemos el primer qubit en superposición
qc.h(0)

# Paso 2: aplicamos una compuerta CNOT (control en qubit 0, objetivo qubit 1)
qc.cx(0, 1)

# Medimos ambos qubits
qc.measure([0,1], [0,1])

# Simulamos
simulator = AerSimulator()

job = simulator.run(qc, shots=1000)
result = job.result()

counts = result.get_counts()
print("Resultados:", counts)
