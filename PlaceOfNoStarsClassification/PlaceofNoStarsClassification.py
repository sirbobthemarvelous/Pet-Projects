#https://scikit-learn.org/stable/modules/clustering.html
import numpy as np
import pandas as pd
import sklearn
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib import style
#clan thunder, shadow, wind, river, sky

data = pd.read_csv(r"C:\Users\robzh\Documents\python\Pet Projects Only For Fun (not Counting Nifty)\PlaceOfNoStarsClassification\Two Variable Place of No Stars Classification.csv")
print(data.head())

#del data['Name'] delete a column this way with pandas
kmeans = KMeans(n_clusters=3, random_state=0).fit(data[['Mentions','Clan']])
#use double square brackets for multiple dataframe columns
#print(kmeans.cluster_centers_)
data['Clusters'] = kmeans.labels_ #adding a column

#print(data['Clusters'].value_count()) #how many in each cluster
data.to_csv(index=False) # export data...double check this

style.use("ggplot")
plt.scatter(x='Mentions',y='Clan',c = 'Clusters', data=data)
plt.title('Place of No Stars Characters by Clan and Relevance')
plt.xlabel('Times Mentioned')
plt.ylabel("Clan")
#ok its FUnctional now add labels
plt.show()