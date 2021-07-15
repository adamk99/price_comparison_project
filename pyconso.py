# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:30:47 2021

@author: Karlen
"""
import pandas as pd
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print(cwd)

df = pd.read_csv("sf_military.csv")
rf = pd.read_csv('sf_hard.csv')

print(df.head())
print(rf.tail())