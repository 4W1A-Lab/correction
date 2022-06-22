# Correction
## Feature detection network-based correction method for accurate nano-tomography reconstruction


## Abstract

Driven by the development of advanced X-ray optics such as Fresnel zone plates, nano-resolution full-field transmission X-ray microscopy (Nano-CT) has become a powerful technique for the non-destructive volumetric inspection of objects and has long been developed at different synchrotron radiation facilities. However, the Nano-CT data are often associated with a random sample jitter because of the drift or radial/axial error motion of the rotation stage during measurement. Without a proper sample jitter correction process prior to reconstruction, the use of Nano-CT in providing accurate 3D structure information for samples is almost impossible. In this paper, to realise accurate 3D reconstruction for Nano-CT, a correction method based on feature detection neural network, which can automatically extract target features from a projective image and precisely correct sample jitter errors, is proposed, thereby resulting in high-quality nanoscale 3D reconstruction. Compared with other feature detection methods, even if the target feature is overlapped by other high-density materials or impurities, the proposed Nano-CT correction method still acquires sub-pixel accuracy in geometrical correction and is more suitable for Nano-CT reconstruction because of its universal and faster correction speed. The simulated and experimental datasets demonstrated the reliability and validity of the proposed Nano-CT correction method.

<img src="https://github.com/4W1A-Lab/correction/blob/main/Figure/fig5.tif" width="600px">

## Workflow 
The workflow is shown in the figure below:

<img src="https://github.com/4W1A-Lab/correction/blob/main/Figure/fig1.tif" width="600px">

## Network structure 
The network structure is shown in the figure below

<img src="https://github.com/4W1A-Lab/correction/blob/main/Figure/fig2.tif" width="600px">

## Getting Started

## Installation
* 1.Clone this repository via git clone https://github.com/4W1A-Lab/correction.git
* 2.Install dependencies and current repo
```
pip install -r requirements.txt
```

## Training on your own dataset

Train a new model starting from your own dataset:
```
python3 train.py train --train_dataroot=/path/to/data/train/ --test_dataroot=/path/to/data/test/ --model_dir=/path/to/your/model/
```
evaluat a new model starting from your own dataset:
```
python3 evaluation.py train --test__path=/path/to/data/evaluation/ --model_dir=/path/to/your/model/
```

## Citation 
Use this bibtex to cite this repository:
```
@article{jiang_lib_segmentation2020,
  title={Feature detection network-based correction method for accurate nano-tomography reconstruction},
  author={Tianyu Fu, Kai Zhang， Yan Wang, Shanfeng Wang, Jin Zhang, Chunxia Yao, Chenpeng Zhou, Wanxia Huang,and Qingxi Yuan},
  journal={Applied Optics},
  year={2022},
}
```

## Contributing
Contributions to this repository are always welcome. Examples of things you can contribute:

* Accuracy Improvements.
* Training on your own data and release the trained models.
* Visualizations and examples.
## Requirements
Python 3.7, tensorflow 1.15.0 and other common packages listed in requirements.txt.
