import pandas as pd
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
# choosing 7 clusters for kmeans ...... based on inertia and silhouette scores
k7 = KMeans(7)
k7.fit(songs_scaled)
k7_labs = k7.predict(songs_scaled)

songs_1995["kmeans_cluster"] = k7_labs

def fave_song_cluster(current_fave_song, songs_1995):
    # takes in one of the user's favorite songs
   fave_song = songs_1995[songs_1995['name']==current_fave_song]
   # gets the cluster number of that song and returns it
   fave_song_cluster_number = fave_song.reset_index().kmeans_cluster[0]
   return fave_song_cluster_number

def fave_song_release_date(current_fave_song, songs_1995):
    # finds the release date of the user's favorite song
    date = songs_1995[songs_1995['name']== current_fave_song][['release_date']].reset_index().release_date[0]
    return date

def return_song_suggestion(songs_1995):
    current_fave_song = input("Enter one of your favorite songs: ")
    # find the cluster of the person's favorite song and then filter song dataframe to only have songs with that cluster
    cluster_num = fave_song_cluster(current_fave_song, songs_1995)
    same_cluster_songs = songs_1995[songs_1995['kmeans_cluster']==cluster_num]
    # find release date of favorite song
    released_on = fave_song_release_date(current_fave_song, songs_1995)
    # filter songs to be released within 3 years of the favorite song
    three_year_delta = timedelta(days=1095)
    min_date = released_on - three_year_delta
    max_date = released_on + three_year_delta
    filtered_same_cluster_songs = same_cluster_songs = songs_1995[(songs_1995['release_date']>=min_date) & (songs_1995['release_date']<=max_date)].reset_index()
    # pick a random song in this filtered same cluster song list
    length_of_song_list = len(filtered_same_cluster_songs)
    random_song_selection = random.randint(0,(length_of_song_list-1))
    song_name = filtered_same_cluster_songs.name[random_song_selection]
    song_artists = filtered_same_cluster_songs.artists[random_song_selection]
    # print song name and artist(s) to the user
    print(f'Song: {song_name}')
    print(f'Artist(s): {song_artists}')


return_song_suggestion(songs_1995)