from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

qr = QuantumRegister(3, 'q')
anc = QuantumRegister(1, 'ancilla')
cr = ClassicalRegister(3, 'c')
qc = QuantumCircuit(qr, anc, cr)

qc.x(anc[0])
qc.h(anc[0])
qc.h(qr[0])
qc.h(qr[1])
qc.h(qr[2])
qc.cx(qr[0], anc[0])
qc.cx(qr[1], anc[0])
qc.cx(qr[2], anc[0])
qc.h(qr[0])
qc.h(qr[1])
qc.h(qr[2])
qc.barrier(qr)
qc.measure(qr, cr)
