#https://scikit-learn.org/stable/modules/clustering.html
import numpy as np
import pandas as pd
import sklearn
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#clan thunder, shadow, wind, river, sky

data = pd.read_csv(r"C:\Users\robzh\Documents\python\Pet Projects Only For Fun (not Counting Nifty)\PlaceOfNoStarsClassification\Two Variable Place of No Stars Classification.csv")
print(data.head())

#del data['Name'] delete a column this way with pandas
kmeans = KMeans(n_clusters=3, random_state=0).fit(data[['Mentions','Clan']])
#use double square brackets for multiple dataframe columns
print(kmeans.cluster_centers_)
data['Clusters'] = kmeans.labels_ #adding a column
print(data)
