from pathlib import Path

folder = Path('UNIGE/Lab/Scintillator_Measurements/HalfLife_Muon/txt_data')

with open('UNIGE/Lab/Scintillator_Measurements/HalfLife_Muon/txt_data/TotalData_Deltat_Aluminium.txt', 'w', encoding='utf-8') as wf:
    for path in folder.glob("Data_*_Deltat_*.txt"):
        with path.open("r", encoding="utf-8") as f:
            data = f.read()
        wf.write(data)
    