# 
#
# This file contains code generated by A. Lambarri Martinez for the
# Galaxy Formation and Evolution course in the 
# Astrophysics Masters at UCM
#
# Version: Dic 11, 2023 @18:00
#
# SPDX-License-Identifier: GPL-3.0+
#

import pandas as pd

def LoadData(filename):
    """Loads IAC-star data file correctly. Only stars are loaded, not integrated quantitites.
       Data is read using the pandas read_csv functionality and using \s+ delimiter. Correct
       functioning is only guaranteed for IAC-star data.

       Parameters
       ----------
       filename : str
           Name of the file to be loaded.
           
       Returns
       -------
       data : pandas dataFrame
           Loaded data.
    """
    colnames = ['log(L)', 'log(Teff)', 'log(g)', 'mass_ini', 'massin', 
                'log(L2)', 'log(Teff2)', 'log(g2)', 'mass_ini2', 'massin2', 
                'age', 'Z', 'mass_2/mass_1', 
                'Mbol', 'U', 'B', 'V', 'R', 'I', 'J', 'H', 'K', 'L', 'L_prime', 'M']
    data = pd.read_csv(filename, delimiter='\s+', skiprows=[i for i in range(0,14)], skipfooter=8, names=colnames)
    return data
