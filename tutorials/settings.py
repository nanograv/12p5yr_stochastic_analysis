# includes matplotlib settings and small functions to
# make the other notebooks look a little shorter

import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
import glob, pickle, os
from enterprise.pulsar import Pulsar


def load_pulsars(datadir, PINT=False, ephemeris='DE438', save=False):
    """
    This is specific to the file structure used in this tutorial.
    If you use a different file structure, this function will need to be modified!
    """
    psrlist = None # define a list of pulsar name strings that can be used to filter.
    # for the entire pta
    parfiles = sorted(glob.glob(datadir + '/par/*par'))
    timfiles = sorted(glob.glob(datadir + '/tim/*tim'))

    if not parfiles or not timfiles:
        print('Check that your data directory exists and has the right folder structure.')
        print('If you interupted this function, you may have to reset the kernel and try again.')

    # filter
    if psrlist is not None:
        parfiles = [x for x in parfiles if x.split('/')[-1].split('.')[0] in psrlist]
        timfiles = [x for x in timfiles if x.split('/')[-1].split('.')[0] in psrlist]

    # Make sure you use the tempo2 parfile for J1713+0747!!
    # ...filtering out the tempo parfile... 
    if PINT:
        parfiles = [x for x in parfiles if 'J1713+0747_NANOGrav_12yv3.gls.t2.par' not in x]
    else:
        parfiles = [x for x in parfiles if 'J1713+0747_NANOGrav_12yv3.gls.par' not in x]
    # check for file and load pickle if it exists:
    pickle_loc = datadir + '/psrs.pkl'
    if os.path.exists(pickle_loc):
        with open(pickle_loc, 'rb') as f:
            psrs = pickle.load(f)
        return psrs

    # else: load them in slowly:
    else:
        psrs = []
        for p, t in zip(parfiles, timfiles):
            if PINT:
                psr = Pulsar(p, t, ephem=ephemeris, timing_package='PINT')
            else:
                psr = Pulsar(p, t, ephem=ephemeris)
            psrs.append(psr)
        if save:
            # Make your own pickle of these loaded objects to reduce load times significantly
            # at the cost of some space on your computer (~1.8 GB).
            with open(datadir + '/psrs.pkl', 'wb') as f:
                pickle.dump(psrs, f)
        return psrs


def fd_rule(chain):
    """
    Freedman-Diaconus rule to find optimal bin width
    """
    return 2 * sps.iqr(chain) / (len(chain))**(1/3)


def fd_bins(chain, logAmin=-20, logAmax=-12):
    """
    Get bins for use with histograms using the FD rule
    """
    width = fd_rule(chain)
    bins = np.arange(logAmin, logAmax, width)
    return bins


def figsize(scale):
    fig_width_pt = 513.17 #469.755    # Get this from LaTeX using \the\textwidth
    inches_per_pt = 1.0 / 72.27         # Convert pt to inch
    golden_mean = (np.sqrt(5.0)-1.0)/2.0    # Aesthetic ratio
    fig_width = fig_width_pt * inches_per_pt * scale  # width in inches
    fig_height = fig_width * golden_mean              # height in inches
    fig_size = [fig_width, fig_height]
    return fig_size


def matplotsettings():
    ## Plotting Parameters For matplotlib
    plt.rcParams.update(plt.rcParamsDefault)
    params = {'backend': 'pdf',
            'axes.labelsize': 10,
            'lines.markersize': 4,
            'font.size': 10,
            'xtick.major.size':6,
            'xtick.minor.size':3,
            'ytick.major.size':6,
            'ytick.minor.size':3,
            'xtick.major.width':0.5,
            'ytick.major.width':0.5,
            'xtick.minor.width':0.5,
            'ytick.minor.width':0.5,
            'lines.markeredgewidth':1,
            'axes.linewidth':1.2,
            'legend.fontsize': 7,
            'xtick.labelsize': 10,
            'ytick.labelsize': 10,
            'savefig.dpi':200,
            'path.simplify':True,
            'figure.figsize': figsize(0.5)}
    plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
    plt.rcParams.update(params)