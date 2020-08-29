# dwg_tutorials

<!--[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nanograv/dwg_tutorials/master)-->
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

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

2. Create a conda environment. Environments are a simple way to create an enclosed sandbox for all of the software for a given project. It will not pollute any other version of python or others versions of your software, provided you stay in the environment. 
	
	* See https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html.
	* Simple environment: `conda create -n test_env python=3.7 numpy scipy matplotlib Cython basemap pandas astropy jupyter notebook mpi4py h5py`
	* To enter the environment: `conda activate test_env`
	* Once inside, to install other packages: `conda install <package_name>`
	* To exit the environment: `conda deactivate`
	* To delete the environment: `conda remove --name test_env --all`

3. To install a new environment from a yaml file: `conda env create --file environment.yaml`

