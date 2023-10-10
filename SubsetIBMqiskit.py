from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister


qreg_q = QuantumRegister(5, 'q')
creg_c = ClassicalRegister(5, 'c')
qc = QuantumCircuit(qreg_q, creg_c)

qc.cx(qreg_q[0], qreg_q[5])  
qc.cx(qreg_q[1], qreg_q[5])  
qc.cx(qreg_q[2], qreg_q[5])  
qc.cx(qreg_q[3], qreg_q[5])  
qc.cx(qreg_q[4], qreg_q[5])  

qc.cx(qreg_q[:5], qreg_q[5])
qc.c_if(creg_c, 2)  

qc.measure(qreg_q, creg_c)

backend = Aer.get_backend("qasm_simulator")
shots = int(1024)
job = execute(qc, backend, shots=shots)
result = job.result()
counts = result.get_counts()

return counts

