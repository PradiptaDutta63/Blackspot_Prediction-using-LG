#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train):
    """Train a logistic regression model."""
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def predict(model, X_test):
    """Generate predictions using the trained model."""
    return model.predict(X_test)

