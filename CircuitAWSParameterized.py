from braket.circuits import Gate
from braket.circuits import Circuit
from braket.devices import LocalSimulator
from braket.aws import AwsDevice

gate_machines_arn= {"riggeti_aspen_m3":"arn:aws:braket:us-west-1::device/qpu/rigetti/Aspen-M-3", "DM1":"arn:aws:braket:::device/quantum-simulator/amazon/dm1", "oqc_lucy":"arn:aws:braket:eu-west-2::device/qpu/oqc/Lucy", "ionq_aria1":"arn:aws:braket:us-east-1::device/qpu/ionq/Aria-1", "ionq_aria2":"arn:aws:braket:us-east-1::device/qpu/ionq/Aria-2", "ionq_forte":"arn:aws:braket:us-east-1::device/qpu/ionq/Forte", "ionq_harmony":"arn:aws:braket:us-east-1::device/qpu/ionq/Harmony", "sv1":"arn:aws:braket:::device/quantum-simulator/amazon/sv1", "tn1":"arn:aws:braket:::device/quantum-simulator/amazon/tn1", "local":"local"}
s3_folder = ("amazon-braket-7c2f2fa45286", "api")
circuit = Circuit()
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.x(0)
circuit.x(2)
circuit.x(3)
circuit.h(3)
circuit.rz(0, gamma)
circuit.cnot(3, 0)
circuit.cnot(3, 1)
circuit.cnot(3, 2)
circuit.x(0)
circuit.x(2)
circuit.h(0)
circuit.h(1)
circuit.h(2)

return executeAWS(s3_folder, gate_machines_arn[machine], circuit, shots)