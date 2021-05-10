# includes matplotlib settings and small functions to
# make the other notebooks look a little shorter

def matplotsettings():
    ## Plotting Parameters For matplotlib
    def figsize(scale):
        fig_width_pt = 513.17 #469.755    # Get this from LaTeX using \the\textwidth
        inches_per_pt = 1.0 / 72.27         # Convert pt to inch
        golden_mean = (np.sqrt(5.0)-1.0)/2.0    # Aesthetic ratio
        fig_width = fig_width_pt * inches_per_pt * scale  # width in inches
        fig_height = fig_width * golden_mean              # height in inches
        fig_size = [fig_width, fig_height]
        return fig_size

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
            'font.family': 'serif',
            'font.serif':'Times',
            'text.latex.preamble': [r'\usepackage{amsmath}'],
            'text.usetex':True,
            'figure.figsize': figsize(0.5)}

    plt.rcParams.update(params)