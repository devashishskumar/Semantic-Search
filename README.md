# Semantic Movie Search Engine

A powerful semantic search engine for movies that uses natural language processing and vector similarity to find movies based on descriptions. This project leverages IMDB's Top 1000 movies dataset and modern NLP techniques to provide intelligent movie recommendations.

## 🌟 Features

- Natural language movie search using semantic similarity
- Fast vector search using FAISS
- Web-based interface built with Streamlit
- Pre-computed embeddings for quick results
- Support for top-k similar movies retrieval

## 🛠️ Technologies Used

- **Sentence Transformers** (`all-MiniLM-L6-v2`) - For generating text embeddings
- **FAISS** - For efficient vector similarity search
- **Streamlit** - For the web interface
- **Pandas & NumPy** - For data processing
- **Python 3.x** - Core programming language

## 📦 Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install pandas numpy sentence-transformers faiss-cpu streamlit
```

## 🚀 Getting Started

### 1. Generate Embeddings and Index

First, run the semantic search preprocessing script:

```bash
python semantic_search.py
```

This will:
- Load the IMDB dataset
- Generate embeddings for movie descriptions
- Create and save the FAISS index

### 2. Launch the Web Interface

Start the Streamlit application:

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser to start searching!

## 📁 Project Structure

- `app.py` - Streamlit web application
- `semantic_search.py` - Core search functionality and index generation
- `imdb_top_1000.csv` - Movie dataset
- `movie_embeddings.npy` - Pre-computed embeddings
- `faiss_index.idx` - FAISS similarity search index
- `Semantic Search.ipynb` - Jupyter notebook with development process

## 🔍 How It Works

1. **Data Preprocessing**:
   - Loads IMDB movie dataset
   - Extracts movie overviews and metadata

2. **Embedding Generation**:
   - Uses Sentence Transformers to convert text to vectors
   - Creates numerical representations of movie descriptions

3. **Search Process**:
   - Converts user query to embedding
   - Uses FAISS to find similar movie vectors
   - Returns top-k matching movies with metadata

## 🎯 Example Usage

Enter natural language descriptions like:
- "A sci-fi movie about space exploration"
- "A romantic comedy set in New York"
- "An action-packed superhero movie"

The system will return the most semantically similar movies from the database.

## 🔄 Future Improvements

- Add filtering by IMDB rating, year, and genre
- Enhance search quality by incorporating more metadata
- Deploy to cloud platforms (AWS, Hugging Face Spaces)
- Add user feedback and recommendation history

## 👤 Author

**Devashish Sanjay Kumar**  
UTA ID: 1002157097  
Course: CSE-6363-004
