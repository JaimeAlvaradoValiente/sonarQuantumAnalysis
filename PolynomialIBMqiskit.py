from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from qiskit.circuit.library import QFT

# Create a quantum circuit
qreg = QuantumRegister(6)
creg = ClassicalRegister(6)
qc = QuantumCircuit(qreg, creg)

# Coefficients of the polynomial a_d, a_{d-1}, ..., a_0
coefficients = [2, 1, 0, 3]  

# Initialize the f register in the |0> state
qc.initialize([1, 0], qreg[0])

# Build the oracle for evaluating p(x)

# Apply an X gate if the coefficient is non-zero for each coefficient
qc.cx(qreg[0], qreg[0])  # coefficient 2
qc.cx(qreg[1], qreg[0])  # coefficient 1
# coefficient 0, no action required
qc.cx(qreg[3], qreg[0])  # coefficient 3

# Apply a controlled X power increment gate for each coefficient (except the last one)
qc.h(qreg[0])
qc.cx(qreg[0], qreg[1])
qc.h(qreg[0])
qc.h(qreg[1])
qc.cx(qreg[1], qreg[2])
qc.h(qreg[1])
qc.h(qreg[2])
qc.cx(qreg[2], qreg[3])
qc.h(qreg[2])

# Perform quantum inversion

# Apply Hadamard gates to all qubits
qc.h(qreg)

# Apply a controlled-Z gate on the first qubit (the target qubit)
qc.z(qreg[0])

# Apply Hadamard gates again to all qubits
qc.h(qreg)

# Measure the qubits in the variable x
qc.measure(qreg, creg)

backend = Aer.get_backend("qasm_simulator")
shots = int(1024)
job = execute(qc, backend, shots=shots)
result = job.result()
counts = result.get_counts()

return counts
