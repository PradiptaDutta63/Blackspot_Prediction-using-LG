#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_univariate(df, column):
    """Plot a univariate distribution of a column."""
    sns.histplot(df[column], kde=True)
    plt.title(f'Univariate Analysis of {column}')
    plt.show()

def plot_bivariate(df, col1, col2):
    """Plot a bivariate relationship."""
    sns.scatterplot(x=col1, y=col2, data=df)
    plt.title(f'Bivariate Analysis between {col1} and {col2}')
    plt.show()

def plot_multivariate(df, cols):
    """Plot a multivariate analysis using a heatmap."""
    sns.heatmap(df[cols].corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

