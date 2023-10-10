from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from qiskit.circuit.library import QFT



qreg = QuantumRegister(6, 'q')
creg = ClassicalRegister(6, 'c')
qc = QuantumCircuit(qreg, creg)

qc.x(qreg[5])
qc.h(range(qreg[5]))
qc.mct(qreg[5], qreg[5])  
qft_circuit = QFT(5, do_swaps=False, inverse=True)
qc.compose(qft_circuit, inplace=True)

qc.measure(qreg, creg)

backend = Aer.get_backend("qasm_simulator")
shots = int(1024)
job = execute(qc, backend, shots=shots)
result = job.result()
counts = result.get_counts()

return counts