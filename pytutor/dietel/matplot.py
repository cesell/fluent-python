#%% [markdown]
# # Matplotlib
# This is a litte extra, not related with OOP

from oop_chsh import Card, DeckOfCards

from pathlib import Path
path = Path('.').joinpath('card_images') # path to current dir, joins images

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from scipy import stats
import seaborn as sns

figure, axes_list = plt.subplots(nrows=4, ncols=13)

#%% 

deck_of_cards = DeckOfCards()

for axes in axes_list.ravel():  #so we can access the matrix as an array
    axes.get_xaxis().set_visible(False) # hide x axis
    axes.get_yaxis().set_visible(False) # hide y axis
    image_name = deck_of_cards.deal_card().image_name
    # joinpath to add the image name to the path
    # resolve converts a relative path ..\.. to an absolute path
    # then get the str representation for the absolute path
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

plt.show()


#%% Linear Regression

nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')
nyc.columns = ['Date', 'Temperature', 'Anomaly']
nyc.Date = nyc.Date.floordiv(100)
linear_regression = stats.linregress(x=nyc.Date, y=nyc.Temperature)

sns.set_style('whitegrid')
axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)
axes.set_ylim(10,70)


#%%
