from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, Aer, transpile, assemble

qreg = QuantumRegister(5, name='q')  
creg = ClassicalRegister(5, name='c') 

qc = QuantumCircuit(qreg, creg)
qc.h(qreg)


qc.x(qreg[0]).c_if(creg, 1)
qc.x(qreg[1]).c_if(creg, 1)
qc.x(qreg[2]).c_if(creg, 1)
qc.x(qreg[3]).c_if(creg, 1)
qc.x(qreg[4]).c_if(creg, 1)


qc.measure(qreg, creg)

simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()

counts = result.get_counts(qc)
print(counts)


simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = assemble(compiled_circuit, shots=1024)
result = simulator.run(job).result()

counts = result.get_counts(qc)
return(counts)