# NANOGrav_12yr_tutorial <img align="right" width="150" height="100" src="https://github.com/nanograv/12p5yr_stochastic_analysis/blob/master/nanograv.png?raw=true">
## Tutorial to go with the [12.5 year GWB analysis](https://arxiv.org/abs/2009.04496)

[![Generic badge](https://img.shields.io/badge/Created%20by-NANOGrav-red)](http://nanograv.org/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/twitter/follow/NANOGrav?style=social)](https://twitter.com/NANOGrav)
 
 Authors: [Stephen Taylor](http://stevertaylor.github.io/), [Sarah Vigeland](https://github.com/svigeland), Joe Simon, [Bence Becsy](https://github.com/bencebecsy) and [Aaron Johnson](https://github.com/AaronDJohnson) for the [NANOGrav Collaboration](https://github.com/nanograv)

 Please send questions about this tutorial to `aaron.johnson (at) nanograv.org`

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


## Tutorials

### Single Pulsar GWB Analysis [Google Colab](https://colab.research.google.com/drive/1sBALRUi6wCykAAKH8Lp5TdS69QUmNgZq#scrollTo=t1FXF9NO5HpG)
	This tutorial is meant to be a quick introduction for those who don't have time to run the computations required in the full pulsar timing array (PTA) gravitational wave background (GWB) analysis. We go through the Bayesian analysis of `J1909` and `J1713`. These are two of the longest timed pulsars in the NANOGrav data set. One of the pulsars supports the GWB, while the other does not.

### White Noise Single Pulsar Analysis [Google Colab](https://colab.research.google.com/drive/11aRVepxn_whRm_JWCbgL_sVqn1hjo9Ik?usp=sharing)
	Here we go through the Bayesian analysis of white noise on a single pulsar. This is done for every pulsar in the NANOGrav data set to find the most likely values of each white noise parameter. These are then set to their most likely value in the full GWB analysis to reduce the computational time required for a full analysis.

### PTA GWB Analysis [Google Colab](https://colab.research.google.com/drive/1dwZ7ihDtpah9ATiPx2SJIWNYt9YJkQvF?usp=sharing)
	In this tutorial, we work through the Bayesian analysis of a subset of pulsars in the NANOGrav data set (those timed for more than 6 years). After going through a generalized process of the single pulsar GWB analysis, we show how to compare models and compute Bayes factors. Figures 1, 2, and part of 3 of the 12.5 year stochastic background paper are reproduced in this notebook.

### Optimal Statistic Analysis [Google Colab](https://colab.research.google.com/drive/1VNLbutN7cKJM2jl6LId0IgkGJDszDloC#scrollTo=bwMNlFWuQhnB)
	This tutorial gives an introduction to frequentist methods we can use to look for the stochastic gravitational-wave background. It calculates the optimal statistic using the maximum likelihood noise parameters and also the noise marginalized optimal statistic using the noise parameter posteriors from a Bayesian analysis. It reproduces Figure 4 and 5 of the stochastic background paper.
