#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1: Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


# Step 2: Load dataset
df = pd.read_csv("Placement_dataset.csv")


# In[ ]:


# Step 3: Explore data
print(df.shape)
print(df.info())
print(df.head())


# In[ ]:


# Step 4: Scatter plot
plt.scatter(df['cgpa'], df['iq'], c=df['placement'], cmap='rainbow')
plt.title("Placement Data (CGPA vs IQ)")
plt.xlabel("CGPA")
plt.ylabel("IQ")
plt.show()


# In[ ]:


# Step 5: Define features (X) and target (y)
X = df.iloc[:, 0:2]    # CGPA, IQ
y = df.iloc[:, -1]     # Placement (target)

print(X.head())
print(y.head())


# In[ ]:


# Step 6: Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42
)


# In[ ]:


# Step 7: Feature scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# In[ ]:


# Step 8: Train Logistic Regression model
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(X_train, y_train)


# In[ ]:


# Step 9: Predictions
y_pred = clf.predict(X_test)


# In[ ]:


# Step 10: Evaluate accuracy
from sklearn.metrics import accuracy_score
print("Accuracy:", accuracy_score(y_test, y_pred))


# In[ ]:


# Step 11: Visualize decision boundary
get_ipython().system('pip install mlxtend')
from mlxtend.plotting import plot_decision_regions

plot_decision_regions(X_train, y_train.values, clf=clf, legend=2)
plt.show()


# In[ ]:


# Step 12: Save model with pickle
import pickle
pickle.dump(clf, open("model.pkl", "wb"))

