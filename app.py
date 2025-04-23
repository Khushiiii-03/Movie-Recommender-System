import streamlit as st
import pickle
import pandas as pd

movie_dict= pickle.load(open('movie_dict.pkl', 'rb'))
movies= pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

option = st.selectbox("Choose Movie",movies['title'].values)
st.write("You selected:", option)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie=[]
    for i in movie_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie

if st.button('Recommend Movie'):
    recommendation = recommend(option)
    for i in recommendation:
        st.write(i)