# Spotify Song Recommender

For my final project in my MSBA program (Master's of Business Analytics), I created a simple Spotify song recommender. I first used principal component analysis (PCA) to reduce the dimensionality of the dataset and increase the interpretability. I used the unsupervised learning method of k-means clustering to cluster over 250,000 Spotify songs. For the clustering, I used song attributes like popularity, danceability, energy, loudness, acousticness, liveliness, etc., which were then reduced down into just 2 variables using PCA.

I then used the song clusters to create an algorithm that recommends a user a new song, given one of their current favorite songs. With this algorithm I was able to finally build an API, host my Python code on Heroku, and connect this to GitHub pages in order to build a website.

Please feel free to check out my song recommender website at https://mlensing.github.io/Spotify_Project/ and give it a try for yourself!
