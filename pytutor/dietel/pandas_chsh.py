#%% [markdown]
# # Pandas
# Created by Wes McKinney in 2008 to handle structures that could 
# handle both time and non-time based data.  The name comes from 
# 'panel data' which is data for measurement over time.

#%% Imports
import pandas as pd

#General Settings
pd.set_option('precision', 2)

#%% Series

grades = pd.Series([87,100,94], index=['Wally','Eva','Katie'])
print(grades['Wally'] + grades.Katie)

hardware = pd.Series(['Hammer','Saw','Wrench'])
print(hardware.str.contains('a'))  #applies the function to each element


#%% DataFrames -
# Columns, Values, Index
grades_dict = {'Wally':[87, 96, 70], 'Eva': [100,87,90], 'Katie':[100,81,82]}
grades = pd.DataFrame(grades_dict, index=['Test1', 'Test2', 'Test3'])


#%% Searching
# loc, iloc, at and iat are more robust and dont make copies, 
# instead of direct []

print(grades.loc['Test1'], grades.iloc[1])
print(grades.loc['Test1':'Test3'], grades.iloc[0:2])

print(grades[(grades>=80) & (grades<=90)])
print('Complex Search\n', 
  grades.loc[(grades.Katie >= 80) & (grades.Katie <= 90), ['Katie']])

print(grades.at['Test2','Eva'])
print(grades.iat[2,0])

#%% Descriptive Statistics
print(grades.describe())
print(grades.mean())
print(grades.T) #transpose

#%% Sorting
print(grades.sort_index(ascending=False))
print(grades.sort_index(axis=1)) #by column
print(grades.sort_values(by='Test2', axis=1, ascending=False))
grades.T.sort_values(by='Test3', inplace=False) #inplace to not copy


#%% Search and Sort
grades.loc['Test1'].sort_values(ascending=False)


#%%
