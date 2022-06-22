# Correction
## Feature detection network-based correction method for accurate nano-tomography reconstruction


## Abstract

Driven by the development of advanced X-ray optics, such as Fresnel zone plates, nano-resolution full-field transmission X-ray microscopy (Nano-CT) has become a powerful technique for the non-destructive volumetric inspection of objects and has long been developed at different synchrotron radiation facilities. However, the nano-tomography data are often associated with a random sample jitter because of the drift or the radial/axial error motion of the rotate stage during the measurement. Without a proper sample jitter correction process prior to the reconstruction, the use of Nano-CT in providing accurate 3D structure information for the sample is almost impossible. In this paper, to realize the accurate 3D reconstruction for the Nano-CT, an accurate correction method based on feature detection neural network, which can automatically extract the target feature from the projective image and precisely correct the sample jitter errors, is proposed, thereby resulting in a high-quality nanoscale 3D reconstruction. We demonstrated the validity of the proposed method using simulated and experimental datasets. Compared with the traditional correction method, even if the target feature is overlapped by other high-density materials or impurities, the proposed correction method still has the advantages of high precision, lower experimental costs, and fast calculation for the Nano-CT reconstruction.

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
