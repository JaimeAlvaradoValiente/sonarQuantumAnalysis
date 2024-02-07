from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from numpy import pi
from qiskit import IBMQ

qc = QuantumCircuit(4, 4)
gate_machines_arn= {"local":"local", "ibm_brisbane":"ibm_brisbane", "ibm_osaka":"ibm_osaka", "ibm_kyoto":"ibm_kyoto", "simulator_stabilizer":"simulator_stabilizer", "simulator_mps":"simulator_mps", "simulator_extended_stabilizer":"simulator_extended_stabilizer", "simulator_statevector":"simulator_statevector"}


qc.h(0)
qc.h(1)
qc.cx(0, 1)
qc.rz(gamma, 1)
qc.cx(0, 1)
qc.h(2)
qc.cx(0, 2)
qc.rz(gamma, 2)
qc.cx(0, 2)
qc.rx(beta, 0)
qc.cx(1, 2)
qc.rz(gamma, 2)
qc.cx(1, 2)
qc.h(3)
qc.cx(1, 3)
qc.rz(gamma, 3)
qc.cx(1, 3)
qc.rx(beta, 1)
qc.cx(2, 3)
qc.rz(gamma, 3)
qc.cx(2, 3)
qc.rx(beta, 2)
qc.rx(beta, 3)

qc.barrier(range(4))
qc.measure(range(4), range(4))


if machine == "local":
    backend = Aer.get_backend("qasm_simulator")
    x=int(shots)
    job = execute(qc, backend, shots=x)
    result = job.result()
    counts = result.get_counts()
    return counts
else:
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub="ibm-q", group="open", project="main")
    backend = provider.get_backend(gate_machines_arn[machine])
    x=int(shots)
    job = execute(qc, backend, shots=x)
    result = job.result()
    counts = result.get_counts()
    return counts