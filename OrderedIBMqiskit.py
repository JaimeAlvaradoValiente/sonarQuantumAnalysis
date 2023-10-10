from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from qiskit.circuit.library import QFT



qreg_q = QuantumRegister(6, 'q')
creg_c = ClassicalRegister(6, 'c')
qc = QuantumCircuit(qreg_q, creg_c)

qc.x(qreg_q[5])
qc.h(range(qreg_q[5]))
qc.mct(qreg_q[:5], qreg_q[5])  
qft_circuit = QFT(5, do_swaps=False, inverse=True)
qc.compose(qft_circuit, inplace=True)

qc.measure(qreg_q, creg_c)

backend = Aer.get_backend("qasm_simulator")
shots = int(1024)
job = execute(qc, backend, shots=shots)
result = job.result()
counts = result.get_counts()

return counts