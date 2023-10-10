from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, assemble


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')

qc = QuantumCircuit(qreg_q, creg_c)

qc.reset(qreg_q[0])
qc.reset(qreg_q[1])
qc.reset(qreg_q[2])
qc.reset(qreg_q[3])
qc.x(qreg_q[0])
qc.x(qreg_q[0])
qc.x(qreg_q[1])
qc.x(qreg_q[2])
qc.x(qreg_q[3])
qc.cx(qreg_q[1], qreg_q[2])
qc.cx(qreg_q[2], qreg_q[1])
qc.cx(qreg_q[1], qreg_q[2])
qc.cx(qreg_q[2], qreg_q[3])
qc.cx(qreg_q[3], qreg_q[2])
qc.cx(qreg_q[2], qreg_q[3])
qc.cx(qreg_q[0], qreg_q[3])
qc.cx(qreg_q[3], qreg_q[0])
qc.cx(qreg_q[0], qreg_q[3])


qc.measure(qreg_q[0], creg_c[0])
qc.measure(qreg_q[1], creg_c[1])
qc.measure(qreg_q[2], creg_c[2])
qc.measure(qreg_q[3], creg_c[3])

simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = assemble(compiled_circuit, shots=1024)
result = simulator.run(job).result()

counts = result.get_counts(qc)
return(counts)