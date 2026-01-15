# 📡 Data Setup: ACT DR6 Lensing Map

To run the TARDIS verification suite, we need the official gravitational lensing map from the Atacama Cosmology Telescope (ACT) Data Release 6.

## 1. Download the Data

**Source:** NASA LAMBDA Archive
**URL:** [https://lambda.gsfc.nasa.gov/product/act/act_dr6_lensing_get.html](https://lambda.gsfc.nasa.gov/product/act/act_dr6_lensing_get.html)

### Required File

- **Filename:** `act_dr6_lens_kappa_baseline_v1.fits` (or similar baseline map)
- **Description:** CMB Lensing Convergence Map ($\kappa$)

## 2. Install Location

Place the downloaded `.fits` file in the `assets/` directory of this repository.

```
mapa-materia-escura/
└── assets/
    └── act_dr6_lens.fits  <-- RENAME to this
```

## 3. Alternative (Synthetic Mode)

If you cannot download the 500MB+ file right now, the `verify_lensing_omega.py` script includes a **Synthetic Mode**. It will generate a mock high-resolution CMB lensing map based on $\Lambda$CDM power spectra to test the TARDIS algorithms.

> **To run in synthetic mode, just execute the script without arguments.**
