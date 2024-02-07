from qiskit import execute, QuantumRegister, ClassicalRegister, QuantumCircuit, Aer
from numpy import pi
from qiskit import IBMQ
qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)
gate_machines_arn= {"local":"local", "ibm_brisbane":"ibm_brisbane", "ibm_osaka":"ibm_osaka", "ibm_kyoto":"ibm_kyoto", "simulator_stabilizer":"simulator_stabilizer", "simulator_mps":"simulator_mps", "simulator_extended_stabilizer":"simulator_extended_stabilizer", "simulator_statevector":"simulator_statevector"}
circuit.h(qreg_q[0])
circuit.x(qreg_q[1])
circuit.x(qreg_q[2])
circuit.h(qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])
circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[2], creg_c[2])
if machine == "local":
    backend = Aer.get_backend("qasm_simulator")
    x=int(shots)
    job = execute(circuit, backend, shots=x)
    result = job.result()
    counts = result.get_counts()
    return counts
else:
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub="ibm-q", group="open", project="main")
    backend = provider.get_backend(gate_machines_arn[machine])
    x=int(shots)
    job = execute(circuit, backend, shots=x)
    result = job.result()
    counts = result.get_counts()
    return counts
