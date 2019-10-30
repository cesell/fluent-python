#%% [markdown] 
# # Data Wrangling
import pandas as pd
import re

# ## Cleaning Data



#%% [markdown]
# ## Data Validation with regular expressions

zips = pd.Series({'Boston' : '02215', 'Miami' : '3310'})
print(zips.str.match(r'\d{5}')) #Valid ZIP

cities = pd.Series(['Boston MA 02215', 'Miami FL 33101'])
print(cities.str.contains(r'[A-Z]{2}')) #Has 2 letter code for state

#%% [markdown]
# ## Formatting Data with MAP

contacts = [['Mike Green', 'demo1@deitel.com', '5555555555'],
            ['Sue Brown', 'demos@deitel.com', '6666666666']
           ]
df = pd.DataFrame(contacts, columns = ['Name', 'Email', 'Phone'])

def format_phone(value):
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    return '-'.join(result.groups()) if result else value

df['Phone'] = df['Phone'].map(format_phone)
print(df)

#%%
