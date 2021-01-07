# NANOGrav_12yr_tutorial <img align="right" width="150" height="100" src="https://github.com/nanograv/12p5yr_stochastic_analysis/blob/master/nanograv.png?raw=true">
## Tutorial to go with the 12.5 year GWB analysis

[![Generic badge](https://img.shields.io/badge/Created%20by-NANOGrav-red)](http://nanograv.org/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/twitter/follow/NANOGrav?style=social)](https://twitter.com/NANOGrav)
 
 Authors: [Stephen Taylor](http://stevertaylor.github.io/), [Sarah Vigeland](https://github.com/svigeland), Joe Simon, [Bence Becsy](https://github.com/bencebecsy) and [Aaron Johnson](https://github.com/AaronDJohnson) for the [NANOGrav Collaboration](https://github.com/nanograv)

 Please send questions about this tutorial to `aaron.johnson (at) nanograv.org`
 
 If you are interested in working through this notebook, but do not want to install the software, we have prepared a related Google Colab notebook: https://colab.research.google.com/drive/1xft6F9nyoEHUVn1LbW-0qgXiiKDJuR3X#scrollTo=7kVh83a8w36s

 By copying this notebook, you can install the software to your own Google account and run the software without installation on your computer.

## Installing PTA software

1. Install Miniconda

	* Either...download and install the relevant Miniconda file from here: https://docs.conda.io/en/latest/miniconda.html
	* OR... use Terminal command line installation
		* Download the right one for your architecture
			* Mac: `wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh`
			* Linux: `wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh`
			* Windows (untested): `wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe`

		* `bash Miniconda3-latest-Linux-x86_64.sh -b`
		* `rm Miniconda3-latest-Linux-x86_64.sh` (careful with “rm”)

2. Make sure you have compiler tools for Mac or Linux (Windows is currently not supported)
	* For Mac: in a terminal run `xcode-select --install` to install command line tools
	* For Linux: in a terminal run `apt-get install gcc g++ gfortran`

3. To install a new environment from a yml file: `conda env create -f environment.yml`

4. This will create a conda environment that can be activated by `conda activate enterprise`

5. After activating install `nb_conda` by `conda install nb_conda`

6. Open a `jupyter notebook`

7. Set the Kernel

   * when opening a new notebook: click `New` and select `Python [conda env:enterprise]`  
   * when opening an existing notebook (like this tutorial): click `Kernel` --> `Change Kernel` --> `Python [conda env:enterprise]`  
