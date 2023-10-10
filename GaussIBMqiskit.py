import numpy as np
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute, assemble


   
qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')

qc = QuantumCircuit(qreg_q, creg_c)

Fq_characters = [0.5, 0.2, -0.3, 0.1] 
precision = 4

character_0 = Fq_characters[0]
character_1 = Fq_characters[1]
character_2 = Fq_characters[2]
character_3 = Fq_characters[3]

qc.u(2 * np.arcsin(character_0), qreg_q[0], precision, qreg_q[0])
qc.u(2 * np.arcsin(character_1), qreg_q[1], precision, qreg_q[1])
qc.u(2 * np.arcsin(character_2), qreg_q[2], precision, qreg_q[2])
qc.u(2 * np.arcsin(character_3), qreg_q[3], precision, qreg_q[3])

qc.measure(qreg_q, creg_c)

backend = Aer.get_backend("qasm_simulator")
shots = int(1024)
job = execute(qc, backend, shots=shots)
result = job.result()
counts = result.get_counts()
return counts 
