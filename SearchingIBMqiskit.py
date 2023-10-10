
from qiskit import QuantumCircuit, transpile, assemble, Aer, QuantumRegister, ClassicalRegister


qreg = QuantumRegister(6)
creg = ClassicalRegister(6)
qc = QuantumCircuit(qreg, creg)

qc.x(qreg[0])
qc.x(qreg[1])
qc.x(qreg[2])
qc.x(qreg[3])
qc.x(qreg[4])
qc.x(qreg[5])

qc.h(qreg[1])
qc.x(qreg[2])
qc.x(qreg[3])
qc.x(qreg[4])
qc.x(qreg[5])
qc.mct(qreg[1:], qreg[0])

qc.h(qreg[1])
qc.x(qreg[2])
qc.x(qreg[3])
qc.x(qreg[4])
qc.x(qreg[5])

qc.measure(qreg, creg)

simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = assemble(compiled_circuit, shots=1024)
result = simulator.run(job).result()

counts = result.get_counts(qc)
return(counts)
