import streamlit as st
import pickle
import requests

movies=pickle.load(open('df_list.pkl','rb'))
sim=pickle.load(open('sim_list.pkl','rb'))
movies_list=movies['title'].values

st.header('Movie Recommender System')
select_value=st.selectbox('Select movie from dropdown',movies_list)

def fetch_poster(movie_id):
    url='https://api.themoviedb.org/3/movie/{}?api_key=007d858440bee9ef1a10988eaf1da52c'.format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path='https://image.tmdb.org/t/p/w500/' + poster_path
    return full_path

def recommend(df):
    index=movies[movies['title']==df].index[0]
    main=sorted(list(enumerate(sim[index])),reverse=True,key=lambda vector:vector[1])
    
    recommend_movies=[]
    recommend_poster=[]
   
    for i in main[1:6]:
         movies_id=movies.iloc[i[0]].id
         recommend_movies.append(movies.iloc[i[0]].title)
         recommend_poster.append(fetch_poster(movies_id))
    return  recommend_movies,recommend_poster

if st.button('Show Recommend'):
    movie_name,movie_poster=recommend(select_value)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
         st.text(movie_name[0])
         st.image(movie_poster[0])
    with col2:
         st.text(movie_name[1])
         st.image(movie_poster[1])
    with col3:
         st.text(movie_name[2])
         st.image(movie_poster[2])
    with col4:
         st.text(movie_name[3])
         st.image(movie_poster[3])
    with col5:
         st.text(movie_name[4])
         st.image(movie_poster[4])