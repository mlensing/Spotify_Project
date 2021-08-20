import pandas as pd
import numpy as np
import random
from datetime import timedelta
import ast

def fave_song_cluster(current_fave_song, songs_1995):
    # takes in one of the user's favorite songs
   fave_song = songs_1995[songs_1995['lower_name']==current_fave_song]
   # gets the cluster number of that song and returns it
   fave_song_cluster_number = fave_song.reset_index().kmeans_cluster[0]
   return fave_song_cluster_number

def fave_song_release_date(current_fave_song, songs_1995):
    songs_1995['release_date'] = pd.to_datetime(songs_1995['release_date'])
    # finds the release date of the user's favorite song
    date = songs_1995[songs_1995['lower_name']== current_fave_song][['release_date']].reset_index().release_date[0]
    return date

def return_song_suggestion(current_fave_song):
    songs_1995 = pd.read_csv('songs_1995_kmeans.csv')
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
    first_song_artist = ast.literal_eval(song_artists)[0]
    # print song name and artist(s) to the user
    print(f'Song: {song_name}')
    print(f'Artist(s): {song_artists}')
    return {'Song' : song_name, 'Artist': first_song_artist}

