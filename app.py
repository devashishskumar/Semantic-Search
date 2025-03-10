import pandas as pd
import numpy as np
import streamlit as st
import faiss
from sentence_transformers import SentenceTransformer

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("imdb_top_1000.csv")
    return df

df = load_data()

# Load FAISS index
@st.cache_resource
def load_faiss():
    return faiss.read_index("faiss_index.idx")

index = load_faiss()

# Load sentence-transformers model
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# Function to perform semantic search
def search_movies(query, top_k=5):
    """Search for similar movies based on a text query."""
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k=top_k)
    
    results = df.iloc[indices[0]][['Series_Title', 'Genre', 'IMDB_Rating', 'Overview', 'Director']]
    results['Similarity_Score'] = distances[0]  # Show similarity score
    
    return results

# Streamlit UI
st.title("🎬 Semantic Movie Search Engine")
st.write("Describe a movie you'd like to watch, and we'll find similar ones!")

query = st.text_input("Enter your movie description here:")

if query:
    results = search_movies(query)
    
    for _, row in results.iterrows():
        st.subheader(row['Series_Title'])
        st.write(f"**Genre:** {row['Genre']}")
        st.write(f"**IMDB Rating:** {row['IMDB_Rating']}")
        st.write(f"**Director:** {row['Director']}")
        st.write(f"**Overview:** {row['Overview']}")
        st.write("---")