# -*- coding: utf-8 -*-
"""Casualty Severity Prediction Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BssSmA8sBs5xiR_arDxHsPN61iNny4b5
"""

# Read the dataset
import pandas as pd
data = pd.read_csv("https://trello-attachments.s3.amazonaws.com/5cf2142046ceb163a0e4b189/5cf4e21e143159856a320b36/e353326f944665ae8a979a0573a8f9fa/Accident_Dataset_prepared.csv")
data.head(3)

independent_variables = data.columns
independent_variables = independent_variables.delete(5)
data1 = data[independent_variables]

# Perform clustering to prepare a clustered dataset
from sklearn.cluster import AgglomerativeClustering
agg_cluster = AgglomerativeClustering(n_clusters=3)

# Train the agglomerative clustering model
agg_cluster.fit(data1)

# Predict the cluster label
data["Cluster Labels"] = agg_cluster.fit_predict(data1)

# Select dependent and independent variables
Y = data["Casualty Severity"]
independent_variables = data.columns
independent_variables = independent_variables.delete(5)
X = data[independent_variables]

# Classify using Gradient Boosted Trees
from sklearn.ensemble import GradientBoostingClassifier
gbc = GradientBoostingClassifier()

#Train the model
gbc.fit(X, Y)

# Predict using GBC Classifier
data["Predicted Casualty Severity"] = gbc.predict(X)

# Take a user input and predict casualty severity
independent_variables = independent_variables.delete(8)

# Take user input and predict casualty
import sys
index = 1
user_input = {}
for var in independent_variables:
# temp = input("Enter "+var+":") 
  temp = sys.argv[index]
  index = index + 1
  user_input[var] = temp

# Calculate the cluster label
index = data1.shape[0]
user_df = pd.DataFrame(data=user_input, index=[index], columns=independent_variables)
data1 = pd.concat([data1, user_df], axis=0) # Add a new row in data1

data1["Cluster Labels"] = agg_cluster.fit_predict(data1)
data1.tail(3)

user_request = data1.tail(1)
severity = gbc.predict(user_request)
severity = severity[0]
if severity == 1:
  print("Casualty Severity is Slight (%d)" % severity)
elif severity == 2:
  print("Casualty Severity is Severe (%d)" % severity)
elif severity == 3:
  print("Casualty Severity is Fatal (%d)" % severity)
