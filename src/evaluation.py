#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.metrics import accuracy_score, precision_score, confusion_matrix, roc_curve
import matplotlib.pyplot as plt

def evaluate_model(y_test, y_pred):
    """Evaluate the model's performance."""
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    print(f'Accuracy: {accuracy:.2f}')
    print(f'Precision: {precision:.2f}')
    print(f'Confusion Matrix:\n{cm}')

def plot_roc(y_test, y_pred_proba):
    """Plot the ROC curve."""
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    plt.plot(fpr, tpr, marker='.')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.show()

