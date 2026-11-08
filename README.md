# Quantitative Mineral Microscopy & Computer Vision Atlas

An extensible computer vision framework and open atlas designed to quantitatively characterize, index, and analyze mineral specimens using digital optical microscopy, gray-level spatial statistics, gradient tensor fields, and frequency-domain decomposition.

---

## 1. Project Overview & Architecture

Mineral identification and quality assessment are frequently limited to qualitative visual descriptions. This repository establishes a reproducible, local-first image processing pipeline to extract objective mathematical fingerprints from macroscopic and microscopic mineral surfaces.

Each cataloged specimen undergoes a standardized characterization pipeline:
* **Optics & Glare Mitigation:** Multi-angle acquisition using digital microscopy (Tomlov DM9) fitted with optical diffusion to eliminate specular sensor saturation.
* **Surface Texture Dynamics:** Gray-Level Co-occurrence Matrix (GLCM) contrast, energy, and homogeneity metrics.
* **Structural Anisotropy:** Edge-gradient vector orientation mapping (Sobel tensor field) isolating crystal growth planes and chatoyant axes.
* **Mineral Phase Quantification:** Unsupervised color clustering in CIE-L\*a\*b\* space calculating exact surface facies coverage.
* **Harmonic Periodicity:** 2D Fast Fourier Transform (FFT) spatial frequency profiling resolving micro-striations and fiber needle bundles.

---

## 2. Cataloged Specimens

| ID | Mineral Specimen | Geological Facies / Origin | Optical Phenomenon | Primary Structural Metric |
| :---: | :--- | :--- | :--- | :--- |
| **`SPEC-0001`** | **Tiger's Eye / Hawk's Eye** | Banded Iron Formation (South Africa) | Chatoyancy (Silicified Crocidolite) | 92° Axis, ~56–224 µm harmonic fiber spacing |
| `SPEC-0002` | *Upcoming Specimen* | — | — | — |

---

## 3. Specimen 0001 Case Study: South African Tiger's Eye

* **Physical Form:** $27 \times 22 \times 14\text{ mm}$ tumbled cabochon displaying both oxidized (Tiger's Eye) and unoxidized (Hawk's Eye / hematite) faces.
* **Key Findings:**
  * **Facies Asymmetry:** Face A (oxidized) exhibits $17.1\% \pm 10.2\%$ golden silk coverage with high textural contrast ($25.32 \pm 25.31$). Face B (host rock) is dominated by dark matrix ($55.3\% \pm 15.4\%$) with isolated narrow veins.
  * **Structural Continuity:** Both faces share an invariant 92° orientation peak, proving the silicified crocidolite growth layers remain parallel throughout the volume of the pebble.

---

## 4. Repository Structure

```text
├── docs/                           # Interactive GitHub Pages Atlas
│   ├── index.html                  # Specimen gallery & data viewer
│   ├── data.json                   # Aggregated feature vectors
│   └── assets/thumbnails/          # Downsampled, watermarked preview assets
├── data/
│   ├── raw/                        # Local raw captures (gitignored)
│   └── processed/                  # Normalized feature datasets
├── scripts/
│   └── extract_features.py         # Standardized batch extraction pipeline
├── inspect_tiger_eye.ipynb         # Exploratory notebook for SPEC-0001
├── requirements.txt
└── .gitignore