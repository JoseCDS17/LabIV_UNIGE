# Muon Detection and Mean Lifetime Measurement from Cosmic Rays

This repository contains the code and numerical notebooks developed for the course Laboratory IV of the Master in Cosmology and Astroparticles Physics, University of Geneva. The project is focused on the study of cosmic rays and muons, and its detection with PMTs and SiPMs, allowing the measurement of the mean lifetime of the muon. 


## Project Overview

The project explores the evolution of inflation, implemented with a scalar field, and its primordial perturbations. When inflation ends, the reheating process occurs, which is also examined. 

The project is organized into four Jupyter notebooks: 

* **1. Quartic Potential (background):** The first notebook solves the background dynamics of the inflaton field under a quartic potential. It is solve with exact numerical methods and with the slow-roll regime, comparing the results. The reheating process is also studied, with the field evolution and the equation of state during this phase. 
* **2. Quartic Potential (perturbations):** This notebook analyzes the inflation perturbations of the scalar and tensor cases. It is mainly focused on the scalar perturbations, showing the evolution of them for different variables ($\delta \phi$, $u$ and $\mathcal{R}$). The power spectrum is also obtained, along with the tensor-to-scalar ratio ($r$) and the scalar spectral index ($n_s$). 
* **3. Natural Inflation:** This third notebook studies a different model than the previous ones, the Natural Inflation. This model has not been completely discarded by the last measurements of the CMB, so it is interesting to examine. We only analyze this model with the slow-roll approximations, varying the duration of inflation and one free parameter ($f$), in order to compare the results with the CMB constraints of the primordial perturbations. 
* **4. Inflation and PBHs:** This last notebook analyzes a more complex model of inflation, which can lead to the formation of PBHs. It is studied with the exact equations and with the slow-roll approximations, to see that this model cannot be computed only with the slow-roll regime, as it fails to reproduce the complete evolution of the inflation field. We solve the background dynamics and the primordial perturbations, examining also the reheating process.


## Requirements

To run the notebooks, the following Python libraries are required:

* `numpy`
* `scipy`
* `matplotlib`
* `jupyter`

Install them using:

```bash
pip install numpy scipy matplotlib jupyter
```

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/JoseCDS17/LabIV_UNIGE.git
   cd LabIV_UNIGE
   ```

2. The folders are organised by parts: .

## Final Thesis Report

For a complete theoretical explanation, please refer to the full TFG paper:

👉 [Click here to read the PDF](0.Paper_CosmologicalPerturbations.pdf)

## Author

Developed by **Jose Carlos Díaz Sierra**, **Alejandro Cabanelas Serrano** and **Steven Thomas** for the End-of-Deegree Project, as part of the Laboratory IV of the Master in Cosmology and Astroparticles Physics at University of Geneva.
