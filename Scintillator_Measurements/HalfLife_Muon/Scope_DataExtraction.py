import pyvisa,time
import numpy as np
from decode_scope_data import LecroyScopeData

#Modify the following global variables according to the model
DSO_RSC = "TCPIP0::192.168.0.2::inst0::INSTR"

rm = pyvisa.ResourceManager('@py')
dso = rm.open_resource(DSO_RSC)
dso.timeout = 30000 #default value is 2000(2s)
dso.chunk_size = 20*1024*1024 #default value is 20*1024(20k bytes)

dso.write("TRIG:MODE SINGLE")
trig_value = -0.2

i = 0
n = 1
date = time.strftime("%d-%m_%T")
file = './Scintillator_Measurements/HalfLife_Data/txt_data/Data_' + date + '_Deltat_Aluminium.txt'
with open(file, 'w', encoding='utf-8') as f:
    while i == 0: #start taking data
        try:
            while dso.query("TRIGGER:STAT?").strip() != 'Stop':
                time.sleep(0.25)
                pass
            actual_time = time.time()
            print(time.strftime("%D %T"), '. Counts:', n)
            n += 1

            dso.write("WAV:SOUR C4")
            dso.write("WAV:PREamble?")
            recv_preamble_start = dso.read_raw()
            dso.write("WAV:DATA?")
            recv_data_start = dso.read_raw()

            dso.write("WAV:SOUR C3")
            dso.write("WAV:PREamble?")
            recv_preamble_stop = dso.read_raw()
            dso.write("WAV:DATA?")
            recv_data_stop = dso.read_raw()

            dso.write("TRIG:MODE SINGLE") #start collecting data another time

            waveform_start = LecroyScopeData(recv_preamble_start,recv_data_start)
            waveform_stop = LecroyScopeData(recv_preamble_stop,recv_data_stop)

            voltage_start = waveform_start.y
            t_start = waveform_start.x
            voltage_stop = waveform_stop.y
            t_stop = waveform_stop.x

            time_start = t_start[np.where(voltage_start<trig_value)][0]
            time_stop = t_stop[np.where(voltage_stop<trig_value)][0]
            time_diff = time_stop - time_start

            line =  str(time_diff*1e6) + ',' + str(actual_time) + '\n'
            f.write(line)
        except Exception as error:
            file_error = './Scintillator_Measurements/HalfLife_Data/txt_data/Data_' + date + '_errors_Aluminium.txt'
            with open(file_error, 'w', encoding='utf-8') as e:
                out = error.strip() + "\n"
                e.write(out)
            pass