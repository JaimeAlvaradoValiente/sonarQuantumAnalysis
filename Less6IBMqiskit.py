from qiskit import QuantumCircuit, execute, Aer
from qiskit import QuantumRegister, ClassicalRegister



# Define los registros cuÃ¡nticos y clÃ¡sicos
qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')

# Crea el circuito
menor_6 = QuantumCircuit(qreg_q, creg_c)

menor_6.x(qreg_q[3])

menor_6.x(qreg_q[2])
menor_6.cz(qreg_q[3], qreg_q[2])
menor_6.x(qreg_q[2])

menor_6.x(qreg_q[1])

# Multicontrolada Z
menor_6.h(qreg_q[1])
menor_6.mcx([qreg_q[2], qreg_q[3]], qreg_q[1])
menor_6.h(qreg_q[1])

menor_6.x(qreg_q[1])

menor_6.x(qreg_q[3])

menor_6.measure(qreg_q, creg_c)

backend = Aer.get_backend("qasm_simulator")
shots = int(1024)
job = execute(menor_6, backend, shots=shots)
result = job.result()
counts = result.get_counts()

return counts