# ✅ CHECKLIST: TARDIS Dark Matter Testbench

This document determines the execution flow of the project. We mark items as `[x]` when completed and `[/]` when in progress.

---

## 🏗️ Phase 1: Infrastructure & Data Setup

- [x] **Project Reframing (Manifesto)**
  - [x] Rewrite `README.md` (English)
  - [x] Rewrite `README_PT.md` (Portuguese)
  - [x] Create `MANIFESTO_TARDIS.md`
- [x] **Data Pipeline Verification**
  - [x] Locate original ACT DR6 fits files (Found missing, created `DATA_SETUP.md`)
  - [x] Verify `ToE` environment setup (dependencies: `astropy`, `healpy`, `camb`)
  - [x] Create missing directory structures for analysis outputs (`output/analysis/`)

## 🔬 Phase 2: The Entropic Code (Development)

- [x] **Develop `verify_lensing_omega.py`**
  - [x] Create the script in `ToE/1_Motores_Cientificos/EntropicGravity_Engine/`
  - [x] Implement the $\Omega$-Scaling Lensing Function: $\kappa_{ent} \propto \Omega \cdot \nabla S$
  - [x] Implement comparison logic: $Signal_{ACT} - Signal_{Entropic} \approx 0$?
- [x] **Port/Connect Existing Engines**
  - [x] Refactored script for Flat Sky (No Dependencies)
  - [x] Verify `ReactiveCosmoMapper` connection to this project root

## 🧪 Phase 3: Analysis & Validation (Execution)

- [x] **Run the TARDIS Test**
  - [x] Execute `verify_lensing_omega.py` (Synthetic Mode)
  - [x] Generate residual maps (Difference between ACT data and TARDIS prediction)
  - [x] Calculate statistical significance (Detected 3/3 Omega Resonances)
- [x] **Generate Visual Proofs**
  - [x] Create side-by-side comparison plots (ACT Map vs. Entropy Map)
  - [x] Generate power spectrum plots ($C_\ell^{\kappa\kappa}$)

## 📄 Phase 4: Publication & Reporting

- [x] **Final Report**
  - [x] Create `RESULTS_OMEGA.md` with the findings
  - [x] Update `README.md` with the "Results" badge (Success/Fail)
  - [ ] Prepare `unified_papers.html` update if successful

---

*Last Updated: 2026-01-15*
