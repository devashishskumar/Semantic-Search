import pandas as pd

# Load dataset
df = pd.read_csv("imdb_top_1000.csv")

# Display dataset info
print(df.head())


from sentence_transformers import SentenceTransformer
import numpy as np

# Load the embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for the "Overview" field
df['Embeddings'] = df['Overview'].astype(str).apply(lambda x: model.encode(x))

# Convert list embeddings to NumPy array
embeddings_matrix = np.array(df['Embeddings'].tolist())

# Save embeddings for future use
np.save("movie_embeddings.npy", embeddings_matrix)



import faiss

# Get embedding dimension
embedding_dim = embeddings_matrix.shape[1]

# Create FAISS index
index = faiss.IndexFlatL2(embedding_dim)

# Add embeddings to FAISS index
index.add(embeddings_matrix)

# Save the FAISS index
faiss.write_index(index, "faiss_index.idx")


def search_movies(query, top_k=5):
    """Search for similar movies based on a text query."""
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k=top_k)
    
    results = df.iloc[indices[0]][['Series_Title', 'Genre', 'IMDB_Rating', 'Overview', 'Director']]
    results['Similarity_Score'] = distances[0]  # Show similarity score
    
    return results

# Example search
query = "A sci-fi movie about space exploration"
search_results = search_movies(query)
print(search_results)


