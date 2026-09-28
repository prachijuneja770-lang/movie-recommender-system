import streamlit as st
import pickle
import requests

# API Key
OMDB_API_KEY = "129fffb6"

def fetch_poster(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    data = requests.get(url).json()
    poster = data.get('Poster')
    if poster and poster!= "N/A":
        return poster
    return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    rec_movies = []
    rec_posters = []
    for i in movies_list:
        title = movies.iloc[i[0]].title
        rec_movies.append(title)
        rec_posters.append(fetch_poster(title))
    return rec_movies, rec_posters

# Load data
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# --- UPAR WALA PART ---
st.title("🎬 Movie Recommender")
st.markdown("<p style='text-align:center; color:gray;'>Find movies similar to your favourites</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>✨ Built with curiosity & a love for movies.</p>", unsafe_allow_html=True)

selected = st.selectbox("Type or select a movie:", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.write(names[i])

# --- NEECHE WALA FOOTER ---
st.markdown("""
<div style='background-color:#f0f2f6; padding:20px; border-radius:10px; text-align:left; margin-top:30px;'>
    <h3>About the Creator</h3>
    <p>Hi, I'm <b>Prachi</b> - B.Tech student and aspiring AI/ML developer.</p>
    <p style='font-size:14px; color:#666; margin-top:15px;'>Built with Streamlit • © 2026 Prachi • Privacy</p>
</div>
""", unsafe_allow_html=True)