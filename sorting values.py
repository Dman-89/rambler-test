# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 10:24:48 2017

@author: fialdm01
"""
import pandas as pd

x = [1, 2, 3]
y = [4, 6, 5]
#zipped = zip(y, x)
#list(zipped)

y2, x2 = zip(*sorted(zip(y, x)))
y2=list(y2)
x2=list(x2)

    
df = pd.DataFrame({'x':[1,2,3], 'y':[4,6,5]})
df.sort_values('y', inplace=True)