# MSLesSeg-2024: baseline and benchmarking of a new Multiple Sclerosis Lesion Segmentation dataset 

This is the official implementation of the preprocessing applied to the MSLesSeg-2024 dataset, described in the paper:  
["MSLesSeg-2024: baseline and benchmarking of a new Multiple Sclerosis Lesion Segmentation dataset "]()

## Abstract
This paper presents MSLesSeg-2024, a new, publicly accessible MRI dataset designed to advance research in Multiple Sclerosis (MS) lesion segmentation. The dataset comprises 115 scans of 75 patients including T1, T2 and FLAIR sequences, along with supplementary clinical data collected across different sources. Expert-validated annotations provide high-quality lesion segmentation labels, establishing a reliable human-labeled dataset for benchmarking. Part of the dataset was shared with expert scientists with the aim to compare the last automatic AI-based image segmentation solutions with an expert-biased handmade segmentation. In addiction, an AI-based lesion segmentation of MSLesSeg-2024 was developed and technically validated against the last state-of-the-art methods. The dataset, the detailed analysis of researcher contributions, and the baseline results presented here mark a significant milestone for advancing automated MS lesion segmentation research.

## Preprocessing
All MRI scans in the dataset underwent the following preprocessing:


* Co-registration to the MNI152 isotropic template, implemented in FSL as `flirt`
* Brain Extraction, using the BET tool implemented in FSL as `bet`

## Requirements
* Linux (if on Windows use WSL as per [the FSL docs](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation/Windows))
* [FSL](https://fsl.fmrib.ox.ac.uk)
* [Python 3](https://www.python.org/downloads/)


## Usage
```
usage: python registration.py --dataset_dir DIRNAME --ref_template TEMPLATE

arguments:
  --dataset_dir      Path to the MSLesSeg-RAW dataset
  --ref_template     "Path to the MNI152 template. Default: ./resources/MNI152_T1_1mm.nii.
```
