# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 11:09:29 2021

@author: Mario
"""

import numpy as np
import pandas as pd

file = open('input.txt','r')
line = file.readline()
file.close()

#%%
string_list = line.split(',')
integer_map = map(int, string_list)
numbers = np.asarray(list(integer_map))

print('The list of numbers in order are: \n', numbers)

#%%
data = pd.read_csv('input.txt', skiprows=2, header=None, delim_whitespace=True)


winning_idx = -1
for number in numbers:
    if len(data) == 5:
            break
    
    data = data.replace(to_replace=number, value=np.NAN)

    for i in data.index:
        
        
        
        if i % 5 == 0 and (data.loc[i:i+4,:].isnull().all().any() or data.loc[i:i+4,:].isnull().all(axis=1).any()):
            winning_idx = i
            print('Winning index {}'.format(i))
            
            data.drop([i, i+1, i+2, i+3, i+4], inplace=True)
    
    
    # if winning_idx != -1:
    #     break

print('')
print('Last winning bingo table:')
print(data)

