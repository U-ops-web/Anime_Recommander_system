import streamlit as st
from pipeline.pipeline import AnimeRecommenadtionpipeline
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title='Anime Recommander',layout = 'wide')

@st.cache_resource
def init_pipeline():
    return AnimeRecommenadtionpipeline()

pipeline = init_pipeline()


st.title("Anime Recommender System")

query = st.text_input("Enter your anime prefernces eg. : light hearted anime with school settings")
if query:
    with st.spinner("Fetching recommendations for you....."):
        response = pipeline.recommand(query)
        st.markdown("### Recommendations")
        st.write(response)