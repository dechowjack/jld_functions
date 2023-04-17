#!/usr/bin/env python
# coding: utf-8

# In[18]:


# This function serves to find the closest pixel in a list to the given coordinates. The input to this function are an 
# column vector of paired Lon/Lat or X/Y coordinates, an X/Lon Value, a Y/Lat Value, and the preferred indexing start 
# zero or one. I originally wrote this script in MATLAB and still do large amounts of data anlaysis in MATLAB so I
# have left this option.

import numpy as np
import pandas as pd
import csv


# In[21]:


def nearest_idxf(xval,yval,coords_x,coords_y,return_index):
    
    dl = len(coords_y)
    x_list = np.empty([dl,1]) 
    y_list = np.empty([dl,1])
    dist = np.empty([dl,1])

    x_list[:,0] = xval ; y_list[:,0] = yval; 
    
    x_diff = np.subtract(x_list[:],coords_x[:])
    y_diff = np.subtract(y_list[:],coords_y[:])

    x_diff = x_diff**2
    y_diff = y_diff**2

    dist = np.add(x_diff,y_diff)
    dist = dist**0.5

    idx = np.argmin(dist)
    
    return idx + return_index


# In[ ]:




