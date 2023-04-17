#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This is a simple function to calculate RMSE for two equal length datasets aka model data and a truth dataset
# First input is measured/truth, second is modeled/predicted

import numpy as np

def jld_rmse(meas,pred):

    dl = np.size(meas)
    
    residual = np.subtract(meas,pred)
    sum_rs = np.nansum(residual**2)
    
    sum_rs_div = sum_rs/dl
    
    result = np.sqrt(sum_rs_div)

    return result

