import pyvisa,time
import matplotlib.pyplot as plt
from lecroy_scope_data import LecroyScopeData

#Modify the following global variables according to the model
MODEL = "T3DSO2354A"
DSO_RSC = "TCPIP0::10.195.51.175::inst0::INSTR"

_rm = pyvisa.ResourceManager('@py')
dso = _rm.open_resource(DSO_RSC)
print(dso.query("*IDN?"))

dso.timeout = 30000 #default value is 2000(2s)
dso.chunk_size = 20*1024*1024 #default value is 20*1024(20k bytes)

minimum = []
t_end = time.time() + 30

while time.time() < t_end:
    dso.write("TRIG:MODE SINGLE")

    while dso.query("TRIGGER:STAT?").strip() != 'Stop':
        #time.sleep(0.5)
        print(dso.query("TRIGGER:STAT?"))

    dso.write("WAV:SOUR C1")
    dso.write("WAV:PREamble?")
    recv_preamble = dso.read_raw()

    dso.write("WAV:DATA?")
    recv_data = dso.read_raw()

    waveform = LecroyScopeData(recv_preamble,recv_data)
    voltage = waveform.y
    m = min(voltage)
    minimum.append(m)

print(len(minimum))
plt.hist(minimum,bins = 20)
plt.show()