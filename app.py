import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# load dataset
movies=pd.read_csv("C:\\Users\\Acer\\Downloads\\tmdb_5000_movies.csv")
movies = movies[['title', 'genres', 'keywords', 'overview']]
movies.dropna(inplace=True)

# Combine relevant text columns
movies['combined'] = movies['genres'] + ' ' + movies['keywords'] + ' ' + movies['overview']

# combined text into numbers
tfidf=TfidfVectorizer(stop_words='english')
tfidf_matrix=tfidf.fit_transform(movies['combined'])

# calculate similarity
similarity=cosine_similarity(tfidf_matrix)

# streamlit
st.title("🎬 Movie Recommender System")
movie_list = ['Select a movie'] + sorted(movies['title'].tolist())
movie_input = st.selectbox("Choose a movie title:", movie_list)

# movie recommendation
if movie_input!='Select a movie':
    if movie_input in movies['title'].values:
        index=movies[movies['title'].str.lower()==movie_input.lower()].index[0]

        # similarity score
        scores=list(enumerate(similarity[index]))
        scores=sorted(scores,key=lambda x: x[1],reverse=True)

        top_movies=scores[1:6]

        st.subheader("Recommended Movies..")
        for i in top_movies:
            movie_title=movies.iloc[i[0]]['title']
            movie_overview = movies.iloc[i[0]]['overview']

            st.markdown(f"**🎬{movie_title}**")
            st.write(movie_overview)
            st.markdown("---")
    else:
        st.error("Movies not found")
