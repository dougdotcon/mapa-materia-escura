# ACT Dark Matter Map

This repository documents the creation of the **largest and most detailed dark matter map ever produced** from the Cosmic Microwave Background (CMB), utilizing data from the **Atacama Cosmology Telescope (ACT)**. The project combines advanced instrumentation, sophisticated algorithms, and open-source software to unveil the invisible mass distribution in the Universe.

---

## Overview

Dark matter constitutes approximately 85% of the matter in the cosmos, yet it emits no light. To map it, scientists analyze how its gravity distorts the light of the CMB—the remnant radiation from the Big Bang. The ACT observed this radiation with high resolution, enabling the reconstruction of a detailed map of dark matter over billions of light-years.

---

## Technologies and Software Used

- **Gravitational Lensing Reconstruction**: Algorithm based on *quadratic estimators* (Hu & Okamoto 2002), implemented with open-source packages:
  - **Falafel**: Curved sky calculations
  - **Tempura**: Normalization and noise corrections
- **Python** and libraries:
  - **Astropy**: Astronomical calculations
  - **Healpy/HEALPix**: Spherical map manipulation
  - **Matplotlib**, **PIL**: Visualization
- **Theoretical Calculation**:
  - **CAMB**: Generation of theoretical CMB and lens spectra
- **Statistical Inference**:
  - **Cobaya**, **GetDist**, **CosmoSIS**: Bayesian fitting and MCMC analysis for cosmological parameters
- **High-Performance Computing**:
  - Clusters and supercomputers (Princeton, SciNet, NERSC) to process large volumes of data and simulations

---

## Methodology Summary

1. **Data Collection**: ACT observations from 2017-2021 covering ~9400 deg² of the sky.
2. **Data Cleaning**: Removal of contaminant signals (point sources, dust, Sunyaev-Zel'dovich effects) using multi-frequency techniques and bias-hardening.
3. **Lensing Reconstruction**: Application of the quadratic estimator to extract the gravitational lensing signal and generate the convergence map (dark matter).
4. **Calibration and Corrections**: Use of simulations to remove statistical biases and validate the map.
5. **Cross-Validation**: Comparison with Planck satellite data and galaxy catalogs, confirming the result's consistency with the standard cosmological model.

---

## Data and Instruments

- **Primary Source**: Cosmic Microwave Background (CMB) observed by the ACT, a 6-meter telescope in Chile.
- **Instrumentation**: Superconducting detectors operating at cryogenic temperatures for high sensitivity.
- **Auxiliary Data**: Maps from the Planck satellite for cleaning and validation.
- **Available Products**:
  - Gravitational convergence maps (dark matter)
  - Separated temperature/polarization maps
  - Simulations for testing and validation
  - Detailed documentation

---

## How to Access Data and Code

- **Public Data**: Available at the NASA [LAMBDA repository](https://lambda.gsfc.nasa.gov/product/act/actadv_dr6_lensing_maps_info.html).
- **Source Code**: Scripts and pipelines used for processing are available within this repository.

---

## Getting Started

*Prerequisites: Python 3.8+, CAMB, Falafel, Tempura, Healpy.*

1. **Clone the repository:**
   bash
   git clone https://github.com/yourusername/act-dark-matter-map.git
   cd act-dark-matter-map
   

2. **Install dependencies:**
   bash
   pip install -r requirements.txt
   

3. **Run the visualization script:**
   bash
   python scripts/visualize_map.py
   

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
