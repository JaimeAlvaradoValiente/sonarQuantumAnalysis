from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')

qc = QuantumCircuit(qreg_q, creg_c)

received_qubits = [0, 1, 1, 0]

qc.x(qreg_q)
qc.cx(qreg_q[0], qreg_q[0])
qc.cx(qreg_q[1], qreg_q[1])
qc.cx(qreg_q[2], qreg_q[2])
qc.cx(qreg_q[3], qreg_q[3])

qc.measure(qreg_q, creg_c)

simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = assemble(compiled_circuit, shots=1024)
result = simulator.run(job).result()

counts = result.get_counts(qc)
return(counts)