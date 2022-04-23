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

	* Either...download and install the relevant Miniforge file from here: https://docs.conda.io/en/latest/miniconda.html
	* OR... use Terminal command line installation
		* Download the right one for your architecture
			* Mac: `wget -q https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh`
        * `bash Miniforge3-MacOSX-x86_64.sh -b`
		    * `rm Miniforge3-MacOSX-x86_64.sh` (careful with “rm”)
			* Linux: `wget -q https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh`
        * `bash Miniforge3-Linux-x86_64.sh -b`
		    * `rm Miniforge3-Linux-x86_64.sh` (careful with “rm”)
      * `enterprise` dependencies do not currently support Windows or M1 Macs

2. To install a new environment: `conda create -n enterprise enterprise_extensions la_forge`
  * Note: if you use Miniconda or Anaconda instead of Miniforge, you will need to use `conda create -n enterprise -c conda-forge enterprise_extensions la_forge`

3. This will create a conda environment that can be activated by `conda activate enterprise`

6. Open a `jupyter notebook`

7. Set the Kernel

  * when opening a new notebook: click `New` and select `Python [conda env:enterprise]`  
  * when opening an existing notebook (like this tutorial): click `Kernel` --> `Change Kernel` --> `Python [conda env:enterprise]`  


## Tutorials

  These tutorials are split into several different files. General topics are shown below.

### Single Pulsar GWB Analysis

  This tutorial is meant to be a quick introduction for those who don't have time to run the computations required in the full pulsar timing array (PTA) gravitational wave background (GWB) analysis. We go through the Bayesian analysis of `J1909` and `J1713`. These are two of the longest timed pulsars in the NANOGrav data set. One of the pulsars supports a common red process, while the other does not.

### White Noise Single Pulsar Analysis

  Here we go through the Bayesian analysis of white noise on a single pulsar. This is done for every pulsar in the NANOGrav data set to find the most likely values of each white noise parameter. White noise parameters are then set to their maximum posterior values in the full GWB analysis to reduce the number of parameters required for a full analysis.

### PTA GWB Analysis
  
  In this tutorial, we work through the Bayesian analysis of a subset of pulsars in the NANOGrav data set (those timed for more than 6 years). After going through a generalized process of the single pulsar GWB analysis, we show how to compare models and compute Bayes factors.

### Optimal Statistic Analysis
	
  This tutorial gives an introduction to frequentist methods we can use to look for the stochastic gravitational-wave background. It calculates the optimal statistic using the maximum likelihood noise parameters and also the noise marginalized optimal statistic using the noise parameter posteriors from a Bayesian analysis. It reproduces Figure 4 and 5 of the stochastic background paper.
