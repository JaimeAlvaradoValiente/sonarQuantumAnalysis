from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from numpy import pi
from qiskit.providers.basic_provider import BasicProvider
from qiskit_ibm_provider import IBMProvider
import qiskit.qasm3
qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)
gate_machines_arn= {"local":"local", "ibm_brisbane":"ibm_brisbane", "ibm_osaka":"ibm_osaka", "ibm_kyoto":"ibm_kyoto", "simulator_stabilizer":"simulator_stabilizer", "simulator_mps":"simulator_mps", "simulator_extended_stabilizer":"simulator_extended_stabilizer", "simulator_statevector":"simulator_statevector"}
circuit.measure(qreg_q[0], creg_c[0])
if machine == "local":
    backend = BasicProvider().get_backend("basic_simulator")
    x=int(shots)
    transpiled_circuit = transpile(circuit, backend)
    job = backend.run(transpiled_circuit, shots=x)
    result = job.result()
    counts = result.get_counts()
    return counts
else:
    provider = IBMProvider()
    backend = provider.get_backend(gate_machines_arn[machine])
    x=int(shots)
    transpiled_circuit = transpile(circuit, backend)
    job = backend.run(transpiled_circuit, backend, shots=x)
    result = job.result()
    counts = result.get_counts()
    return counts
