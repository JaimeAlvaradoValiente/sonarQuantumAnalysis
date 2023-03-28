from qiskit import execute, QuantumRegister, ClassicalRegister, QuantumCircuit, Aer
from numpy import pi
qreg_q = QuantumRegister(5, 'q')
creg_c = ClassicalRegister(5, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)
circuit.h(qreg_q[1])
circuit.h(qreg_q[0])
circuit.h(qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])
circuit.measure(qreg_q[1], creg_c[1])
backend = Aer.get_backend("qasm_simulator")
x=int(shots)
job = execute(circuit, backend, shots=x)
result = job.result()
counts = result.get_counts()
return counts