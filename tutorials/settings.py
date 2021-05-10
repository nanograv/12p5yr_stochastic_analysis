# includes matplotlib settings and small functions to
# make the other notebooks look a little shorter


def trim_set(parfiles, timfiles):
    """
    Trim full pulsar set down to those timed >6 years.

    Use this if you want sampling to go a little faster. The results will be different
    than the full pulsar list.

    Inputs:
        parfiles (list): list of all .par file location strings
        timfiles (list): list of all .tim file location strings

    Outputs:
        parfiles_cut (list): list of .par files for subset of pulsars
        timfiles_cut (list): list of .tim files for subset of pulsars
    """
    psr_names = ['B1855+09', 'B1937+21', 'J0030+0451', 'J0613-0200',
                 'J0645+5158', 'J1012+5307', 'J1024-0719', 'J1455-3330',
                 'J1600-3053', 'J1614-2230', 'J1640+2224', 'J1643-1224',
                 'J1713+0747', 'J1738+0333', 'J1744-1134', 'J1903+0327',
                 'J1909-3744', 'J1910+1256', 'J1918-0642', 'J1944+0907',
                 'J2010-1323', 'J2145-0750', 'J2317+1439']
    parfiles_cut = []
    timfiles_cut = []
    for par in parfiles:
        if par.split('/')[-1].split('_')[0] in psr_names:
            parfiles_cut.append(par)
    for tim in timfiles:
        if tim.split('/')[-1].split('_')[0] in psr_names:
            timfiles_cut.append(tim)
    return parfiles_cut, timfiles_cut