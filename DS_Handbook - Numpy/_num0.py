# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:39:57 2018

@author: evan9
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

data = pd.read_csv(r"C:\PyCodes\PythonDataScienceHandbook Sample Code\notebooks\data\Seattle2014.csv")
rainfall_mm = np.array(data['PRCP'])
rainfall_inch = rainfall_mm / 254

seaborn.set()
plt.hist(rainfall_inch, 40)
