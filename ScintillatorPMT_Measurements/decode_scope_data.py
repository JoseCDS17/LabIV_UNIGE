import struct
import numpy as np
from datetime import datetime

class LecroyScopeData:
  """
  Class that represents a Lecroy Scope data, containing all its information.
  The parsing relies heavily on struct.

  """

  _map_timebase = ['200 ps/div', '500 ps/div', '1 ns/div', '2 ns/div', '5 ns/div', '10 ns/div', '20 ns/div', '50 ns/div', '100 ns/div', '200 ns/div', '500 ns/div', '1 us/div', '2 us/div', '5 us/div', '10 us/div', '20 us/div', '50 us/div', '100 us/div', '200 us/div', '500 us/div', '1 ms/div', '2 ms/div', '5 ms/div', '10 ms/div', '20 ms/div', '50 ms/div', '100 ms/div', '200 ms/div', '500 ms/div', '1 s/div', '2 s/div', '5 s/div', '10 s/div', '20 s/div', '50 s/div', '100 s/div', '200 s/div', '500 s/div', '1 ks/div']

  _map_probe_attenuation = [0.1, 0.2, 0.5, 1., 2., 5., 10., 20., 50., 100., 200., 500., 1000., 2000., 5000., 10000.]

  # _map_fixed_vert_gain = ['1 uV/div', '2 uV/div', '5 uV/div', '10 uV/div', '20 uV/div', '50 uV/div', '100 uV/div', '200 uV/div', '500 uV/div', '1 mV/div', '2 mV/div', '5 mV/div', '10 mV/div', '20 mV/div', '50 mV/div', '100 mV/div', '200 mV/div', '500 mV/div', '1 V/div', '2 V/div', '5 V/div', '10 V/div', '20 V/div', '50 V/div', '100 V/div', '200 V/div', '500 V/div', '1 kV/div']

  _map_wave_source = {0: 'CHANNEL 1', 1: 'CHANNEL 2', 2: 'CHANNEL 3', 3: 'CHANNEL 4', 9: 'UNKNOWN'}

  _map_coupling = ['DC', 'AC', 'GND']

  # _map_processing = ['no processing', 'fir filter', 'interpolated', 'sparsed', 'autoscaled', 'no result', 'rolling', 'cumulative']

  # _map_record_type = ['single sweep', 'interleaved', 'histogram', 'graph', 'filter coefficient', 'complex', 'extrema','sequence obsolete', 'centered RIS', 'peak detect']

  def __init__(self, preamble, data):
    """
    Parses a `bytes` object and store its content as data members.

    If reading from a file:
    ```
    with open('file.trc'), 'rb') as f:
      trc_bytes = f.read()

    trc = LecroyTrc(trc_bytes)
    print(trc.x) # prints the timebase
    print(trc.y) # prints the waveforms array

    If reading from the scope directly:
    osc = LecroyVbs(rm, 'TCPIP0::10.195.49.11::INSTR')
    ...
    # setup oscilloscope
    ...

    trc_bytes = osc.inst.query_binary_values('C1:WAVEFORM?'.format(i), datatype='s')[0] # this is equivalent to the content of a TRC file
    trc = LecroyTrc(trc_bytes)
    print(trc.x) # prints the timebase
    print(trc.y) # prints the waveforms array
    ```

    See the code for all the available data members (everything of the form self.xxx is available as trc.xxx)
    """

    beginning, = struct.unpack('50s', preamble[:50])
    offset = beginning.find(b'WAVEDESC')
    # print(offset)

    descriptor, template, comm_type, comm_order = struct.unpack('16s16s2H', preamble[offset:offset+36])
    # print(descriptor, template, comm_type, comm_order)

    # TODO check this
    # if comm_order == 0:
    #   end_chr = '>' # big endian
    # else:
    #   end_chr = '<' # little endian

    wave_desc_length, _, _, _, _, _ = struct.unpack('6I', preamble[offset+36:offset+60]) # length of preamble
    # print(wave_desc_length)

    wave_array_1, _, _, _ = struct.unpack('4I', preamble[offset+60:offset+76]) # lenght of data array in bytes
    # print(wave_array_1)

    instrument_name, _, _, _ = struct.unpack('16sI16sI', preamble[offset+76:offset+116])
    # print(instrument_name)

    wave_array_count, _, _, _ = struct.unpack('4I', preamble[offset+116:offset+132]) # number of data points in data array for analog channel
    first_point, sparse_factor, _, _, _, _, _, vert_gain, vert_offset, max_value, min_value, _, _, hor_interval, hor_offset, _, _, _, _, _, _, _, _, _, _, time_base_idx, vert_coupling_idx, probe_attenuation_idx, fixed_vert_gain, bw_limit, _, _, wave_source = struct.unpack('5I2H4f2Hf2d48s48sf16sf6HI2H2fH', preamble[offset+132:offset+346]) 

    if probe_attenuation_idx > 15:
      probe_attenuation, = struct.unpack('f', preamble[offset+328:offset+332])
    else:
      probe_attenuation = self._map_probe_attenuation[probe_attenuation_idx]

    # print(first_point, sparse_factor, vert_gain, vert_offset, max_value, min_value, hor_interval, hor_offset, self._map_timebase[time_base_idx], self._map_coupling[vert_coupling_idx], probe_attenuation, fixed_vert_gain, bw_limit, wave_source)

    # print(data)
    beginning, = struct.unpack('20s', data[:20])
    offset = beginning.find(b'#')
    n_digits, = struct.unpack('s', data[offset+1:offset+2])
    n_digits = int(n_digits)
    n_data_points, = struct.unpack(f'{n_digits}s', data[offset+2:offset+2+n_digits])
    n_data_points = int(n_data_points)
    # print(n_data_points)
    
    offset = offset+2+n_digits

    if comm_type == 0:
      data_type = 'i1' # 8-bit data
    else:
      data_type = 'i2' # 16-bit data

    y_raw = np.frombuffer(data[offset:], dtype=data_type, count=n_data_points, offset=0) # waveforms in DAC counts
    # print(y_raw)

    self.y = y_raw * vert_gain / 30 - vert_offset
    # print(self.y)

    x_raw = np.arange(self.y.shape[0])
    self.x = x_raw * hor_interval + hor_offset # horizontal scale in seconds
    # print(self.x)

