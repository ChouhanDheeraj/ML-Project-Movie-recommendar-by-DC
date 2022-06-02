#from turtle import color
import streamlit as st
import pickle
import pandas as pd
import requests
#new_dmf = pd.DataFrame('movie_list_new')

def fetch_poster(movie_id):
    responce = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&language=en-US'.format(movie_id))
    data = responce.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index = movie_list_new[movie_list_new['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse = True,key = lambda x:x[1])[1:6]

    recommend_movies = []
    recommended_movie_poster = []
    for i in movie_list:
        movie_id = movie_list_new.iloc[i[0]].movie_id
        # fetch poster from API
        recommended_movie_poster.append(fetch_poster(movie_id))
        recommend_movies.append(movie_list_new.iloc[i[0]].title)
    return recommend_movies,recommended_movie_poster


movie_list_new = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movie_title = movie_list_new['title'].values
st.title('Movie Recommendor System by Mr. DC')
selected_movie_name = st.selectbox(
     'Please type your movie favourite movie name',
     movie_title)


if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
