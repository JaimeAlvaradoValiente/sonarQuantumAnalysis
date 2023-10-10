from qiskit import QuantumCircuit, execute, Aer
from qiskit import QuantumRegister, ClassicalRegister


# Define los registros cuÃ¡nticos y clÃ¡sicos
qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')

# Crea el circuito
menor_11 = QuantumCircuit(qreg_q, creg_c)

menor_11.x(qreg_q[3])
menor_11.x(qreg_q[2])
menor_11.z(qreg_q[3])
menor_11.x(qreg_q[3])
menor_11.x(qreg_q[1])

# Multicontrolada Z
menor_11.h(qreg_q[1])
menor_11.mcx([qreg_q[3], qreg_q[2]], qreg_q[1])
menor_11.h(qreg_q[1])

menor_11.x(qreg_q[1])
menor_11.x(qreg_q[0])

# Multicontrolada Z
menor_11.h(qreg_q[0])
menor_11.mcx([qreg_q[1], qreg_q[2], qreg_q[3]], qreg_q[0])
menor_11.h(qreg_q[0])

menor_11.x(qreg_q[2])
menor_11.x(qreg_q[0])

menor_11.measure(qreg_q, creg_c)

backend = Aer.get_backend("qasm_simulator")
shots = int(1024)
job = execute(menor_11, backend, shots=shots)
result = job.result()
counts = result.get_counts()

return counts