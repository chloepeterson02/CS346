# Github Repository / Commit

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px


dat = pd.read_csv('mydat')

target = 'female'

subdat = dat.loc[dat['gender' == target]]
out = subdat['salary'].mean()
out

sub1 = dat.loc[dat['gender' == 'Female']]
out1 = sub1['salary'].mean()
out1

#Find average salary of males
sub2 = dat.loc[dat['gender' == 'Male']]
out2 = subdat2['salary'].mean()
out2

#Define target
grade = 1 
stat = 'mean'


#User Inputs in Streamlit (Define target)
grade = st.slider('Pick grade', 1, 12)
stat = st.selectbox('Pick stat', ['mean', 'median', 'max', 'min'])

# 