from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister
import math


qreg = QuantumRegister(6)
creg = ClassicalRegister(6)
qc = QuantumCircuit(qreg, creg)

qc.h(qreg)

qc.x([qreg[0], qreg[3], qreg[5]])


qc.h(qreg[0])
qc.mct(qreg[1:], qreg[0])
qc.h(qreg[0])


qc.x([qreg[0], qreg[3], qreg[5]])
qc.h(qreg[0])
qc.cp(-math.pi/2, qreg[0], qreg[1])
qc.h(qreg[1])
qc.cp(-math.pi/4, qreg[0], qreg[2])
qc.cp(-math.pi/2, qreg[1], qreg[2])
qc.h(qreg[2])
qc.cp(-math.pi/8, qreg[0], qreg[3])
qc.cp(-math.pi/4, qreg[1], qreg[3])
qc.cp(-math.pi/2, qreg[2], qreg[3])
qc.h(qreg[3])
qc.cp(-math.pi/16, qreg[0], qreg[4])
qc.cp(-math.pi/8, qreg[1], qreg[4])
qc.cp(-math.pi/4, qreg[2], qreg[4])
qc.cp(-math.pi/2, qreg[3], qreg[4])
qc.h(qreg[4])
qc.cp(-math.pi/32, qreg[0], qreg[5])
qc.cp(-math.pi/16, qreg[1], qreg[5])
qc.cp(-math.pi/8, qreg[2], qreg[5])
qc.cp(-math.pi/4, qreg[3], qreg[5])
qc.cp(-math.pi/2, qreg[4], qreg[5])
qc.h(qreg[5])


qc.measure(qreg, creg)

backend = Aer.get_backend("qasm_simulator")
shots = int(1024)
job = execute(qc, backend, shots=shots)
result = job.result()
counts = result.get_counts()
return counts 