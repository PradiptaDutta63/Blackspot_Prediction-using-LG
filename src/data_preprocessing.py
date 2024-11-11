#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    """Load the dataset."""
    return pd.read_csv(filepath)

def preprocess_data(df):
    """Preprocess the data by handling missing values, encoding categorical variables, and scaling features."""
    # Drop unnecessary columns
    df.drop(columns=['Unnecessary_Column'], inplace=True)
    
    # Fill missing values
    df['Column1'].fillna(df['Column1'].median(), inplace=True)
    df['Column2'].fillna(df['Column2'].mode()[0], inplace=True)
    
    # Encoding categorical features
    df = pd.get_dummies(df, columns=['Categorical_Column1', 'Categorical_Column2'])
    
    # Scaling numerical features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df.select_dtypes(include=['float64', 'int64']))
    
    return pd.DataFrame(scaled_features, columns=df.columns)

def split_data(df, target_column):
    """Split data into training and testing sets."""
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=0.3, random_state=42)

