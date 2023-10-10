from qiskit import QuantumCircuit, execute, Aer
from qiskit import QuantumRegister, ClassicalRegister


# Circuito rango (0,6)=[1,5]
qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(3, 'c')

# Crea el circuito
rango_1_4 = QuantumCircuit(qreg_q, creg_c)

rango_1_4.x(qreg_q[2])
rango_1_4.z(qreg_q[2])
rango_1_4.x(qreg_q[2])

rango_1_4.x(qreg_q[1])

rango_1_4.cz(qreg_q[1], qreg_q[2])

rango_1_4.x(qreg_q[1])

rango_1_4.x(qreg_q[0])
rango_1_4.x(qreg_q[1])
rango_1_4.x(qreg_q[2])

# Multicontrolada Z
rango_1_4.h(qreg_q[2])
rango_1_4.mcx([qreg_q[0], qreg_q[1]], qreg_q[2])
rango_1_4.h(qreg_q[2])

rango_1_4.x(qreg_q[0])
rango_1_4.x(qreg_q[1])
rango_1_4.x(qreg_q[2])

rango_1_4.measure(qreg_q, creg_c)

backend = Aer.get_backend("qasm_simulator")
shots = int(1024)
job = execute(rango_1_4, backend, shots=shots)
result = job.result()
counts = result.get_counts()

return counts

    