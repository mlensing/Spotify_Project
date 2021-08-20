
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances 
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn import metrics
import random
from datetime import timedelta
from sklearn.decomposition import PCA
import pandas as pd

songs_1995 = pd.read_csv('/Users/michellelensing/Documents/MSBA/Spotify Project/songs_1995.csv')
songs_1995 = songs_1995.drop(['Unnamed: 0'], axis=1)

songs_1995['release_date'] = pd.to_datetime(songs_1995['release_date'])
songs_clean = songs_1995.drop(columns=['id', 'duration_ms', 'artists', 'id_artists', 'release_date', 'key', 'time_signature', 'explicit', 'mode'])
songs_clean = songs_clean.set_index('name')

sc= StandardScaler()
songs_scaled = sc.fit_transform(songs_clean)

songs_scaled = pd.DataFrame(songs_clean, columns=songs_clean.columns)

pca = PCA()
pcs = pca.fit_transform(songs_scaled)

comps = pcs[:,:2]
pca_df = pd.DataFrame(comps,columns=["pc1","pc2"])

random.seed(42) 
# fit the model
k7 = KMeans(7)
k7.fit(songs_scaled)
k7_labs = k7.predict(songs_scaled)

songs_1995["kmeans_cluster"] = k7_labs

songs_1995_kmeans = songs_1995

songs_1995['lower_name'] = [str(x) for x in songs_1995.name]
songs_1995['lower_name'] = [x.lower() for x in songs_1995.lower_name]

songs_1995_kmeans.head()

songs_1995_kmeans.to_csv('/Users/michellelensing/Documents/MSBA/Spotify Project/songs_1995_kmeans.csv')
