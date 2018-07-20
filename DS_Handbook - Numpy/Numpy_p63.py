# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 15:59:51 2018

@author: evan9
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

data = pd.read_csv(r"C:\PyCodes\PythonDataScienceHandbook Sample Code\notebooks\data\president_heights.csv")
heights = np.array(data['height(cm)'])
print(heights)
print('Average:', heights.mean())
print('Standard Deviation:', heights.std())
print('Minimum:', heights.min())
print('Maximum:', heights.max())
print('Median:', np.median(heights))
print('25th Percentile:', np.percentile(heights, 25))
print('50th Percentile:', np.percentile(heights, 50))
print('75th Percentile:', np.percentile(heights, 75))

seaborn.set()
plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')
