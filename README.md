# Muon Detection and Mean Lifetime Measurement from Cosmic Rays

This repository contains the code and numerical notebooks developed for the course Laboratory IV of the Master in Cosmology and Astroparticles Physics, University of Geneva. The project is focused on the study of cosmic rays and muons, and its detection with PMTs and SiPMs, allowing the measurement of the mean lifetime of the muon. 


## Project Overview

The project explores the cosmic rays detection, focused on the study of muons. To detect the muons we have used photomultipliers, in particular photomultiplier tubes (PMTs) and silicon photomultipliers (SiPM). With these detectors some measurements are performed: the muon flux with respect the azimuthal angle and the muon mean lifetime. 

The project is organized into three folders: 

* **1. PMT Measurements:** The first folder contains the codes used for the experiments with the PMTs. There is a folder for the experiment of the muon lifetime, where an histogram is obtained from the measurements to calculate the value of the lifetime. In the folder are other notebooks, used for the calibration of the PMTs before the experiments and to obtain the relation of the muon flux with respect the azimuthal angle. 
* **2. SiPM:** In this folder we study the SiPMs, in particular the breakdown potencial of the detectors and the crosstalk probability. 
* **3. PMs comparison:** This last folder contains a comparison of the detectors. For this purpose, the waveform of the different detectors is plotted and other quantities like the charge or the amplitude are also studied.  


## Requirements

To run the notebooks, the following Python libraries are required:

* `numpy`
* `scipy`
* `matplotlib`
* `jupyter`
* `pyvisa`

Install them using:

```bash
pip install numpy scipy matplotlib jupyter pyvisa
```

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/JoseCDS17/LabIV_UNIGE.git
   cd LabIV_UNIGE
   ```

2. The codes can be of mainly two types:
   * *Data Extraction*: scripts used to extract information from the oscilloscope and process it with python. Use with a previous configuration of the oscilloscope. 
   * *Data Analysis*: scripts used to analyze the data obtained from the codes above. Can be runned, as the data is stored in the txt.files. 

## Final Report

For a complete theoretical explanation, please refer to the full report:

👉 [Click here to read the PDF](LabIV_MuonLifetimeExperiment.pdf)

## Author

Developed by **Jose Carlos Díaz Sierra**, **Alejandro Cabanelas Serrano** and **Steven Thomas** for the Laboratory IV, as part of Master in Cosmology and Astroparticles Physics at University of Geneva.
