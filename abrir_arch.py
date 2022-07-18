# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 22:35:45 2021

@author: Caroline
"""
import pandas as pd

csv_path = 'C:/Users/Caroline/Pictures/Departments.csv'

df = pd.read_csv(csv_path)

print(df.head())
