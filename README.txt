Name: Devashish Sanjay Kumar
UTA ID: 1002157097
Course: 2252-CSE-6363-004


# Semantic Movie Search Engine

This project implements a **semantic search engine** for movies using **IMDB's Top 1000 movies dataset**. It allows users to enter a movie description and get relevant recommendations based on **text embeddings** and **vector similarity search**.

---

## **How to Run This Project Locally**

### **1. Install Dependencies**
Make sure you have Python installed, then install the required libraries:

```bash
pip install pandas numpy sentence-transformers faiss-cpu streamlit
```

---

### **2. Execute `semantic_search.py` (To Build Index)**
Before running the search engine, we need to **generate embeddings** and create a **vector database (FAISS index)**.

Run the following command:
```bash
python semantic_search.py
```
This will:
- Load the **IMDB dataset**  
- Generate **text embeddings** for movie overviews  
- Store embeddings in a **FAISS vector database**  
- Save the index for fast retrieval  

---

### **3. Run the Streamlit App (`app.py`)**
Once the index is built, you can start the **web application**.

Run:
```bash
streamlit run app.py
```

Then open the browser at:
```
http://localhost:8501
```
Now, enter a movie description (e.g., *"A sci-fi movie about space travel"*), and the app will suggest relevant movies.

---

## **What We Used**
### **Libraries & Technologies**
- **[Sentence Transformers](https://www.sbert.net/)** – For generating **text embeddings**  
- **[FAISS](https://faiss.ai/)** – For fast **vector search** (cosine similarity)  
- **[Streamlit](https://streamlit.io/)** – To build a **web-based search engine**  
- **Pandas & NumPy** – For handling and processing **IMDB dataset**  

---

## **Process Workflow**
### **1. Data Preprocessing**
- Loaded **IMDB Top 1000 movies dataset** (`imdb_top_1000.csv`).
- Extracted the **"Overview"** field to generate embeddings.
- Optionally, we can improve embeddings by including **"Genre", "Director", etc."**.

### **2. Embedding Generation**
- Used **Hugging Face’s `all-MiniLM-L6-v2` model** to convert text into numerical vectors.
- Stored embeddings in a **FAISS vector index**.

### **3. Semantic Search**
- When a user enters a description, we:
  1. Convert it to an **embedding**.
  2. Find the **top-k similar movies** using **FAISS cosine similarity**.
  3. Display movie details like **title, genre, rating, and overview**.

### **4. Streamlit UI**
- Users enter a movie description, and we **return matching movies** instantly.

---

## **Additional Files**
### **Semantic Search Jupyter Notebook**
For reference, a **Jupyter Notebook** is included with code snippets to explore the dataset and test semantic search.

### **Dataset**
The **IMDB dataset (`imdb_top_1000.csv`)** is provided for training and retrieval.

---

## **Next Steps & Improvements**
- Add **IMDB rating filters** in the Streamlit app  
- Improve **search quality** by concatenating more metadata (genre, director, etc.)  
- Deploy the app on **AWS, Hugging Face Spaces, or Streamlit Cloud**  

---


