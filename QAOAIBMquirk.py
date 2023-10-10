from qiskit import execute, QuantumRegister, ClassicalRegister, QuantumCircuit, Aer
from numpy import pi
qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)
circuit.measure(qreg_q[0], creg_c[0])
backend = Aer.get_backend("qasm_simulator")
x=int(shots)
job = execute(circuit, backend, shots=x)
result = job.result()
counts = result.get_counts()
return counts
