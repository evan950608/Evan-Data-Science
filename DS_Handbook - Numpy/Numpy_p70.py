# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:33:36 2018

@author: evan9
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x)**10 + np.cos(x*y + 10) * np.cos(x)
plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
plt.colorbar()