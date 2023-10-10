import numpy as np
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute


qreg_q = QuantumRegister(6, 'q')
creg_c = ClassicalRegister(6, 'c')

# Create a quantum circuit using the registers
qc = QuantumCircuit(qreg_q, creg_c)

# Apply the square root approximation
qc.h(qreg_q[0])
qc.h(qreg_q[1])
qc.h(qreg_q[2])
qc.h(qreg_q[3])
qc.x(qreg_q[4])

qc.swap(qreg_q[1], qreg_q[4])
qc.u(np.arcsin(1/2), qreg_q[0], qreg_q[4])
qc.swap(qreg_q[0], qreg_q[4])
qc.u(np.arcsin(1/4), qreg_q[1], qreg_q[4])
qc.swap(qreg_q[1], qreg_q[4])
qc.u(np.arcsin(1/8), qreg_q[2], qreg_q[4])
qc.swap(qreg_q[2], qreg_q[4])
qc.u(np.arcsin(1/16), qreg_q[3], qreg_q[4])

qc.measure(qreg_q, creg_c)

backend = Aer.get_backend("qasm_simulator")
shots = int(1024)
job = execute(qc, backend, shots=shots)
result = job.result()
counts = result.get_counts()

return counts
