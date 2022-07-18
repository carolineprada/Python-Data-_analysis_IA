# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 22:26:10 2021

@author: Caroline
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()

def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)
    
    
link1 = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv'
link2 = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'


#Question 1: Create a dataframe that contains the GDP data and display the first five rows of the dataframe
##Use the dictionary links and the function pd.read_csv to create a Pandas dataframes that contains the GDP data.
##Hint: links["GDP"] contains the path or name of the file.
df = pd.read_csv(link1) #GDP


##Use the method head() to display the first five rows of the GDP data, then take a screen-shot.
#print(df.head())



#Question 2: Create a dataframe that contains the unemployment data. Display the first five rows of the dataframe. ¶
##Use the dictionary links and the function pd.read_csv to create a Pandas dataframes that contains the unemployment data.

dt = pd.read_csv(link2) #unemployment

##Use the method head() to display the first five rows of the GDP data, then take a screen-shot.
#print(dt.head())


#Question 3: Display a dataframe where unemployment was greater than 8.5%. Take a screen-shot.
#dt.query('unemployment > 8.5', inplace = True)
#print(dt.query)



#Question 4: Use the function make_dashboard to make a dashboard¶
##In this section, you will call the function make_dashboard , to produce a dashboard. We will use the convention of giving each variable the same name as the function parameter.
##Create a new dataframe with the column 'date' called x from the dataframe that contains the GDP data.

##PARTE 1
x = pd.DataFrame(df, columns=['date'])
print(x.head())


##PARTE 2
gdp_change = pd.DataFrame(df, columns=['change-current'])
print(gdp_change.head())


##PARTE 3
unemployment = pd.DataFrame(dt, columns=['unemployment'])
print(unemployment.head())


##Give your dashboard a string title, and assign it to the variable title
title = "GDP and Unemployment Data"

#Finally, the function make_dashboard will output an .html in your direictory, just like a csv file. The name of the file is "index.html" and it will be stored in the varable file_name.
file_name = "index.html"


##Call the function make_dashboard , to produce a dashboard. Assign the parameter values accordingly take a the , take a screen shot of the dashboard and submit it.
make_dashboard(x = pd.DataFrame(df, columns=['date']), gdp_change = pd.DataFrame(df, columns=['change-current']), unemployment = pd.DataFrame(dt, columns=['unemployment']), title = "GDP and Unemployment Data", file_name = "index.html")
#output_file("index.html")
output_notebook()
p = figure(title=title, x_axis_label='year', y_axis_label='%')
p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
show(p)








































